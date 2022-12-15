from bisect import bisect_left
from datetime import datetime, timedelta
from typing import Dict
from config import Config


from models.fee import FeeModel
from util.dateutil import DateUtil
from models import VehicleType
from models.ticket import Ticket


class Process:
    slots: Dict[VehicleType, list] = {}
    tickets: Dict[str, Ticket] = {}
    fee_list: Dict[VehicleType, FeeModel] = {}

    def __setup_slot(self):
        for vehicle_type in self.config['allowed_vehicle'].keys():
            self.slots[vehicle_type] = ['A' for count in range(
                self.config['allowed_vehicle'][vehicle_type]['slot'])]

    def __setup_fee_list(self):
        for vehicle_type in self.config['allowed_vehicle'].keys():
            vehicle_type_config = self.config['allowed_vehicle'][vehicle_type]
            if vehicle_type_config['fee_model_type'] == 'fixed':
                self.fee_list[vehicle_type] = FeeModel(vehicle_type_config['fee_model_type'],
                                                       fee=vehicle_type_config['fee'])
            else:
                self.fee_list[vehicle_type] = FeeModel(vehicle_type_config['fee_model_type'],
                                                       fee_list=vehicle_type_config['fee'])

    def __init__(self, config_file: str) -> None:
        self.config: dict = Config.load_config_file(config_file)
        Config.validate_config(self.config)
        self.__setup_slot()
        self.__setup_fee_list()

    def __allocate_slot(self, vehicle_type: VehicleType) -> str:

        slot_number: str = ''

        slot = bisect_left(self.slots[vehicle_type], 'A')
        if slot != len(self.slots[vehicle_type]):
            slot_number = str(slot + 1).zfill(4)
            self.slots[vehicle_type][slot] = slot_number
            return slot_number
        return slot_number

    def __unallocate_slot(self, vehicle_type: VehicleType, slot_number: str) -> None:

        slot = int(slot_number) - 1
        self.slots[vehicle_type][slot] = 'A'

    def park(self, vehicle_type: VehicleType, parking_time: datetime) -> Ticket:

        available_slot = self.__allocate_slot(vehicle_type)
        if available_slot:
            parking_ticket = Ticket(available_slot, vehicle_type, parking_time)
            self.tickets[parking_ticket.number] = parking_ticket
            return parking_ticket
        else:
            raise Exception('Slot is not available')

    def __fee_calculation(self, vehicle_type, parking_time: timedelta) -> float:
        fee_model = self.fee_list[vehicle_type]
        hours = DateUtil.to_hours(parking_time)

        total_fees: float = 0.0
        fees: list = []
        if fee_model.fee_type == 'fixed':
            total_fees = fee_model.fee * hours
        elif fee_model.fee_type == 'interval_hours':
            fees = fee_model.fee_list
            for index in range(len(fees)):
                if fees[index][0] == '#':
                    total_fees = fees[index - 1][1]
                    extra_hours = DateUtil.to_hours(
                        timedelta(hours=hours) - timedelta(hours=fees[index - 1][0]))
                    total_fees += extra_hours * fees[index][1]
                    break
                if hours <= fees[index][0]:
                    total_fees = fees[index][1]
                    break
        elif fee_model.fee_type == 'interval_days':
            fees = fee_model.fee_list
            for index in range(len(fees)):
                if fees[index][0] == '#':
                    total_fees = fees[index - 1][1]
                    extra_hours = DateUtil.to_hours(
                        timedelta(hours=hours) - timedelta(hours=fees[index - 1][0]))
                    extra_days = int(extra_hours / 24)
                    extra_days += 1 if extra_hours % 24 > 0 else 0
                    total_fees += extra_days * fees[index][1]
                    break
                if hours <= fees[index][0]:
                    total_fees = fees[index][1]
                    break

        return total_fees

    def unpark(self, ticket_number: str, checkout_time: datetime) -> float:
        if ticket_number not in self.tickets:
            raise Exception(f'Ticket {ticket_number} not found')

        ticket = self.tickets[ticket_number]
        self.__unallocate_slot(ticket.vehicle_type, ticket.slot_number)
        del self.tickets[ticket_number]

        hours: timedelta = checkout_time - ticket.parking_time

        hours = DateUtil.ceil_hour(hours)
        return self.__fee_calculation(ticket.vehicle_type, hours)

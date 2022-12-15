from datetime import datetime
from models import VehicleType
from util.generator import ID

class Ticket:
    number: str
    vehicle_type: VehicleType
    slot_number: str
    parking_time: datetime
    
    def __init__(self, slot_number: str, vehicle_type: VehicleType, parking_time: datetime) -> None:
        self.number = ID.upper_case_alpha(5)
        self.vehicle_type = vehicle_type
        self.slot_number = slot_number
        self.parking_time = parking_time

import json
from os import path
from exception import InvalidConfigException


class Config:

    @staticmethod
    def load_config_file(config_file: str) -> dict:
        if path.exists(config_file):
            with open(config_file) as config_fs:
                config: dict = json.load(config_fs)
                return config
            
        return {}

    @staticmethod
    def validate_config(config: dict) -> bool:
        
        if 'name' not in config:
            raise InvalidConfigException('Sit name is missing in the config file')
        
        if 'type' not in config:
            raise InvalidConfigException('Sit type is missing in the config file')
        elif config['type'] not in ['mall', 'stadium', 'airport', 'train_station']:
            raise InvalidConfigException(f"{config['type']} is not valid site type")
        
        if 'allowed_vehicle' not in config:
            raise InvalidConfigException('allowed_vehicle is missing in the config file')
        else:
            allowed_vehicle: dict = config['allowed_vehicle']
            for vehicle_type in allowed_vehicle.keys():
                if vehicle_type not in ['motorcycle', 'car', 'bus']:
                    raise InvalidConfigException('Wrong vehicle type found in the allowed_vehicle')
                
                if 'slot' not in allowed_vehicle[vehicle_type]:
                    raise InvalidConfigException(f"No of slots missing for the vehicle_type {vehicle_type}")
                
                if 'fee_model_type' not in allowed_vehicle[vehicle_type]:
                    raise InvalidConfigException(f"fee_model_type configuration missing for the vehicle_type {vehicle_type}")
                elif allowed_vehicle[vehicle_type]['fee_model_type'] not in ['fixed', 'interval_hours', 'interval_days']:
                    raise InvalidConfigException(f"Invalid fee_model_type for the vehicle_type {vehicle_type}")
                
                
                if 'fee' not in allowed_vehicle[vehicle_type]:
                    raise InvalidConfigException(f"fee configuration missing for the vehicle_type {vehicle_type}")
                else:
                    
                    fee_config = allowed_vehicle[vehicle_type]['fee']
                    
                    if allowed_vehicle[vehicle_type]['fee_model_type'] == 'fixed':
                        if type(fee_config) != float:
                            raise InvalidConfigException(f"Invalid fee configuration for the vehicle_type {vehicle_type}")
                    else:
                        if type(fee_config) != list:
                            raise InvalidConfigException(f"Invalid fee configuration for the vehicle_type {vehicle_type}")
                        
                        if fee_config[-1][0] != '#':
                            raise InvalidConfigException(f"Infinity fee configuration is missing or not in right position for the vehicle_type {vehicle_type}")
                    
                    
        return True


from datetime import timedelta


class DateUtil:
    
    @staticmethod
    def ceil_hour(val: timedelta) -> timedelta:
        return_value = val
        
        if val.seconds % 3600 > 0:
            
            excess_seconds = val.seconds % 3600            
            return_value = return_value - timedelta(seconds=excess_seconds)
            return_value = return_value + timedelta(hours=1)
            
        return return_value

    @staticmethod    
    def to_hours(val: timedelta) -> int:
        return (val.days * 24) + int(val.seconds / 3600)
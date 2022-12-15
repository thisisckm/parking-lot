
class FeeModel:
    
    fee_type: str
    fee: float
    fee_list: list
    
    def __init__(self, fee_type: str, fee: float = 0.0, fee_list:list = []) -> None:
        self.fee_type = fee_type
        
        self.fee = fee 
        self.fee_list = fee_list
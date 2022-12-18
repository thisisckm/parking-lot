class InvalidConfigException(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

class ProcessException(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

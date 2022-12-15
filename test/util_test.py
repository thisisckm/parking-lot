from datetime import timedelta
from util.dateutil import DateUtil
from util.generator import ID

class TestDateUtil:
    
    def test_ceil_hours(self):
        input = timedelta(hours=10, seconds=40)
        
        expected = timedelta(hours=11)
        actual = DateUtil.ceil_hour(input)
        
        assert actual == expected
        
        
class TestGenertor:
    
    def test_upper_case_alpha_id(self):
        actual = ID.upper_case_alpha(5)
        
        assert len(actual) == 5
        assert actual.isupper()
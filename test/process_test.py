from datetime import datetime, timedelta
from process import Process
from os import path


class TestProcess:
    
    def test_park_basic(self):
        process = Process(path.join("config", "config.json"))
        parking_time = datetime.strptime("2022-10-22 10:30:40", "%Y-%m-%d %H:%M:%S")
        
        actual = process.park('car', parking_time)
        assert actual.parking_time == parking_time
        assert actual.slot_number is not None
        assert actual.number is not None


    def test_unpark_basic(self):
        process = Process(path.join("config", "config.json"))
        
        parking_time = datetime.strptime("2022-10-22 10:30:40", "%Y-%m-%d %H:%M:%S")
        checkout_time = datetime.strptime("2022-10-22 11:31:40", "%Y-%m-%d %H:%M:%S")
        
        ticket = process.park('car', parking_time)
        
        actual = process.unpark(ticket.number, checkout_time)
        
        assert actual == 60.0
    
    def test_park_unpark_bus(self):
        process = Process(path.join("config", "config.json"))
        
        parking_time = datetime.strptime("2022-10-22 10:30:40", "%Y-%m-%d %H:%M:%S")
        checkout_time = datetime.strptime("2022-10-25 23:14:00", "%Y-%m-%d %H:%M:%S")
        
        ticket = process.park('bus', parking_time)
        
        actual = process.unpark(ticket.number, checkout_time)
        
        assert actual == 650.0
        
        
    def test_stadium_data(self):
        process = Process(path.join("test_config", "stadium-config.json"))
        
        # Motorcycle
        parking_time = datetime.strptime("2022-12-15 10:30:00", "%Y-%m-%d %H:%M:%S")
        checkout_time = datetime.strptime("2022-12-15 14:10:00", "%Y-%m-%d %H:%M:%S")
        
        ticket = process.park('motorcycle', parking_time)
        
        actual = process.unpark(ticket.number, checkout_time)
        
        assert actual == 30.0
        
        # Motorcycle
        parking_time = datetime.strptime("2022-12-15 08:10:21", "%Y-%m-%d %H:%M:%S")
        checkout_time = datetime.strptime("2022-12-15 23:09:21", "%Y-%m-%d %H:%M:%S")
        
        ticket = process.park('motorcycle', parking_time)
        
        actual = process.unpark(ticket.number, checkout_time)
        
        assert actual == 390.0
        
        # Electric SUV
        parking_time = datetime.strptime("2022-12-14 23:45:10", "%Y-%m-%d %H:%M:%S")
        checkout_time = datetime.strptime("2022-12-15 11:15:10", "%Y-%m-%d %H:%M:%S")
        
        ticket = process.park('car', parking_time)
        
        actual = process.unpark(ticket.number, checkout_time)
        
        assert actual == 180.0
        
        # SUV
        parking_time = datetime.strptime("2022-12-15 04:45:45", "%Y-%m-%d %H:%M:%S")
        checkout_time = datetime.strptime("2022-12-15 17:50:45", "%Y-%m-%d %H:%M:%S")
        
        ticket = process.park('car', parking_time)
        
        actual = process.unpark(ticket.number, checkout_time)
        
        assert actual == 580.0
        
        
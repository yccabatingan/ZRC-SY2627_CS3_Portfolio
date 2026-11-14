from abc import ABC, abstractmethod

class Get_reading(ABC):
    
    @abstractmethod
    
    def get_data(self):
        
        pass
    
class TempSensor(Get_reading):
    
    def get_data(self):
        return "[Temperature Sensor]: Reading 24.5°C"
        
class PHSensor(Get_reading):
    
    def get_data(self):
        return "[PH Sensor]: Reading: 7.2 (Neutral)"
        
sensor1 = TempSensor()
sensor2 = PHSensor()
print("--- Lab Inventory System ---")
print(sensor2.get_data())
print(sensor1.get_data())
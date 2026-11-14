from abc import ABC, abstractmethod 

class Sensor(ABC):

    @abstractmethod

    def get_data(self):

        pass

class TempSensor(Sensor):

    pass

my_sensor = TempSensor() 
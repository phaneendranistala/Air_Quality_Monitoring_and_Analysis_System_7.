import random

class SensorData:
    def __init__(self, manual=False):
        if manual:
            self.temperature = float(input("Enter Temperature (°C): "))
            self.humidity = float(input("Enter Humidity (%): "))
            self.pm25 = float(input("Enter PM2.5 value: "))
            self.pm10 = float(input("Enter PM10 value: "))
        else:
            self.temperature = random.randint(20, 40)
            self.humidity = random.randint(30, 80)
            self.pm25 = random.randint(10, 200)
            self.pm10 = random.randint(20, 300)

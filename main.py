import datetime
from sensor import SensorData
from aqi_calculator import AQICalculator
from analyzer import DataAnalyzer
from alert_system import AlertSystem
from data_logger import DataLogger

def main():
    print("------ AQMAS SYSTEM ------")
    choice = input("1.Manual  2.Auto: ")

    if choice == "1":
        sensor = SensorData(manual=True)
    else:
        sensor = SensorData()

    aqi = AQICalculator().calculate_aqi(sensor.pm25, sensor.pm10)
    status = DataAnalyzer().analyze(aqi)
    alert = AlertSystem().check_alert(status)

    data = [datetime.datetime.now(), sensor.pm25, sensor.pm10, aqi, status]
    DataLogger().save(data)

    print("AQI:", aqi)
    print("Status:", status)
    print("Alert:", alert)

if __name__ == "__main__":
    main()

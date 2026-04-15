import random
import datetime
import csv

# ---------------- SENSOR MODULE ----------------
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


# ---------------- AQI CALCULATOR ----------------
class AQICalculator:
    def calculate_aqi(self, pm25, pm10):
        return (0.6 * pm25) + (0.4 * pm10)


# ---------------- DATA ANALYZER ----------------
class DataAnalyzer:
    def analyze(self, aqi):
        if aqi <= 50:
            return "Good"
        elif aqi <= 100:
            return "Moderate"
        elif aqi <= 200:
            return "Poor"
        elif aqi <= 300:
            return "Very Poor"
        else:
            return "Severe"


# ---------------- ALERT SYSTEM ----------------
class AlertSystem:
    def check_alert(self, status):
        if status == "Poor":
            return "Caution: Pollution Increasing"
        elif status == "Very Poor":
            return "Warning: High Pollution!"
        elif status == "Severe":
            return "Danger: Stay Indoors!"
        else:
            return "Air Quality Normal"


# ---------------- DATA LOGGER ----------------
class DataLogger:
    def save(self, data):
        with open("aqi_data.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)


# ---------------- MAIN FUNCTION ----------------
def main():
    print("------ AQMAS SYSTEM ------")
    print("1. Manual Input")
    print("2. Automatic (Random Data)")

    choice = input("Choose mode (1/2): ")

    if choice == "1":
        sensor = SensorData(manual=True)
    else:
        sensor = SensorData()

    aqi_calc = AQICalculator()
    analyzer = DataAnalyzer()
    alert = AlertSystem()
    logger = DataLogger()

    # Calculate AQI
    aqi = aqi_calc.calculate_aqi(sensor.pm25, sensor.pm10)

    # Analyze AQI
    status = analyzer.analyze(aqi)

    # Alert check
    warning = alert.check_alert(status)

    # Save data
    data = [
        datetime.datetime.now(),
        sensor.temperature,
        sensor.humidity,
        sensor.pm25,
        sensor.pm10,
        aqi,
        status
    ]

    logger.save(data)

    # Output
    print("\n------ RESULT ------")
    print("Temperature:", sensor.temperature)
    print("Humidity:", sensor.humidity)
    print("PM2.5:", sensor.pm25)
    print("PM10:", sensor.pm10)
    print("AQI:", aqi)
    print("Status:", status)
    print("Alert:", warning)


# ---------------- RUN ----------------
if __name__ == "__main__":
    main()
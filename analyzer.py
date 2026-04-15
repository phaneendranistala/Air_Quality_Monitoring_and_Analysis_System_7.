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
class AQICalculator:
    def calculate_aqi(self, pm25, pm10):
        return (0.6 * pm25) + (0.4 * pm10)

class AQICalculator:
    def calculate_aqi(self, pm25, pm10):
        return (0.6 * pm25) + (0.4 * pm10)

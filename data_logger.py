import csv

class DataLogger:
    def save(self, data):
        with open("aqi_data.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

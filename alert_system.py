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

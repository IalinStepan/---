class TemperatureSensor:
    def __init__(self, sensor_id, type, min_temp, max_temp, accuracy):
        self.sensor_id = sensor_id
        self.type = type
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.accuracy = accuracy
    def info(self):
        print(f"Датчик {self.sensor_id} ({type}): диапазон {self.min}..{self.max} °C, точность ±{self.accuracy} °C")
TemperatureSensor1 = TemperatureSensor("1", )






    
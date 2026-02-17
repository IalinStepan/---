class TemperatureSensor:
    def __init__(self, sensor_id, type, min_temp, max_temp, accuracy):
        self.sensor_id = sensor_id
        self.type = type
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.accuracy = accuracy
    def info(self):
        print(f"Датчик {self.sensor_id} ({self.type}): диапазон {self.min_temp}..{self.max_temp} °C, точность ±{self.accuracy} °C")
TemperatureSensor1 = TemperatureSensor("1", 1, 150, 350, 7)
TemperatureSensor2 = TemperatureSensor("2", 2, 250, 450, 6)
TemperatureSensor3 = TemperatureSensor("3", 3, 350, 550, 5)
TemperatureSensor1.info()
TemperatureSensor2.info()
TemperatureSensor3.info()





    
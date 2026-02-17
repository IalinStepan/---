class TemperatureSensor:
    def __init__(self, sensor_id, type, min_temp, max_temp, accuracy):
        self.__sensor_id = sensor_id
        self.__type = type
        self.__min_temp = min_temp
        self.__max_temp = max_temp
        self.__accuracy = accuracy

    @property
    def sensor_id(self):
        return self.__sensor_id
    
    @property
    def type(self):
        return self.__type
    
    @property
    def min_temp(self):
        return self.__min_temp
    
    @min_temp.setter
    def min_temp(self, value):
        if -273 <= value <= 1000:
            self.__min_temp = value
        else:
            raise ValueError("Неправильная температура")
    
    @property
    def max_temp(self):
        return self.__max_temp
    
    @max_temp.setter
    def max_temp(self, value):
        if  -273 <= value <= 1000:
            if value > self.__min_temp:
                self.__max_temp = value
            else:
                raise ValueError("Максимум должен быть больше минимума")
        else:
            raise ValueError("Неправильная температура")
    
    @property
    def accuracy(self):
        return self.__accuracy
    
    @accuracy.setter
    def accuracy(self, value):
        if 0 < value <= 10:
            self.__accuracy = value
        else:
            raise ValueError()
    @property
    def temp_fahrenheit(self):
        return ((self.max_temp + self.min_temp)/2 * 9 / 5) + 32
    
    def info(self):
        print(f"Датчик {self.__sensor_id} (тип {self.__type}): диапазон {self.__min_temp}..{self.__max_temp} °C, точность ±{self.__accuracy} °C")


sensor1 = TemperatureSensor("1", 1, -50, 150, 0.5)
sensor2 = TemperatureSensor("2", 2, 0, 350, 1)
sensor3 = TemperatureSensor("3", 3, 20, 550, 2.5)
sensor1.info()
sensor2.info()
sensor3.info()
try:
    sensor1.min_temp = 2000
except ValueError as e:
    print(f"min_temp: {e}")
print(f"Фаренгейты: {sensor1.temp_fahrenheit} °F")
    

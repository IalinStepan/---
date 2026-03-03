class TemperatureSensor:
    def __init__(self, sensor_id, type, min_temp, max_temp, accuracy):
        self.__sensor_id = sensor_id
        self.__type = type
        self.__min_temp = min_temp
        self.__max_temp = max_temp
        self.__accuracy = accuracy
    def info(self):
        return f"Датчик {self.__sensor_id} ({self.__type}): диапазон {self.__min_temp}..{self.__max_temp} °C"
    def __str__(self):
        return f"Датчик {self.__sensor_id} ({self.__type}): диапазон {self.__min_temp}..{self.__max_temp} °C"
    
    def __repr__(self):
        return f"TemperatureSensor('{self.__sensor_id}', {self.__type}, {self.__min_temp}, {self.__max_temp}, {self.__accuracy})"

    def __eq__(self, other):
        if type(other) == TemperatureSensor:
            return self.__sensor_id == other.__sensor_id
        else:
            False

    def __lt__(self, other):
        if type(other) == TemperatureSensor:
           return self.__max_temp < other.__max_temp
        
    def __add__(self, other):
        if type(other) == TemperatureSensor:
            return [self, other]
        else:
            return False

TemperatureSensor1 = TemperatureSensor("1", 1, 150, 350, 7)
TemperatureSensor2 = TemperatureSensor("2", 2, 250, 450, 6)
TemperatureSensor3 = TemperatureSensor("3", 3, 350, 550, 5)

print(TemperatureSensor1.info)
print(TemperatureSensor2.info)
print(TemperatureSensor3.info)


print(TemperatureSensor1)

print(TemperatureSensor1.__repr__)

print(TemperatureSensor1 == TemperatureSensor2)

print(TemperatureSensor1<TemperatureSensor2)

print(TemperatureSensor1.info)

print(TemperatureSensor1 + TemperatureSensor2)

TemperatureSensor4 = eval(repr(TemperatureSensor1))
print(TemperatureSensor4)


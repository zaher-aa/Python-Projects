from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"I am a {self.__name}"

    @abstractmethod
    def get_desctiption(self):
        pass


class Car(Vehicle):
    def __init__(self, color, model):
        super().__init__("Car", color)
        self.__model = model

    def get_desctiption(self):
        return f"{self.get_name()} {self.__model} color is {self.get_color()}"


class Van(Vehicle):
    def __init__(self, color, model, hight):
        super().__init__("Van", color)
        self.__hight = hight
        self.__model = model

    def get_desctiption(self):
        return f"{self.get_name()} {self.__model} is {self.get_color()} and {self.__hight} meters hight"


class Plane(Vehicle):
    def __init__(self, color, model, hight, hours_fliet):
        super().__init__("Plane", color)
        self.__model = model
        self.__hight = hight
        self.__hours_fliet = hours_fliet

    def get_desctiption(self):
        return f"{self.get_name()} {self.__model} is {self.get_color()} and {self.__hight} meters hight and fly {self.__hours_fliet} hours"


bmw = Car("black", "X6")
van = Van("blue", "R3500", 2.3)
plane = Plane("white", "bowing 990", 15, 447)
print(bmw.get_desctiption())
print(van.get_desctiption())
print(plane.get_desctiption())

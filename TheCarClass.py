class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed = self.__speed + 5
    def brake(self):
        self.__speed = self.__speed - 5
    def get_speed(self):
        return self.__speed
    def year_model(self):
        return self.__year_model
    def make(self):
        return self.__make
    
car = Car(2003, "Run faster")

print("\n\033[1;34;40mYOUR CAR IS ACCELERATING")
for x in range(5):
    car.accelerate()
    print("Your car's current speed is:", car.get_speed())

print("\n\033[1;35;40m YOUR CAR IS ON BRAKE")
for y in range(5):
    car.brake()
    print("Your car's current speed is:", car.get_speed())
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, on = False, speed = SLOW, radius = 5.0, color = 'blue', ):
        self.__on = on
        self.__speed = speed
        self.__radius = radius
        self.__color = color


    def get_on(self):
        return self.__on

    def set_on(self, on):
        self.__on = on

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

#class test fan
    #def test fan
    #print output

#instance


class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, on = False, speed = SLOW, radius = 5.0, color = 'blue'):
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

class TestFan:

    def run_test(self):

        testFan1 = Fan(on = True, speed = Fan.FAST, radius = 10.0, color = 'yellow')
        testFan2 = Fan(on = False, speed = Fan.MEDIUM, radius = 5.0, color = 'blue')

        print("\033[1;37;40mFan 1")
        print("\033[1;37;40mSpeed:", testFan1.get_speed())
        print("\033[1;37;40mRadius:", testFan1.get_radius())
        print("\033[1;33;40mColor:", testFan1.get_color())
        print("\033[1;37;40mOn:", testFan1.get_on())

        print("\n\033[1;37;40mFan 2")
        print("\033[1;37;40mSpeed:", testFan2.get_speed())
        print("\033[1;37;40mRadius:", testFan2.get_radius())
        print("\033[1;34;40mColor:", testFan2.get_color())
        print("\033[1;37;40mOn:", testFan2.get_on())



test = TestFan()
test.run_test()
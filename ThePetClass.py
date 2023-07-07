class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_age(self, age):
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
pet = Pet()

name = str(input("\033[1;37;40mInput your pet's name: "))
animal_type = str(input("\033[1;37;40mWhat is your pet's animal type: "))
age = int(input("\033[1;37;40mEnter your pet's age: "))


pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)


print("\n\033[1;33;40mYour pet's name is", pet.get_name())
print("\n\033[1;34;40mIt's animal type is a", pet.get_animal_type())
print("\n\033[1;35;40mIt's age is", pet.get_age())

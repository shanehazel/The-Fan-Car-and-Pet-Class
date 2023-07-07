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

name = str(input("Input your pet's name: "))
animal_type = str(input("What is your pet's animal type: "))
age = int(input("Enter your pet's age: "))


pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)


print("Your pet's name is", pet.get_name())
print("It's animal type is a", pet.get_animal_type())
print("It's age is", pet.get_age())

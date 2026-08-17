class Animal:
    def __init__(self,name):
        self.name = name 

    def info(self):
        print("Animal Name is ", self.name)

    def sound(self):
        print("Animal makes a sound!")

    def greet(self):
        print("Animal Greets you! ")



class Dog(Animal):
    def __init__(self, name,age,breed):
        super().__init__(name)
        self.age = age
        self.breed = breed

    def info(self):
        print(f"Hi, My name is {self.name} and I am a {self.breed}")

    def sound(self):
        print(f"{self.name} barks")

    def greet(self):
        print(f'{self.name} starts wagging tail and smiles!')


class Cat(Animal):
    def __init__(self, name,age,breed):
        super().__init__(name)
        self.age = age
        self.breed = breed

    def details(self):
        print(f"This is {self.name} , a {self.breed}")

    def sound(self):
        print(f'{self.name} mews')

    def greet(self):
        print(f'You greet {self.name} !! And you are ignored!! ')


class Cow(Animal):
    def __init__(self, name,age,breed, _color):
        super().__init__(name)
        self.name = name
        self.age = age
        self.breed = breed
        self._color = _color

    def set_color(self,new_col):
        self._color = new_col
        print(f'The updated color of our cow is {self._color}')


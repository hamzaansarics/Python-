def show(a,c):
       if type(a) is int and type(c) is int:
           return a+c
       raise TypeError("You Can't Add other integer values together!")
print(show('khan','Ansari'))

class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError("You Have Define Own Method For You Subclass")
class Dog(Animal):
    def __init__(self,name,voice):
        super().__init__(name)
        self.voice=voice
    def sound(self):
        return  "Bhoaw Bhaow Bhaow Bhawo"
class Cat(Dog):
    def __init__(self,name,voice,address):
        super().__init__(name,voice)
        self.address=address
    def sound(self):
        return "Meao Meoa Meao Meao"
obj=Dog('Kulfi','TON TON')
print(obj.sound())
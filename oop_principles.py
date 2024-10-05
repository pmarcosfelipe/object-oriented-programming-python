#Inheritance and Polymorphism

class Animal:
  def __init__(self, name) -> None:
    self.name = name
  
  def walk(self):
    print(f"The animal {self.name} walked...")
    return
  
  def roar(self):
    pass


class Dog(Animal):
  def roar(self):
    return "au, au..."
  
class Cat(Animal):
  def roar(self):
    return "meow, meow..."
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
  

dog = Dog(name = "Max")
cat = Cat(name = "Juliana")

print(f"\nExamples Polymorphism")
animals = [dog, cat]

for animal in animals:
  print(f"{animal.name} roar {animal.roar()}")


# Encapsulation
print(f"\nExamples Encapsulation")
class BankAccount():
  def __init__(self, balance) -> None:
    self.__balance = balance # private attribute

  def deposit(self, value):
    if value > 0:
      self.__balance += value

  def withdraw(self, value):
    if value > 0 and value <= self.__balance:
      self.__balance -= value

  def get_balance(self):
    return self.__balance
  
account = BankAccount(balance = 1000)
print(f"\nAccount Balance: {account.get_balance()}")
account.deposit(value=100)
print(f"\nAccount Balance after deposit: {account.get_balance()}")
account.withdraw(value=500)
print(f"\nAccount Balance after withdraw: {account.get_balance()}")


print(f"\nAbstraction Example")
from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def turn_on(self):
    pass

  @abstractmethod
  def turn_off(self):
    pass

class Car(Vehicle):
  def __init__(self) -> None:
    pass

  def turn_on(self):
    return "Car turned on..."

  def turn_off(self):
    return "Car turned off..."


car = Car()

print(f"{car.turn_on()}")
print(f"{car.turn_off()}")

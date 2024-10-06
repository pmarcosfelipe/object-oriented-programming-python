# classmethod
# staticmethod

class MyClass:
  value = 10 # Class attribute

  def __init__(self, name) -> None:
    self.name = name

  # Requires an class instance to be called
  def instance_method(self):
    return f"Instance method called for {self.name}"
  
  @classmethod
  def class_method(cls):
    return f"Class method called for value: {cls.value}"

  @staticmethod
  def static_method():
    return "Called Static Method"  
  

object = MyClass(name = "Example Class")

print(f"{object.instance_method()}")
print(f"Class value: {MyClass.value}")
print(f"Class Method: {MyClass.class_method()}")
print(f"Class Static Method: {MyClass.static_method()}")


# Class Method Example
class Car:
  def __init__(self, brand, model, year) -> None:
    self.brand = brand
    self.model = model
    self.year = year

  @classmethod
  def create_car(cls, configuration):
    brand, model, year = configuration.split(",")
    return cls(brand, model, int(year))


toyota_configuration = "Toyota,Corolla,2022"

toyota = Car.create_car(toyota_configuration)

print(f"\nBrand: {toyota.brand}")
print(f"Model: {toyota.model}")
print(f"Year: {toyota.year}")


# 
# Static Method Example
# Static methods can be acessed without create class instance 
#

class Math:
  @staticmethod
  def sum(a, b):
    return a + b

print(f"\nStatic Method Sum: {Math.sum(2,2)}")
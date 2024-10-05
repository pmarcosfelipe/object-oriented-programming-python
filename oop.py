# Object Oriented Programming

# Class
class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def greetings(self):
    return f"Hello, my name is {self.name} and I am {self.age} years old!"

# Object
person = Person("Marcos", 32)
message = person.greetings()

print(message)
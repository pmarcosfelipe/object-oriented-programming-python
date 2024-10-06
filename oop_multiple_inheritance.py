# Multiple Inheritance

class Animal:
  def __init__(self, name) -> None:
    self.name = name

  def emit_sound(self):
    pass

class Mammal(Animal):
  def breastfeed(self):
    return f"{self.name} is breastfeeding..."
  

class Bird(Animal):
  def fly(self):
    return f"{self.name} is flying..."
  

class Bat(Mammal, Bird):
  def emit_sound(self):
    return f"Bats emit sounds ultrasonic..."
  
bat = Bat("batman")

# Call methods from class Animal
print(f"Bat name: {bat.name}")
print(f"Bat sound: {bat.emit_sound()}")


# Call methods from class Mammal
print(f"Bat: {bat.breastfeed()}")

# Call methods from class Bird
print(f"Bat: {bat.fly()}")
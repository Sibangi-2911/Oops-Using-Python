# Single Inheritance
class Car:
  color = "Black"
  @staticmethod
  def start():
    print("Car started...")
  @staticmethod
  def stop():
    print("Car Stopped.")

class ToyotaCar(Car):
  def __init__(self, name):
    self.name = name

Car1 = ToyotaCar("Fortuner")
Car2 = ToyotaCar("prius")
print(Car1.name)
print(Car1.start())
print(Car2.stop())
print(Car1.color)
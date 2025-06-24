#MultiLevel inheritance
class Car:
  @staticmethod
  def start():
    print("Car started")
  @staticmethod
  def stop():
    print("Car Stopped")

class ToyotaCar(Car):
  def __init__(self, brand):
    self.brand = brand

class Fortuner(ToyotaCar):
  def __init__(self, type):
    self.type = type            

Car1 = Fortuner("diesel")
print(Car1.start())
#COMPLEX NUMBER EXAMPLE FOR OPERATOR OVERLOADING
class Complex:
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary
  def showNumber(self):
    print(self.real,"i + ",self.imaginary,"j")
  #dunder function to add two complex numbers
  def __add__(self,num2):
    newReal = self.real+num2.real
    newImagi = self.imaginary+num2.imaginary
    return Complex(newReal,newImagi)
  def __sub__(self,num2):
    newReal = self.real-num2.real
    newImagi = self.imaginary-num2.imaginary
    return Complex(newReal,newImagi)
num1 = Complex(4,3)
num1.showNumber()
num2 = Complex(3,4)
num2.showNumber()
num3 = num1+num2
num3.showNumber()
num4 = num1-num2
num4.showNumber()

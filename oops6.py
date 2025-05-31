# static method
class Student:
  @staticmethod
  def collegename():
    print("IGIT SARANG")
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks
  def average(self):
    sum = 0
    for val in self.marks:
      sum+=val
    print("Hi!!",self.name,". Your average score is ",sum/3)

s1 = Student("Sibangi", [99,100,99])
print(s1.collegename())
s1.average()
s1.name = "Seetal"
s1.average()
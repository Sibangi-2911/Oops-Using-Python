# Use of Methods
class Student:
  college_name = "IGIT SARANG"
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    print("add a new student")

  #method
  def greeting(self):
    print("Welcome ", self.name)
  def get_marks(self):
    return self.marks  

s1 = Student("Sibangi",97)
print(s1.name)
s1.greeting()
print("marks: ", s1.get_marks())
s2 = Student("Seetal",97)
print(s2.name)
s2.greeting()
print("marks: ", s2.get_marks())
s3 = Student("Resma",97)
print(s3.name)
s3.greeting()
print("marks: ", s3.get_marks())


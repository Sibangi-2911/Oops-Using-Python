# using the --init-- function
class Student:
  #default constructors
  def __init__(self):
    pass
  
  #Parameterised constructor
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    print("Added a new student to the database ")

s1 = Student("Sibangi",97)
s2 = Student("Seetal",97)
s3 = Student("Resma",97)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s3.name,s3.marks)
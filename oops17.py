#use of class method to change the class attributes
class Person:
  name = "anonymous"
  age = 50
  @classmethod
  def changeNameAge(cls,name,age):
    cls.name = name
    cls.age = age

p1 = Person()
p1.changeNameAge("Sibangi",22)
print(Person.name)
print(Person.age)
print(p1.name)
print(p1.age)
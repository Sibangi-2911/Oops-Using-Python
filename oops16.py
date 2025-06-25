#one way apart from class method for changing class attributes
class Person:
  name="anonymous"
  age =40
  def changeNameAge(self,name,age):
    Person.name=name
    self.__class__.age=age

p1 = Person()
p1.changeNameAge("Sibangi",22)
print(p1.age)
print(p1.name)
print(Person.age)
print(Person.name)

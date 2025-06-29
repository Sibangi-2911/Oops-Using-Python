class Employee:
  def __init__(self, role, department, salary):
    self.role = role
    self.department = department
    self.salary = salary

  def showDetails(self):
    print("Role = ",self.role)
    print("Department = ",self.department)
    print("Salary = ",self.salary)

class Engineer(Employee):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    super().__init__("Engineer","IT","1,50,000")

e1 = Employee("Manager","TECHNICAL HEAD","1,00,000")
e1.showDetails()
eng1 = Engineer("Rahul",23)
eng1.showDetails()
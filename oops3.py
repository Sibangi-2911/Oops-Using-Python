class Student:
  college_name = "IGIT SARANG" #THIS IS A CLASS ATTRIBUTE THAT IS ITS VALUE IS SAME FOR ALL OBJECTS
  def __init__(self,name,marks):
    self.name = name #THIS IS INSTANCE ATTRIBUTE THAT IS DIFFERENT  FOR EACH OBJECT
    self.marks = marks #THIS IS INSTANCE ATTRIBUTE THAT IS DIFFERENT  FOR EACH OBJECT
    print("added a new student to database")

s1 = Student("Sibangi",97)
s2 = Student("Seetal",97)
s3 = Student("Resma",97)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s3.name,s3.marks)

print(Student.college_name)
print(s1.college_name)
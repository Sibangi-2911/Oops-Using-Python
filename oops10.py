#private attribute  implementation
class Account:
  def __init__(self,acc_no,acc_pass):
    self.acc_no = acc_no
    self.__acc_pass = acc_pass

  def reset_pass(self):
    print(self.__acc_pass)

a1 = Account("12345","23456")
print(a1.acc_no)
print(a1.reset_pass())
print(a1.__acc_pass)

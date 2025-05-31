#Example
class Account:
  def __init__(self, bal, accno):
    self.balance = bal
    self.accountno = accno
  def debit(self, amount):
    self.balance -= amount
    print(f"Rs.{amount} has been debited from your account.")
    print("Total balance: ",self.get_balance())
  def credit(self, amount):
    self.balance +=amount
    print(f"Rs.{amount} has been credited to your account.")
    print("Total balance: ",self.get_balance())
  def get_balance(self):
    return self.balance
acc1 = Account(10000,2345)
acc1.debit(200)
acc1.credit(200)
print(acc1.balance)
print(acc1.accountno)
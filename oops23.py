class Order:
  def __init__(self,item,price):
    self.item = item
    self.price = price
  def __gt__(self,ord2):
    return self.price>ord2.price

ord1 = Order("Chips",30)
ord2 = Order("Tea",10)

print(ord2>ord1)
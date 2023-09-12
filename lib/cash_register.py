#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total=0
    self.items=[]
    self.previous_transaction = []
   
  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    
    ran= range(quantity)
    for i in ran:
      self.items.append(title)
    self.previous_transaction.append(
      {"item": title, "price": price, "quantity": quantity}
    )

  def apply_discount(self):
    if (self.discount > 0) :
       self.total= int(self.total- ((self.discount/100) * self.total))
       print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
        last_transaction = self.previous_transaction.pop()
        self.total = self.total - (last_transaction["price"] * last_transaction["quantity"])

#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.transactions = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(title)
    self.transactions.append({"item": title, "quantity": quantity, "price": price})    
  
  def apply_discount(self):
    if not self.discount:
      print("There is no discount to apply.")
    else:
      self.total *= (1 - (self.discount /100))
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    if not self.transactions:
      print("There are no transactions to void.")
    else:
      #find the total cost of the last transaction and subtract from total
      self.total -= self.transactions[-1]["quantity"] * self.transactions[-1]["price"]
      self.transactions.pop()
      #update the items array
      for _ in range(self.transactions[-1]["quantity"]):
          self.items.pop()
      


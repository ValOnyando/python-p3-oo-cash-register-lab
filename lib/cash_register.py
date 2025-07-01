#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
      self.total = 0
      self.discount = discount
      self.items = []
      self.transactions = []

    def add_item(self, title, price, quantity=1):
      self.total += price * quantity
      self.items.extend([title] * quantity)
      self.transactions.append({'title': title, 'price': price, 'quantity': quantity})

    def apply_discount(self):
      if self.discount > 0:
        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount
        message = f"After the discount, the total comes to ${int(self.total)}."
        print(message)
        return message
      else:
        message = "There is no discount to apply."
        print(message)
        return message

    def get_items(self):
      return self.items

    def void_last_transaction(self):
      if self.transactions:
        last = self.transactions.pop()
        self.total -= last['price'] * last['quantity']
        for _ in range(last['quantity']):
          if last['title'] in self.items:
            self.items.remove(last['title'])



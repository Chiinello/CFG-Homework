# ######Task one ########
# Write a class to represent a Cash Register.
# You class should keep the state of price total and purchased items
# Below is a starter code:
# ------------------------
# 1. you can add new variables and function if you want to
# 2. you will NEED to add accepted method parameters where required.
# For example, method add_item probably accepts some kind of an item?..
# 3. You will need to write some examples of how your code works.
import random


class CashRegister:

    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_and_price):
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, amount):
        self.discount += amount

    def get_total(self):
        discount_total = sum(self.total_items.values())
        total = discount_total - self.discount
        return total

    def show_items(self):
        for item, price in self.total_items.items():
            print(f"{item}:  £{price:.2f}")

    def reset_register(self):
        self.total_items = {}
        self.discount = 0


# On Till 1, a customer wants to purchase 2 milks, 1 cereal and 1 bread
till_1 = CashRegister()

till_1.add_item({'Banana': 0.75})
till_1.add_item({'Milk': 1.45})
till_1.add_item({'Cereal': 3.50})
till_1.add_item({'Bread': 1.00})

# Now customer wants to remove 1 milk
till_1.remove_item('Bread')

# Customer has a £2 voucher
till_1.apply_discount(2.00)

# To show the customer their total items and its price
till_1.get_total()

# To show the customer their receipt
till_1.show_items()

# To reset the till
till_1.reset_register()

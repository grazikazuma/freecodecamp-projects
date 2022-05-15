# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
#from unittest import main

#creating food category
food = budget.Category("Food")
#food initial deposit
food.deposit(1000, "initial deposit")
# withdraw for groceries
food.withdraw(10.15, "groceries")
# withdraw restaurant 
food.withdraw(15.89, "restaurant and more food for dessert")
# print balance
print("Balance ", food.get_balance())
#create Clothing category
clothing = budget.Category("Clothing")
# tranfer 50 to clothing category
food.transfer(50, clothing)
# withdraw for clothing
clothing.withdraw(25.55)
clothing.withdraw(100)
# create category auto
auto = budget.Category("Auto")
# deposit 1000 in auto
auto.deposit(1000, "initial deposit")
# withdraw 15 fro auto
auto.withdraw(15)
# print(food)
# print(clothing)
# print(auto)
print(create_spend_chart([food, clothing, auto]))

#Run unit tests automatically
#main(module='test_module', exit=False)
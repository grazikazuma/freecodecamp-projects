import math
from itertools import zip_longest

class Category:

  #create object (completo)
  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.withdraws = 0
    self.ledger = list()

  #object description
  def __str__(self):
    #title 
    title = self.name.center(30, '*')

    # itens
    list_items = ""
    for items in self.ledger:
      list_values = list(items.values())
      d =  str(list_values[1])[:23].ljust(23)
      a = str("%2.2f" % float(list_values[0])).rjust(7)
      line = d + a + "\n"
      list_items += line
      
    #total
    total = "Total: " + str("%2.2f" % float(self.balance))
   
    return title +'\n'+ list_items + total

  #1 deposit (completo)
  def deposit(self, amount, description = ""):
    self.check_funds(amount)
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount
    
# #2 withdraw (completo)
  def withdraw(self, amount, description = ""):
    withdraw_amount =  amount
    self.check_funds(amount)
    if self.balance > amount:
      self.balance -= amount
      self.withdraws +=  withdraw_amount
      self.ledger.append({"amount": -(amount), "description": description})
      
      
      return True
    else:
      return False

  #3 transfer
  def transfer(self, amount, category):
    if self.balance < amount:
      return False
    if self.balance >= amount:
      self.balance -= amount
      self.withdraws += amount
      self.ledger.append({"amount": -amount, "description": "Transfer to " + category.name})
      category.balance += amount
      category.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
      return True
  
  #4-get balance 
  def get_balance(self):
    return self.balance
    
    
  #5 check funds
  def check_funds(self,amount):
    if amount > self.balance:
      return False
    if amount <= self.balance:
      return True
  
##### create chart 
      
def create_spend_chart(c_list):
  chart = "Percentage spent by category\n" # print final
  total_w = 0 #total withdraw
  l_names = []
  l_name_len = [] # list of 
  l_perc = []

  print("\n")
#print name and value
  
  for category in c_list:
    print(category.name, math.ceil(category.withdraws * 100) /100)
    l_names.append(category.name)
    

#total of withdraw
    total_w += math.ceil(category.withdraws)
  print('total_w =',total_w)

#calculate percentage
  for category in c_list:
    y = math.ceil((category.withdraws * 100) /total_w)
    l_perc.append(y)
    l_name_len.append(len(category.name))
  
  max_name_len = max(l_name_len)
    
# add first part of the chart 
  for x in reversed(range(0,101,10)):
    chart += str(x).rjust(3)+"| "
    for num in l_perc:
      if num >= x:
        chart += "o  "
      if num < x:
        chart += "   "
    chart += "\n"
  chart += "    -".ljust((5 + len(l_perc)* 3 ),'-') + "\n"
    
#add second part of the chart

#calculate max_len of categories names
 

  for x in range(max_name_len):
    chart += "     "
    for name in l_names:
      if x >= len(name):
        chart += "   "
      else:
        chart += name[x] + "  "

    if(x != max_name_len -1):      
      chart += "\n"
      
  return chart
  

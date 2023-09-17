# Budgeting App First Attempt

import os

class Budget:
    def __init__(self,name):
        self.name=name
        self.balance=0

def deposit(self,amount):
    self.balance+=amount
    return(f"You have deposited ${amount}. \
Your new balance is ${self.balance} in {self.name}'s budget.")

def withdraw(self,amount):
    if self.balance<amount:
        print("*****Transaction Failed*****\nInsufficient Funds")
    else:
        self.balance-=amount
        return(f"*****Successful Transaction*****\nYour new \
balance is ${self.balance} in {self.name}'s budget.")
        


test=Budget("November")

testdep=deposit(test,500)
print(testdep)
# print(test.name)
# print(test.balance)

testwith=withdraw(test,500)
print(testwith)
# print(test.name)
# print(test.balance)
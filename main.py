#here are the tasks of the LHA
'''
start a bank account.
add funds. when funds are added the date is recorded. import datetime
user input for expense
while loop bank balance.  if the balance is below zero, then

simple bank account
add fund
add expense
track balance and print balance
import datetime
'''

from datetime import datetime, date, timedelta

""" Here is the overage date table where dates are pulled 
 Can you find a way to set a date only on the 1st and 15th?
 """
today = datetime.today()
_today = today.strftime("%m/%d/%y")
today_15 = datetime.today() + timedelta(days=15)
overage_today_15 = today_15.strftime("%m/%d/%y")
today_30 = datetime.today() + timedelta(days=30)
overage_today_30 = today_30.strftime("%m/%d/%y")
today_45 = datetime.today() + timedelta(days=45)
overage_today_45 = today_45.strftime("%m/%d/%y")
today_60 = datetime.today() + timedelta(days=60)
overage_today_60 = today_60.strftime("%m/%d/%y")


"""Here is a correct way"""

# class BankAccount:
#
#     """Initialize OOP"""
#     def __init__ (self, date):
#         self.date = date
#
#     """Create a function to check the user's bank balance"""
#     def check_balance(self, balance):
#         self.balance = balance
#         if greeting == "check balance":
#             print(f"Today is {date} and your bank balance is {balance}")
#
# class Transaction:



"""Here is the basic transactions of a bank account"""
greeting = ""
balance = 0
overage_table = 0
bank = 0
credit = (bank * 3)
credit_balance = balance - overage_table




while greeting != "q":
    greeting = input(("""
Welcome to the bank. Here is are the transactions you can make:
- check balance - add funds - remove funds - q
    """))

    if greeting == "check balance":
        print(f'Your bank balance is {bank} on {_today}')

    if greeting == "add funds":
        add_funds_request = int(input("how much would you like to add?"))
        bank += add_funds_request
        print(f'You added {add_funds_request} to your bank account on {_today}')

    if greeting == "remove funds":
        remove_funds = int(input("how much would you like to remove?"))
        bank -= remove_funds
        print(f'YOU withdrew {remove_funds} and your balance is {bank} on {_today}')

    while bank < 0:
        overage_table += bank
        bank = 0
        balance = bank + overage_table
        print("your bank is at", bank)
        print("your balance with the bank and overage is", balance)
        if overage_table < 0:
            overage_split = overage_table / 4
            print (f"today is ", _today,".  You will be charged ", overage_split,"four times over the next 60 days")
            print(f'''
- #1 ${overage_split} will be pulled from your bank on {overage_today_15}
- #2 ${overage_split} will be pulled from your bank on {overage_today_30}
- #3 ${overage_split} will be pulled from your bank on {overage_today_45}
- #4 ${overage_split} will be pulled from your bank on {overage_today_60}
                     ''')

"""
Q: Can you store and print the recent transactions?
Q: Can you show the balance for a future date after 1 or 2 payments?
 
"""
# here the sum of the overage table is


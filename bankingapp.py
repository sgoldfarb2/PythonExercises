#using our UML diagram, create a banking app

#since we can't see our UML diagram, here are the notes we are using to create our banking app
#our banking app needs a members section which stores all of our members -- DONE
#our members need a first name and last name and account number and unique ID -- DONE
#our base class will be called account and we will have savings accounts and checking accounts and money market accounts that inherit from our accounts class -- DONE
#all of our accounts need a balance, need a withdrawal method, a deposit method - DONE
#checking and saving account have an interest rate, a monthly fee - DONE
#need a global class variable that keeps track of how much money the entire bank has (reserve balance)
#our member class will have methods (add checking, add savings, or add money market account) - DONE
#our member class needs an account list to hold whatever accounts we create using our add accounts methods - DONE
#need a bank class that holds our members - DONE
#bank will also have a name, a location of it's own
#our members will have an account number key and an object that contains all of their member  information, so they are easy to look up by their key (their account number) - DONE
#bank class needs an add member method, a find member by account number method, a find member by name method, and a delete member method - DONE
#reserve balances needed for savings, for checking, and for our money market accounts separately
#our bank is starting with a reserve balance of $100,000 - DONE

import random

#our bank has a name, an address, and a dictionary containing all of the members inside by account number as the key and their member object as its value


class Bank:
  def __init__(self, bank_name, bank_address):
    self.bank_name = bank_name
    self.bank_address = bank_address
    self.member_dictionary = {}

#we are adding new members by creating members with our Member class and putting them in our member dictionary object
  def add_new_member(self, member_first_name, member_last_name, member_account_number):
    temp = Member(member_first_name, member_last_name, member_account_number)
    self.member_dictionary[member_account_number] = {temp}

#getting our
  def find_member_by_account_number(self, member_account_number):
    print(self.member_dictionary[member_account_number])

#still need to do this
  def find_member_by_name(self, member_first_name):
    pass

  def delete_member(self, member_account_number):
    del self.member_dictionary[member_account_number]



#here is our Member class, which creates an account number for each member, stores their first and last names, and stores which accounts each member has
class Member:
  def __init__(self, member_first_name, member_last_name, member_account_number):
    self.member_first_name = member_first_name
    self.member_last_name = member_last_name
    self.member_account_number = member_account_number #later will change this to random
    self.member_accounts = []

  def add_checking_account(self):
    temp = Checking(account_balance)
    self.member_accounts.append(temp)
    print(member_accounts)

  def add_savings_account(self):
    temp = Savings(account_balance)
    self.member_accounts.append(temp)

  def add_money_market_account(self):
    temp = MoneyMarket(account_balance)
    self.member_accounts.append(temp)



class Account:
  def __init__(self, account_balance, member_account_number):
    self.reserve_balance = 100000
    self.account_balance = account_balance

  def withdraw_money(self, amount_to_withdraw):
    self.account_balance = self.account_balance - amount_to_withdraw

  def deposit_money(self, amount_to_deposit):
    self.account_balance = self.account_balance + amount_to_deposit

class MoneyMarket(Account):
  def __init__(self, account_balance):
    self.interest = .05
    self.monthly_fees = 20
    self.account_name = 'Money Market Account'
    self.account_balance = account_balance

class Checking(Account):
  def __init__(self, account_balance):
    self.interest = .01
    self.monthly_fees = 5
    self.account_name = 'Checking Account'
    self.account_balance = account_balance

class Savings(Account):
  def __init__(self, account_balance):
    self.interest = .02
    self.monthly_fees = 10
    self.account_name = 'Savings Account'
    self.account_balance = account_balance


our_bank = Bank('Bank of DigitalCrafts', '123 Happy Coder Road')
our_bank.add_new_member('Sabrina', 'Goldfarb', 1)
our_bank.add_new_member('Michael', 'Goldfarb', 2)
our_bank.add_new_member('Steven', 'Goldfarb', 3)
our_bank.add_new_member('Barbara', 'Goldfarb', 4)

#questions!
#how would I add a new checking/savings/money market account to my people?
#how would I access the withdrawal and deposit for someone?

# Class Methods

from math import sqrt

class Clown:
	nose = 'big and red'
	bag = 'Black and Yellow'
	def dance():
		return 'No Thanks'
	def summation(x):
		return sqrt(x)

class Account:
	def __init__(self, account_holder):
		self.holder = account_holder
		self.balance = 0
	def deposit(self, amount):
		self.balance += amount
		return self.balance
	def withdraw (self, amount):
		if self.balance > amount:
			self.balance-= amount
			return self.balance
		else:
			print('Insufficient balance')
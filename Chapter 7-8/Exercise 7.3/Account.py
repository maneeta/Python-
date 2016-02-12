import math

class Account:
    # Construct a account object 
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__Id = id

    def getBalance(self):
        return self.__balance
    
    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def getMonthlyInterestRate(self):
        monthyInterestRate = self.__annualInterestRate/12
        return monthyInterestRate

    def getMonthlyInterest(self):
        monthlyInterest = self.__balance *getMonthlyInterestRate()
        return monthlyInterest

    def withdraw(self,amount):
        if amount <= self.__balance:
           self.__balance -= amount 

    def deposit(self,amount):
        self.__balance += amount

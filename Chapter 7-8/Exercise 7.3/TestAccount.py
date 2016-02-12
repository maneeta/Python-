from Account import Account

def main():
    accountA = Account(1122,20000,4.5)
    print("ID is", accountA.getId())
    accountA.balance = 20000
    #accountA.annualInterestRate = 0.045
    print("Initial Balance is ", accountA.getBalance())
    accountA.withdraw(2500)
    accountA.deposit(3000)
    
    print("Balance is", accountA.getBalance())
    print("Monthly Interest rate is", accountA.getMonthlyInterestRate())
    print("Monthly Interest is", (accountA.getBalance() * accountA.getMonthlyInterestRate()/100))
    
  
main() # Call the main function

from Account import Account

def main():
    accountList = []
    i = eval(input("Enter an account id : "))
    
    for i in range (10):
        accountList.append(Account(id=i))
            
    print("\nMain menu")
    print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
   
    choice = eval(input("Enter a choice: "))
    accountA = Account(i)
    if choice == 1:
        print("The balance is", accountA.getBalance())
        print("\nMain menu")
        print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
        choice = eval(input("Enter a choice: "))
        if choice == 2:
            withdrawAmount = eval(input("Enter an amount to withdraw: "))
            print("\nMain menu")
            print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
            choice = eval(input("Enter a choice: "))
            if choice == 1:
                print(" The balance is", (accountA.getBalance() - withdrawAmount))
                print("\nMain menu")
                print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
                choice = eval(input("Enter a choice: "))
            
                if choice == 3:
                    depositAmount = eval(input("Enter an amount to deposit: "))    
                    print("\nMain menu")
                    print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
                    choice = eval(input("Enter a choice: "))
            
                    if choice == 1:
                        print(" The balance is", (accountA.getBalance() - withdrawAmount+ depositAmount))
                        print("\nMain menu")
                        print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
                        choice = eval(input("Enter a choice: "))
        
                        if choice == 4:
                            print(eval(input("Enter an account id : ")))
                            print("\nMain menu")
                            print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
                            choice = eval(input("Enter a choice: "))
        
            
    elif choice == 3:
        amount = eval(input("Enter an amount to deposit: "))
        print("\nMain menu")
        print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
        choice = eval(input("Enter a choice: "))
        if choice == 1:
            print("balance is", (accountA.getBalance() + amount ))
            print("\nMain menu")
            print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
            choice = eval(input("Enter a choice: "))
    elif choice == 4:
        print(eval(input("Enter an account id : ")))
        print("\nMain menu")
        print("1: check balance\n2: withdraw\n3: deposit\n4: exit")
        choice = eval(input("Enter a choice: "))
    
 
main() # Call the main function

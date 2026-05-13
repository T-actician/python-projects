#================TERMINAL BAKNK SYSTEM REDONE======================

balance = 1000
transactions = []
running = True
user_pin = 1234
trials = 3
    
menu ={
    "1.": "Deposit",
    "2.": "Withdraw",
    "3.": "Check Balance",
    "4.": "Transaction History",
    "5.": "Exit"    
}

print("============TACTICIANS BANK=========")

while trials > 0:
    try:
        pin = int(input("⚡Enter your PIN to transact: "))
        if pin == user_pin:
            while running:
                for key, value in menu.items():
                    print(f"{key} {value}")
                    
                choice = input(("⚡Pick a service: "))
                    
                if choice == "1":
                    try:
                        amount = float(input("⚡Enter the amount to deposit: "))
                        if amount == 0:
                            print("Amount cannot be 0!")
                        elif amount < 0:
                            print("You cannot deposit a negative figure!")
                        else:
                            balance += amount
                            print(f"{amount} deposited successfully. Your new bank balance is {balance}")
                            transactions.append(f"Deposited: {amount}")
                    except ValueError:
                        print("Invalid Ammount! Only numbers accepted.")

                elif choice == "2":
                    try:
                        amount = float(input("⚡Enter the amount to withdraw: "))
                        if amount == 0:
                            print("Amount cannot be 0!")
                        elif amount < 0:
                            print("You cannot withdraw a negative figure!")
                        elif amount > balance:
                            print(f"Failed to withdraw {amount}. Your Bank account balance is {balance}")          
                        else:
                            balance -= amount
                            print(f"{amount} deposited successfully. Your new bank balance is {balance}")
                            transactions.append(f"Withdrew: {amount}")
                            
                    except ValueError:
                        print("Invalid Ammount! Only numbers accepted.")
                        
                elif choice == "3":
                    print(f"Your account Balance is {balance}")
                    
                elif choice == "4":
                    print("==========================")
                    for transaction in transactions:
                        print(transaction)
                    print("==========================")
                    
                elif choice == "5":
                    print("=======THANK YOU FOR TRANSACTING WITH US!=============")
                    running = False
                    trials = 0
                    
                    
                else:
                    print("Invalid Choice!")
        else:
            trials -= 1            
            if trials > 0:
                print(f"Incorrect PIN. Trials remaining {trials}")
            else:
                print("Too many PIN attempts. Access denied!")
                trials = 0
        
    except ValueError:
        print("INVALID!")    
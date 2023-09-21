from account import Account
class customer:
    def __init__(self, name, id, age, cardnumber, pin, atm_instance, account_instance,savings_balance,cuatroxmil):
        self.name = name
        self.id = id
        self.age = age
        self.cardnumber = cardnumber
        self.pin = pin
        self.atm_instance = atm_instance
        self.account_instance = account_instance
        self.savings_balance = savings_balance
        self.cuatroxmil = cuatroxmil
        self.account = account_instance

    def insertcard(self):
        print("Reading card...")
        print("Welcome {}!".format(self.name))
        entered_pin = input("Please enter your PIN:  ")
        if entered_pin == self.pin:
            while True:
                print("\nOptions:")
                print("1. Transfer")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Change your PIN")
                print("5. Save money")
                print("6. Check balance")
                print("7. Exit")
                option = input("Please enter your option (1/2/3/4/5/6):  ")
                
                if option == "1":
                    if self.cuatroxmil.lower() == "yes":
                        amount = int(input("Please enter the amount to transfer:  "))
                        transfer_fee = (amount*4)/1000
                        amount = amount + transfer_fee
                        self.atm_instance.transfer(amount, self.account_instance)
                        
                    elif self.cuatroxmil.lower() == "no":
                        amount = int(input("Please enter the amount to transfer:  "))
                        self.atm_instance.transfer(amount, self.account_instance)
                    
                    else:
                        print("ERROR: Unknown")
                        
                elif option == "2":
                    amount = int(input("Please enter the amount to deposit:  "))
                    self.account_instance.deposit(amount)
                elif option == "3":
                        amount = int(input("Please enter the amount to withdraw:  "))
                        self.account_instance.withdraw(amount)
                
                elif option == "4":
                    self.changepin()
                
                elif option == "5":
                    self.savemoney()
                
                elif option == "6":
                    print('Your account balance is {}.'.format(self.account_instance.balance))
                
                elif option == "7":
                    print("Exiting the system. Thank you for using our services!")
                    break
                else:
                    print("Invalid option")
        else:
            print("Invalid PIN")
    
    def savemoney(self):
        amount = int(input("Please enter the amount to save:  "))
        if amount > 0 and amount < self.account_instance.balance:
                self.savings_balance += amount
                self.account_instance.balance -= self.savings_balance
                print("You have saved ${}, your savings account balance is now ${}.".format(amount, self.savings_balance))
        else:
            print("Insufficient funds or the value is negative")
    
    def changepin(self):
        entered_pin = input('Please enter your current PIN: ')
        if entered_pin == self.pin:
            while True:
                new_pin = input('Please enter your new PIN: ')
                new_pin2 = input("Please enter your new PIN again:  ")
                if new_pin == new_pin2:
                    self.pin = new_pin
                    print("You have changed your PIN successfully")
                    break
                else:
                    print("Pin doesn't match")
        else:
            raise TypeError("Your pin is incorrect")
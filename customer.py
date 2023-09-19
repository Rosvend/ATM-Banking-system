class customer:
    def __init__(self, name, id, age, cardnumber, pin, atm_instance, account_instance,savings_balance):
        self.name = name
        self.id = id
        self.age = age
        self.cardnumber = cardnumber
        self.pin = pin
        self.atm_instance = atm_instance
        self.account_instance = account_instance
        self.savings_balance = savings_balance

    def insertcard(self):
        print("Reading card...")
        entered_pin = input("Please enter your PIN:  ")
        if entered_pin == self.pin:
            while True:
                print("\nOptions:")
                print("1. Transfer")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")
                option = input("Please enter your option (1/2/3/4):  ")
                
                if option == "1":
                    amount = int(input("Please enter the amount to transfer:  "))
                    self.atm_instance.transfer(amount, self.account_instance)
                elif option == "2":
                    amount = int(input("Please enter the amount to deposit:  "))
                    self.account_instance.deposit(amount)
                elif option == "3":
                    amount = int(input("Please enter the amount to withdraw:  "))
                    self.account_instance.withdraw(amount)
                elif option == "4":
                    print("Exiting the system. Thank you for using our services!")
                    break
                else:
                    print("Invalid option")
        else:
            print("Invalid PIN")
    
    def savemoney(self,amount):
        amount = int(input("Please enter the amount to save:  "))
        self.savings_balance += amount
        print("You have saved ${}, your savings account balance is now ${}.".format(amount, self.savings_balance))

    
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
from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def bank_name(self):
        pass

    @abstractmethod
    def transfer(self,amount):
        pass

class Account(Bank):
    def __init__(self, owner, balance,account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
        
    def bank_name(self):
        return self.bank_name
    
    def transfer(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
            return self.balance
        else:
            self.balance -= amount
            print("Transferred correctly, your new balance is ${}".format(self.balance))
            return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        print("You have deposited ${}, your new balance is ${}".format(amount,self.balance))
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        print("You have withdrawn ${}, your new balance is ${}".format(amount,self.balance))
        return self.balance

account1 = Account("Luis",10000,"001")
        
class ATM(Bank):
    def __init__(self, location, bank_name,balance):
        self.location = location
        self.bank_name = bank_name
        self.balance = balance
    
    def bank_name(self):
        return self.bank_name
    
    def transfer(self, amount,account):
        if amount > account.balance:
            print("Insufficient funds")
        else:
            account.balance -= amount
            print("Transferred correctly, your new balance is ${}".format(account.balance))
    
    def deposit(self, amount,account):
        account.balance += amount
        print("Deposited money correctly, your new balance is ${}".format(account.balance))
    
    def withdraw(self, amount,account):
        if amount > account.balance:
            print("Insufficient funds")
        else:
            account.balance -= amount
            print("You have withdrawn money correctly, your new balance is ${}".format(account.balance))
        

ATM1 = ATM("Laureles","Bancolombia", 12000)
account1.transfer(100)
account1.deposit(100)

class customer():
    def __init__(self, name, id, age,cardnumber,pin):
        self.name = name
        self.id = id
        self.age = age
        self.cardnumber = cardnumber
        self.pin = pin
    

    def insertcard(self):
        print("Reading card...")
        userpin = input("Please enter your pin:  ")
        if  userpin == self.pin:
            option = input("Please enter your option (Transfer/Deposit/Withdraw/Check balance):  ")
            if option == "Transfer":
                amount = int(input("Please enter amount to transfer:  "))
                ATM1.transfer(amount,account1)
            elif option == "Deposit":
                amount = int(input("Please enter amount to deposit:  "))
                ATM1.deposit(amount,account1)
            elif option == "Withdraw":
                amount = int(input("Please enter amount to withdraw: "))
                ATM1.withdraw(amount,account1)
            elif option == "Check":
                print("Your balance is ${}".format(account1.balance))
            else:
                raise ValueError("Invalid option")

            
        else:
            raise ValueError("Invalid card number")
    
    def savemoney(self, amount,account):
        amount = int(input("Please enter the amount to save:  "))
        ATM1.transfer(amount,account)
        print("Saved money correctly, your savings account balance is ${}".format(account.balance))

    
customer1 = customer("Daniel",100,23,"001","1234")
customer1.insertcard()


class savings_account(Account):
    def __init__(self, savings_account_name, balance):
        self.savings_account_name = savings_account_name
        self.balance = balance
    
    def earn_interest(self, account):
        interest = 0.10
        account.balance = (interest*account.balance) + account.balance
        print("Your balance is now ${} with a earned interest of 10%".format(savings_account1.balance))


savings_account1 = savings_account("Mortgage savings account",100000)
savings_account1.earn_interest(account1)
customer1.savemoney(5000,savings_account1)
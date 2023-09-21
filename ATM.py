from  Bank import Bank
class ATM(Bank):
    def __init__(self, location, bank_name, account_instance):
        self.location = location
        self.bank_name = bank_name
        self.account_instance = account_instance
    
    def bank_name(self):
        return self.bank_name
    
    def transfer(self, amount, account_instance):
        if amount > self.account_instance.balance:
            print("Insufficient funds")
        else:
            self.account_instance.balance -= amount  
            print("Transferred correctly, your new balance is ${}".format(self.account_instance.balance))
    
    def deposit(self, amount):
        self.account_instance.balance += amount  
        print("Deposited money correctly, your new balance is ${}".format(self.account_instance.balance))
    
    def withdraw(self, amount):
        if amount > self.account_instance.balance:
            print("Insufficient funds")
        else:
            self.account_instance.balance -= amount  
            print("You have withdrawn money correctly, your new balance is ${}".format(self.account_instance.balance))
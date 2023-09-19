from  Bank import Bank
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
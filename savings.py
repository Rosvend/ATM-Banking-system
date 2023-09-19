from account import Account
class savings_account(Account):
    def __init__(self, savings_account_name,balance):
        self.savings_account_name = savings_account_name
        self.balance = balance
    
    def earn_interest(self, account):
        interest = 0.10
        account.balance = (interest*account.balance) + account.balance
        print("Your balance is now ${} with a earned interest of 10%".format(account.balance))
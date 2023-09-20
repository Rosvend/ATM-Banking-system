from Bank import Bank #Importamos la interfaz ya que esta clase hereda de la interfaz
class Account(Bank):
    def __init__(self, owner, balance, account_number):  #Creamos el metodo constructor con 3 argumentos que vamos a utilizar
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
        self.bank_name = "" 
    
    def bank_name(self):
        return super().bank_name()
    
    
    def transfer(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Transferred correctly, your new balance is ${}".format(self.balance))
    
    def deposit(self, amount):
        self.balance += amount
        print("You have deposited ${}, your new balance is ${}".format(amount, self.balance))
    
    def withdraw(self, amount):
        self.balance -= amount
        print("You have withdrawn ${}, your new balance is ${}".format(amount, self.balance))
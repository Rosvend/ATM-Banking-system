#Importamos todas las clases al arhivo 'Main'
from account import Account
from ATM import ATM
from customer import customer
from savings import savings_account

#Creamos objetos a partir de todas las clases dándoles atributos respectivamente e instanciamos en algunos casos
account1 = Account("Luis", 10000, "001")
ATM1 = ATM("Laureles", "Bancolombia",12000)
customer1 = customer("Daniel", 100, 23, "1", "1234",ATM1,account1,0)
savings_account1 = savings_account("Mortgage savings account",100000)

#Aplicamos los métodos a cualquiera de los objetos
account1.transfer(100)
account1.deposit(100)
customer1.insertcard()
customer1.changepin()
savings_account1.earn_interest(account1)
customer1.savemoney(5000,savings_account1)
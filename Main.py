#Importamos todas las clases al arhivo 'Main'
from account import Account
from ATM import ATM
from customer import customer
from savings import savings_account

#Creamos objetos a partir de todas las clases dándoles atributos respectivamente e instanciamos en algunos casos
customer1_account = Account("Daniel", 50000, "001")
customer2_account = Account("Sofia", 100000, "002")
ATM1 = ATM("Laureles", "Bancolombia",customer1_account)
ATM2 = ATM("San Juan", "Davivienda",customer2_account)
customer1 = customer("Daniel", "100", 26, "001", "1234",ATM1,customer1_account,0,"yes")
customer2 = customer("Sofia", "99", 18, "002", "4321", ATM2,customer2_account, 0, "no")
savings_account1 = savings_account("Mortgage savings account",0)

#Aplicamos los métodos a cualquiera de los objetos
customer1.insertcard()
savings_account1.earn_interest(customer1_account)
customer2.insertcard()
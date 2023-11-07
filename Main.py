#Importamos todas las clases al arhivo 'Main'
from account import Account
from ATM import ATM
from customer import customer
from savings import savings_account
import tkinter as tk
import sqlite3


conn = sqlite3.connect('bank.db')
c = conn.cursor()


c.execute('''
    CREATE TABLE customers (
        name TEXT,
        id TEXT,
        age INTEGER,
        cardnumber TEXT,
        pin TEXT,
        atm_location TEXT,
        account_balance REAL,
        savings_balance REAL,
        cuatroxmil TEXT
    )
''')

c.execute("INSERT INTO customers VALUES ('Daniel', '100', 26, '001', '1234', 'Laureles', 50000, 0, 'yes')")
c.execute("INSERT INTO customers VALUES ('Sofia', '99', 18, '002', '4321', 'San Juan', 100000, 0, 'no')")
c.execute("INSERT INTO customers VALUES ('Juan', '98', 30, '003', '0000', 'Laureles', 50000, 0, 'yes')")

# Commit the changes
conn.commit()

# Close the connection
conn.close()


#Creamos objetos a partir de todas las clases dándoles atributos respectivamente e instanciamos en algunos casos
customer1_account = Account("Daniel", 50000, "001")
customer2_account = Account("Sofia", 100000, "002")
ATM1 = ATM("Laureles", "Bancolombia",customer1_account)
ATM2 = ATM("San Juan", "Davivienda",customer2_account) 
customer1 = customer("Daniel", "100", 26, "001", "1234",ATM1,customer1_account,0,"yes")
customer2 = customer("Sofia", "99", 18, "002", "4321", ATM2,customer2_account, 0, "no")
customer3 = customer("Juan", "98", 30, "003", "0000", ATM1, customer1_account, 0, "yes")
savings_account1 = savings_account("Mortgage savings account",0)

#Aplicamos los métodos a cualquiera de los objetos
def main():
    customer1.starting_ATM()
main()

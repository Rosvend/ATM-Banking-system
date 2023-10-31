import tkinter as tk
from account import Account
from ATM import ATM
from customer import customer
from savings import savings_account

customer1_account = Account("Daniel", 50000, "001")
customer2_account = Account("Sofia", 100000, "002")
ATM1 = ATM("Laureles", "Bancolombia",customer1_account)
ATM2 = ATM("San Juan", "Davivienda",customer2_account)
customer1 = customer("Daniel", "100", 26, "001", "1234",ATM1,customer1_account,0,"yes")
customer2 = customer("Sofia", "99", 18, "002", "4321", ATM2,customer2_account, 0, "no")
savings_account1 = savings_account("Mortgage savings account",0)


root = tk.Tk()
root.title("ATM Banking System")

root.geometry("400x300+600+200")

label1 = tk.Label(root, text="Welcome to the ATM")
label2 = tk.Label(root, text="Reading your card...")

label1.pack()

button1 = tk.Button(root, text='Insert card', padx=20,pady=10,command=customer1.insertcard)
button1.pack()
label2.pack()
root.mainloop()

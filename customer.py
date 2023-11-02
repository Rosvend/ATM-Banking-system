from account import Account
from ATM import ATM
import tkinter as tk

root = tk.Tk()

class customer:
    
            def __init__(self, name, id, age, cardnumber, pin, atm_instance, account_instance, savings_balance, cuatroxmil):
                self.name = name
                self.id = id
                self.age = age
                self.cardnumber = cardnumber
                self.pin = pin
                self.atm_instance = atm_instance
                self.account_instance = account_instance
                self.savings_balance = savings_balance
                self.cuatroxmil = cuatroxmil
                self.account = account_instance
                

            def insertcard(self):
                def option1():
                    if self.cuatroxmil.lower() == "yes":
                        entry = tk.Entry(root, text='Please enter the amount to transfer: ')
                        entry.pack()
                        amount = float(entry.get())
                        transfer_fee = (amount*4)/1000
                        amount += transfer_fee
                        self.atm_instance.transfer(amount, self.account_instance)
                    elif self.cuatroxmil.lower() == "no":
                        entry = tk.Entry(root, text='Please enter the amount to transfer: ')
                        entry.pack()
                        amount = float(entry.get())
                        self.atm_instance.transfer(amount, self.account_instance)
                    else:
                        error_label = tk.Label(root, text="ERROR: Unknown")
                        error_label.pack()

                def option2():
                    entry = tk.Entry(root, text='Please enter the amount to deposit: ')
                    entry.pack()
                    amount = float(entry.get())
                    self.account_instance.deposit(amount)
                    success_label = tk.Label(root, text="Deposit successful")
                    success_label.pack()

                def option3():
                    entry = tk.Entry(root, text='Please enter the amount to withdraw: ')
                    entry.pack()
                    amount = float(entry.get())
                    if amount > self.account_instance.balance:
                        error_label = tk.Label(root, text="Insufficient funds")
                        error_label.pack()
                    else:
                        self.account_instance.withdraw(amount)
                        success_label = tk.Label(root, text="Withdrawal successful")
                        success_label.pack()

                def option4():
                    self.changepin()

                def option5():
                    entry = tk.Entry(root, text='Please enter the amount to save: ')
                    entry.pack()
                    save_button = tk.Button(root, text="Save", command=lambda: self.savemoney(entry.get()))
                    save_button.pack()

                def option6():
                    balance_label = tk.Label(root, text="Your account balance is {}.".format(self.account_instance.balance))
                    balance_label.pack()

                def option7():
                    exit_label = tk.Label(root, text="Exiting the system. Thank you for using our services!")
                    exit_label.pack()
                    root.quit()

                name_label = tk.Label(root, text=f'Welcome {self.name} to the ATM, please enter your PIN to continue')
                name_label.pack()
                pin_var = tk.StringVar()
                entry = tk.Entry(root, textvariable=pin_var)
                entry.pack()
                
                def submit():
                    entered_pin = entry.get()
                    global invalid_label_frame
                    try:
                         invalid_label_frame.destroy()
                    except NameError:
                         pass
                    if entered_pin == self.pin:
                            def show_options():
                                options_label = tk.Label(root, text="\nPlease select an option:",font=('arial', 10, 'bold'))
                                options_label.pack()

                                button_frame = tk.Frame(root)
                                button_frame.pack()

                                transfer_button = tk.Button(button_frame, text="Transfer",command=option1)
                                deposit_button = tk.Button(button_frame, text="Deposit",command=option2)
                                withdraw_button = tk.Button(button_frame, text="Withdraw",command=option3)
                                change_pin_button = tk.Button(button_frame, text="Change your PIN",command=option4)
                                save_money_button = tk.Button(button_frame, text="Save money",command=option5)
                                check_balance_button = tk.Button(button_frame, text="Check balance",command=option6)
                                exit_button = tk.Button(button_frame, text="Exit",command=option7)
                                

                                transfer_button.grid(row=0, column=0, padx=15, pady=10)
                                deposit_button.grid(row=1, column=0, padx=5, pady=10)
                                withdraw_button.grid(row=2, column=0)
                                change_pin_button.grid(row=0, column=1)
                                save_money_button.grid(row=1, column=1)
                                check_balance_button.grid(row=2, column=1)
                                exit_button.grid(row=3, column=0, columnspan=2,pady=20)

                            show_options()
                            submit_button.config(state='disabled')
    
                    else:
                        invalid_label_frame = tk.Frame(root)
                        invalid_label_frame.pack()
                        invalid_label = tk.Label(invalid_label_frame,text="Invalid PIN")
                        invalid_label.pack()
                
                submit_button = tk.Button(root, text="Submit",command=submit)
                submit_button.pack()

            def savemoney(self):
                entry = tk.Entry(root, text='Please enter the amount to save: ')
                entry.pack()
                amount = float(entry.get())
                if amount <= 0:
                    error_label = tk.Label(root, text="Invalid amount")
                    error_label.pack()
                elif amount > self.account_instance.balance:
                    error_label = tk.Label(root, text="Insufficient funds")
                    error_label.pack()
                else:
                    self.savings_balance += amount
                    self.account_instance.balance -= amount
                    save_label = tk.Label(root, text="You have saved ${}, your savings account balance is now ${}.".format(amount, self.savings_balance))
                    save_label.pack()

            def changepin(self):
                pin_var = tk.StringVar()
                entry = tk.Entry(root, textvariable=pin_var)
                entry.pack()
                entered_pin = entry.get()
                if entered_pin == self.pin:
                    while True:
                        new_pin_var = tk.StringVar()
                        new_pin_entry = tk.Entry(root, textvariable=new_pin_var)
                        new_pin_entry.pack()
                        new_pin = new_pin_var.get()
                        new_pin2_var = tk.StringVar()
                        new_pin2_entry = tk.Entry(root, textvariable=new_pin2_var)
                        new_pin2_entry.pack()
                        new_pin2 = new_pin2_var.get()
                        if new_pin == new_pin2:
                            self.pin = new_pin
                            success_label = tk.Label(root, text="PIN changed successfully")
                            success_label.pack()
                            break
                        else:
                            error_label = tk.Label(root, text="PINs don't match")
                            error_label.pack()
                else:
                    error_label = tk.Label(root, text="Invalid PIN")
                    error_label.pack()

            def starting_ATM(self):
                    
                    root.title("ATM Banking System")
                    root.geometry("600x600+500+100")

                    label1 = tk.Label(root, text="Welcome to the ATM, please enter your card to continue", font=('arial', 10, 'bold'), bg='yellow')
                    label2 = tk.Label(root, text="Reading your card...",state='normal')

                    def show_label2():
                        label2.pack()

                    def start_process():
                        show_label2()
                        self.insertcard()

                    label1.pack()

                    button1 = tk.Button(root, text='Insert card', padx=20,pady=10,command=start_process)
                    button1.pack()
                    root.mainloop()


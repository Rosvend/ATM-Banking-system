from account import Account
from ATM import ATM
import tkinter as tk
from tkinter import messagebox

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
            

            def view_transactions(self):
                for transaction in self.account_instance.transactions:
                    transaction_label = tk.Label(root,text='Transaction type: {}, amount: ${}'.format(transaction[1], transaction[0]),bg='light blue', font=('arial', 10, 'bold'))
                    transaction_label.pack()
            
        

            def insertcard(self):
                def transfer():
                        
                        if self.cuatroxmil.lower() == 'yes':
                            transfer_label = tk.Label(root, text="You have a 4x1000 fee, please enter the amount to transfer: ", bg='light blue', font=('arial', 10, 'bold'))
                            transfer_label.pack()
                            self.widgets.append(transfer_label)
                            entry = tk.Entry(root)
                            entry.pack()
                            self.widgets.append(entry)
                        
                        else:
                            transfer_label = tk.Label(root, text="Please enter the amount to transfer: ", bg='light blue', font=('arial', 10, 'bold'))
                            transfer_label.pack()
                            self.widgets.append(transfer_label)
                            entry = tk.Entry(root)
                            entry.pack()
                            self.widgets.append(entry)

                        def confirm_transfer():
                            amount = float(entry.get())
                            if self.cuatroxmil.lower() == "yes":
                                transfer_fee = (amount*4)/1000
                                amount += transfer_fee
                                confirm = messagebox.askyesno("Confirmation", "Are you sure you want to transfer ${}?".format(amount))
                                if confirm:
                                    self.atm_instance.transfer(amount, self.account_instance)
                                    success_label = tk.Label(root,text="You have successfully transferred {}, your new balance is ${}".format(amount,self.account_instance.balance),bg='light blue', font=('arial', 10, 'bold'))
                                    success_label.pack()
                                    self.widgets.append(success_label)
                                else:
                                    cancel_label = tk.Label(root,text="Transfer cancelled.",bg='light blue', font=('arial', 10, 'bold'))
                                    cancel_label.pack()
                                    self.widgets.append(cancel_label)
                            
                            elif self.cuatroxmil.lower() == 'no':
                                confirm = messagebox.askyesno("Confirmation", "Are you sure you want to transfer ${}?".format(amount))
                                if confirm:
                                    self.atm_instance.transfer(amount, self.account_instance)
                                    success_label = tk.Label(root,text="You have successfully transferred {}, your new balance is ${}".format(amount,self.account_instance.balance),bg='light blue', font=('arial', 10, 'bold'))
                                    success_label.pack()
                                    self.widgets.append(success_label)
                                else:
                                    cancel_label = tk.Label(root,text="Transfer cancelled.",bg='light blue', font=('arial', 10, 'bold'))
                                    cancel_label.pack()
                                    self.widgets.append(cancel_label)

                            else:
                                error_label = tk.Label(root, text="ERROR: Unknown")
                                error_label.pack()
                                self.widgets.append(error_label)

                        transfer_button = tk.Button(root, text="Confirm transfer", command=confirm_transfer,font=('arial', 10, 'bold'))
                        transfer_button.pack(pady=10)
                        self.widgets.append(transfer_button)
                    

                def deposit():
                    deposit_label = tk.Label(root, text="Please enter the amount to deposit: ",bg='light blue', font=('arial', 10, 'bold'))
                    deposit_label.pack()
                    self.widgets.append(deposit_label)
                    entry = tk.Entry(root)
                    entry.pack()
                    self.widgets.append(entry)

                    def confirm_deposit():
                        amount = float(entry.get())
                        self.account_instance.deposit(amount)
                        success_label = tk.Label(root, text="You have succesfully deposited ${}, your new balance is ${}".format(amount, self.account_instance.balance),bg='light blue', font=('arial', 10, 'bold'))
                        success_label.pack()
                        self.widgets.append(success_label)

                    deposit_button = tk.Button(root, text="Confirm deposit", command=confirm_deposit,font=('arial', 10, 'bold'))
                    deposit_button.pack(pady=15)
                    self.widgets.append(deposit_button)

                def withdraw():
                    withdraw_label = tk.Label(root, text="Please enter the amount to withdraw: ",bg='light blue', font=('arial', 10, 'bold'))
                    withdraw_label.pack()
                    entry = tk.Entry(root)
                    entry.pack()
                    def confirm_withdraw():
                        amount = float(entry.get())
                        if amount > self.account_instance.balance:
                            error_label = tk.Label(root, text="Insufficient funds")
                            error_label.pack()
                        else:
                            self.account_instance.withdraw(amount)
                            success_label = tk.Label(root, text=f"Withdrawal successful, your new balance is ${self.account_instance.balance}",bg='light blue', font=('arial', 10, 'bold'))
                            success_label.pack()
                    
                    withdraw_button = tk.Button(root, text="Confirm withdrawal", command=confirm_withdraw,font=('arial', 10, 'bold'))
                    withdraw_button.pack(pady=15)

                def change_pin():
                        pin_label = tk.Label(root, text="Please enter your current PIN: ",bg='light blue', font=('arial', 10, 'bold'))
                        pin_label.pack()
                        pin_var = tk.StringVar()
                        entry = tk.Entry(root, textvariable=pin_var)
                        entry.pack()
                        self.widgets.append(entry)

                        def confirm_pin():
                            entered_pin = pin_var.get()
                            if entered_pin == self.pin:
                                new_pin_var = tk.StringVar()
                                new_pin_entry = tk.Entry(root, textvariable=new_pin_var)
                                new_pin_entry.pack()
                                self.widgets.append(new_pin_entry)

                                def confirm_new_pin():
                                    new_pin = new_pin_var.get()
                                    self.pin = new_pin
                                    success_label = tk.Label(root, text="PIN changed successfully",bg='light blue', font=('arial', 10, 'bold'))
                                    success_label.pack()
                                    self.widgets.append(success_label)

                                confirm_button = tk.Button(root, text="Confirm new PIN", command=confirm_new_pin)
                                confirm_button.pack(pady=10)
                                self.widgets.append(confirm_button)
                            else:
                                error_label = tk.Label(root, text="Incorrect PIN",bg='red', font=('arial', 10, 'bold'))
                                error_label.pack(pady=10)
                                self.widgets.append(error_label)

                        confirm_button = tk.Button(root, text="Confirm current PIN", command=confirm_pin)
                        confirm_button.pack(pady=10)
                        self.widgets.append(confirm_button)

                def save_money():
                    save_money_label = tk.Label(root, text="Please enter the amount to save: ",bg='light blue', font=('arial', 10, 'bold'))
                    save_money_label.pack(pady=10)
                    entry = tk.Entry(root)
                    entry.pack()

                    def save_money_button():
                        amount = float(entry.get())
                        if amount <= 0:
                            error_label = tk.Label(root, text="Invalid amount",bg='red', font=('arial', 10, 'bold'))
                            error_label.pack()
                        elif amount > self.account_instance.balance:
                            error_label = tk.Label(root, text="Insufficient funds", bg='red', font=('arial', 10, 'bold'))
                            error_label.pack()
                        else:
                            self.savings_balance += amount
                            self.account_instance.balance -= amount
                            save_label = tk.Label(root, text="You have saved ${}, your savings account balance is now ${}.".format(amount, self.savings_balance),bg='light blue', font=('arial', 10, 'bold'))
                            save_label.pack()
                    
                    save_button = tk.Button(root, text="Save money", command=save_money_button,font=('arial', 10, 'bold'))
                    save_button.pack(pady=10)


                def check_balance():
                    balance_label = tk.Label(root, text="Your account balance is ${}.".format(self.account_instance.balance),bg='light blue')
                    balance_label.pack()

                def exit():
                    exit_label = tk.Label(root, text="Exiting the system. Thank you for using our services!",bg='light blue', font=('arial', 10, 'bold'))
                    exit_label.pack()
                    root.quit()

                name_label = tk.Label(root, text=f'Welcome {self.name} to the ATM, please enter your PIN to continue',bg='light blue', font=('arial', 10,'bold'))
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
                                options_label = tk.Label(root, text="\nPlease select an option:",font=('arial', 10, 'bold'),bg='light blue')
                                options_label.pack()

                                button_frame = tk.Frame(root,bg='light blue')
                                button_frame.pack()

                                transfer_button = tk.Button(button_frame, text="Transfer",command=transfer,width=40)
                                deposit_button = tk.Button(button_frame, text="Deposit",command=deposit,width=40)
                                withdraw_button = tk.Button(button_frame, text="Withdraw",command=withdraw,width=40)
                                change_pin_button = tk.Button(button_frame, text="Change your PIN",command=change_pin,width=40)
                                save_money_button = tk.Button(button_frame, text="Save money",command=save_money,width=40)
                                check_balance_button = tk.Button(button_frame, text="Check balance",command=check_balance,width=40)
                                view_transactions_button = tk.Button(button_frame, text="View transaction history",command=self.view_transactions,width=40)
                                exit_button = tk.Button(button_frame, text="Exit",command=exit,bg='red',font=('arial', 10, 'bold'),width=36)
                                

                                transfer_button.grid(row=0, column=0, padx=15, pady=10)
                                deposit_button.grid(row=1, column=0, padx=5, pady=10)
                                withdraw_button.grid(row=2, column=0)
                                change_pin_button.grid(row=0, column=1)
                                save_money_button.grid(row=1, column=1)
                                check_balance_button.grid(row=2, column=1)
                                view_transactions_button.grid(row=3, column=1, pady=10)
                                exit_button.grid(row=3, column=0,pady=20)

                            show_options()
                            submit_button.config(state='disabled')
    
                    else:
                        invalid_label_frame = tk.Frame(root)
                        invalid_label_frame.pack()
                        invalid_label = tk.Label(invalid_label_frame,text="Incorrect PIN",bg='red',font=('arial', 15, 'bold'))
                        invalid_label.pack()
                
                submit_button = tk.Button(root, text="Submit",command=submit,font=('arial', 10, 'bold'))
                submit_button.pack(pady=10)

                
            def savemoney(self):
                save_label = tk.Label(root, text="Please enter the amount to save: ",bg='light blue', font=('arial', 10, 'bold'))
                save_label.pack()
                entry = tk.Entry(root)
                entry.pack()

                def save_money_button():
                    amount = float(entry.get())
                    if amount <= 0:
                        error_label = tk.Label(root, text="Invalid amount",bg='red', font=('arial', 10, 'bold'))
                        error_label.pack()
                    elif amount > self.account_instance.balance:
                        error_label = tk.Label(root, text="Insufficient funds", bg='red', font=('arial', 10, 'bold'))
                        error_label.pack()
                    else:
                        self.savings_balance += amount
                        self.account_instance.balance -= amount
                        save_label = tk.Label(root, text="You have saved ${}, your savings account balance is now ${}.".format(amount, self.savings_balance),bg='light blue', font=('arial', 10, 'bold'))
                        save_label.pack()
                
                save_money_button = tk.Button(root, text="Save money", command=save_money_button,font=('arial', 10, 'bold'))
                save_money_button.pack(pad=10)


            def starting_ATM(self):
                    
                    root.title("ATM Banking System")
                    root.geometry("800x800+400+20")
                    root.configure(background='light blue')

                    self.widgets = []

                    def clear_widgets():
                        for widget in self.widgets:
                            widget.destroy()
                        self.widgets = []
                    
                    
                    label1 = tk.Label(root, text="Welcome to the ATM, please enter your card to continue", font=('arial', 12, 'bold'),bg='light blue')
                    label2 = tk.Label(root, text="Reading your card...",state='normal',font=('arial',10,'bold'),bg='light blue')

                    def show_label2():
                        label2.pack(pady=5)

                    def start_process():
                        clear_widgets()
                        show_label2()
                        self.insertcard()

                    label1.pack()

                    button1 = tk.Button(root, text='Insert card', padx=5,pady=5,command=start_process,font=('arial', 13, 'bold'))
                    button1.pack(pady=10)
                    self.widgets.append(button1)
                    root.mainloop()


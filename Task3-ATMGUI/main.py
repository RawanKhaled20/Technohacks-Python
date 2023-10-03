"""Author: Rawan Khaled"""

import tkinter as tk

balance = 0

def Deposit():
    global balance
    Deposit_sum = 0
    amount = float(entry_Amount.get())  # Convert the entry value to float
    Deposit_sum += amount
    balance += Deposit_sum
    entry_Amount.delete(0, tk.END)  # Clear the entry field

def Withdraw():
    global balance
    withdraw_sum = 0
    amount = float(entry_Amount.get())  # Convert the entry value to float
    withdraw_sum += amount
    if balance >= withdraw_sum:
        balance -= withdraw_sum
    else:
        result_label.config(text="Insufficient balance")
    entry_Amount.delete(0, tk.END)  # Clear the entry field

def checkbalance():
    result_label.config(text=f"Your current balance is: {balance}")

root = tk.Tk()
root.geometry("500x350")
root.title("ATM")
root.resizable(False, False)
icon_image = tk.PhotoImage(file="ATM.png")
root.iconphoto(False, icon_image)

custom_font = ("Times New Roman", 14, "bold")
custom_font2 = ("Times New Roman", 10, "bold")

label = tk.Label(root, text="This is a Python ATM. What do you want to do:", font=custom_font)
label.pack(pady=10)

entry_Amount = tk.Entry(root, font=custom_font, width=15)
entry_Amount.pack(pady=5)

button_Deposit = tk.Button(root, text="Deposit", command=Deposit, width=10, height=2, bg="Light Gray", font=custom_font2)
button_Deposit.pack(padx=5, pady=5)

button_withdraw = tk.Button(root, bg="Light Gray", command=Withdraw, text="Withdraw", width=10, height=2, font=custom_font2)
button_withdraw.pack(padx=5, pady=5)

result_label = tk.Label(root, text="", font=custom_font)
result_label.pack()

button_balance = tk.Button(root, text="Check Balance", command=checkbalance, font=custom_font2, width=15, height=2,bg="Light Gray")
button_balance.pack(pady=5, padx=5)

quit_button = tk.Button(root, text="Quit", command=root.quit, width=15, height=2, bg="Light Gray", font=custom_font2)
quit_button.pack(pady=5, padx=28)

root.mainloop()

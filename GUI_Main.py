# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:24:44 2023

@author: hp
"""

import tkinter as tk
from tkinter import messagebox


# Replace this function with your own fake currency verification logic
def is_fake_currency(amount):
    # Add your verification logic here, e.g., checking against a predefined list
    fake_currencies = [1000, 500, 50]  # Example fake currency denominations
    return amount in fake_currencies

def check_currency():
    amount = entry_amount.get()
    try:
        amount = int(amount)
        if is_fake_currency(amount):
            messagebox.showwarning("Fake Currency Detected", f"{amount} is fake currency!")
        else:
            messagebox.showinfo("Currency Verification", f"{amount} is genuine currency.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount (numeric value).")

# Create the main application window
app = tk.Tk()
app.title("Fake Currency App")

# Create GUI components
label_amount = tk.Label(app, text="Enter Amount:")
label_amount.pack()

entry_amount = tk.Entry(app)
entry_amount.pack()

btn_check = tk.Button(app, text="Check", command=check_currency)
btn_check.pack()

# Start the application
app.mainloop()
   
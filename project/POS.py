import tkinter as tk
from tkinter import ttk

# Data
prices = {
    "Rice": 2500,
    "Beans": 1500,
    "Oil": 3000,
    "Sugar": 1200,
    "Spaghetti": 800
}

cart = []

# Functions 
def add_to_cart():
    item = item_var.get()
    qty = int(qty_var.get())
    price = prices[item] * qty
    
    cart.append((item, qty, price))
    update_receipt()

def update_receipt():
    receipt_text = "--- RECEIPT ---\n"
    total = 0
    
    for item, qty, cost in cart:
        receipt_text += f"{item} x{qty} = ₦{cost}\n"
        total += cost
    
    receipt_text += "---------------------\n"
    receipt_text += f"TOTAL = ₦{total}"
    
    receipt_label.config(text=receipt_text)

def clear_all():
    cart.clear()
    receipt_label.config(text="--- RECEIPT ---")

# GUI 
window = tk.Tk()
window.title("Grocery Store POS")
window.geometry("1080x1080")

# Dropdown
item_var = tk.StringVar(value="Rice")
item_dropdown = ttk.Combobox(window, textvariable=item_var, values=list(prices.keys()))
item_dropdown.pack(pady=10)

# Quantity
qty_var = tk.StringVar()
qty_entry = ttk.Entry(window, textvariable=qty_var)
qty_entry.pack(pady=10)

# Add Button
add_btn = tk.Button(window, text="Add to Cart", command=add_to_cart)
add_btn.pack(pady=10)

# Receipt
receipt_label = tk.Label(window, text="--- RECEIPT ---", font=("Arial", 12), justify="left")
receipt_label.pack(pady=20)

# Clear Button
clear_btn = tk.Button(window, text="Clear Cart", command=clear_all)
clear_btn.pack(pady=10)

window.mainloop()

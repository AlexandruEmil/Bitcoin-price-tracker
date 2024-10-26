import requests
import tkinter as tk
from tkinter import ttk

def get_crypto_price(crypto_ids=["bitcoin", "ethereum", "cardano"], vs_currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto_ids),
        "vs_currencies": vs_currency
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("An error occurred:", response.status_code)
        return None

def update_prices():
    print("Button clicked!")
    data = get_crypto_price()
    for row in tree.get_children():
        tree.delete(row)

    if data:
        for crypto, details in data.items():
            price = details.get("usd")
            tree.insert("", "end", values=(crypto.capitalize(), f"{price} USD"))

# Main application window
root = tk.Tk()
root.title("Cryptocurrency Price Tracker")
root.geometry("400x350")
root.update()

# Application title
title = tk.Label(root, text="Cryptocurrency Prices", font=("Arial", 16))
title.grid(row=0, column=0, columnspan=2, pady=10)

# Table setup
columns = ("Cryptocurrency", "Price (USD)")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Cryptocurrency", text="Cryptocurrency")
tree.heading("Price (USD)", text="Price (USD)")
tree.grid(row=1, column=0, columnspan=2, pady=20)

# Update button
update_button = tk.Button(root, text="Update Prices", command=update_prices)
update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Initial call to populate the table
update_prices()

root.mainloop()

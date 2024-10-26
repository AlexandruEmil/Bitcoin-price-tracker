import requests
import pandas as pd
from tabulate import tabulate

def get_crypto_price(crypto_ids=["bitcoin", "ethereum", "cardano"], vs_currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto_ids),  # lista criptomonedelor pe care le dorim
        "vs_currencies": vs_currency  # moneda în care vrem prețul (usd, eur, etc.)
    }
    
    # Facem cererea
    response = requests.get(url, params=params)
    
    # Verificăm răspunsul și extragem datele
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("A apărut o eroare:", response.status_code)
        return None

def display_prices(data):
    # Cream o listă de date pentru a le structura frumos
    rows = []
    for crypto, details in data.items():
        price = details.get("usd")
        rows.append([crypto.capitalize(), price])
    
    # Afișăm tabelul
    print(tabulate(rows, headers=["Cryptocurrency", "Price (USD)"], tablefmt="grid"))

def main():
    crypto_data = get_crypto_price()
    if crypto_data:
        display_prices(crypto_data)

if __name__ == "__main__":
    main()

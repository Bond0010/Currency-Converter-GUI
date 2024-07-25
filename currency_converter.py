# currency_converter.py

import requests

API_URL = " https://v6.exchangerate-api.com/v6/d8589982d5e6b5a33619ad88/latest/USD"

def fetch_exchange_rates():
    try:
        response = requests.get(API_URL)
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates']
        else:
            print("Error fetching exchange rates:", data['error-type'])
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching exchange rates:", e)
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency code.")
        return None
    # Convert amount to USD first
    amount_in_usd = amount / rates[from_currency]
    # Convert USD to target currency
    converted_amount = amount_in_usd * rates[to_currency]
    return converted_amount

def list_currencies(rates):
    print("Available currencies:")
    for currency in rates:
        print(currency)

if __name__ == "__main__":
    rates = fetch_exchange_rates()
    if rates:
        print("Exchange rates fetched successfully.")
    else:
        print("Failed to fetch exchange rates.")

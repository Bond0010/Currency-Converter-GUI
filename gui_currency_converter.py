# gui_currency_converter.py

import tkinter as tk
from tkinter import messagebox
from currency_converter import fetch_exchange_rates, convert_currency

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.rates = fetch_exchange_rates()
        if not self.rates:
            messagebox.showerror("Error", "Failed to fetch exchange rates.")
            self.root.quit()

        self.create_widgets()

    def create_widgets(self):
        # Amount Entry
        self.amount_label = tk.Label(self.root, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # From Currency
        self.from_currency_label = tk.Label(self.root, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)
        self.from_currency_var = tk.StringVar(self.root)
        self.from_currency_var.set("USD")
        self.from_currency_menu = tk.OptionMenu(self.root, self.from_currency_var, *self.rates.keys())
        self.from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

        # To Currency
        self.to_currency_label = tk.Label(self.root, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)
        self.to_currency_var = tk.StringVar(self.root)
        self.to_currency_var.set("EUR")
        self.to_currency_menu = tk.OptionMenu(self.root, self.to_currency_var, *self.rates.keys())
        self.to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

        # Convert Button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()
            result = convert_currency(amount, from_currency, to_currency, self.rates)
            if result is not None:
                self.result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
            else:
                self.result_label.config(text="Conversion failed.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

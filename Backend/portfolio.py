import json
import os

class Portfolio:
    def __init__(self, file_path='data/portfolio.json'):
        self.file_path = file_path
        self.portfolio = self.load_portfolio()
        self.stocks = {}  

    def load_portfolio(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {}

    def save_portfolio(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w') as f:
            json.dump(self.portfolio, f, indent=4)

    def add_stock(self, symbol, quantity, purchase_price):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
        else:
            self.portfolio[symbol] = {'quantity': quantity, 'purchase_price': purchase_price}
        self.save_portfolio()

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] -= quantity
            if self.portfolio[symbol]['quantity'] <= 0:
                del self.portfolio[symbol]
        self.save_portfolio()

    def view_portfolio(self):
        return self.portfolio

    def calculate_portfolio_value(self, price_data):
        total_value = 0.0
        for symbol, stock in self.portfolio.items():
            quantity = stock['quantity']
            current_price = price_data.get(symbol)

            # Handle the case where current_price is None
            if current_price is None:
                print(f"Warning: No current price available for {symbol}. Skipping...")
                continue

            print(f"Symbol: {symbol}, Quantity: {quantity}, Current Price: {current_price}")

            try:
                quantity = float(quantity)
                current_price = float(current_price)
            except ValueError:
                print(f"Error: Non-numeric data found for symbol {symbol}.")
                continue

            total_value += quantity * current_price

        return total_value


    def calculate_gains_losses(self, price_data):
        gains_losses = {}
        for symbol, data in self.portfolio.items():
            quantity = data['quantity']
            purchase_price = data['purchase_price']
            current_price = price_data.get(symbol)

            # Handle the case where current_price is None
            if current_price is None:
                print(f"Warning: No current price available for {symbol}. Skipping...")
                continue

            try:
                quantity = float(quantity)
                purchase_price = float(purchase_price)
                current_price = float(current_price)
            except ValueError:
                print(f"Error: Non-numeric data found for symbol {symbol}.")
                continue

            cost_basis = quantity * purchase_price
            current_value = quantity * current_price
            gains_losses[symbol] = current_value - cost_basis

        return gains_losses


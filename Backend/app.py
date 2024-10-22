from flask import Flask, request, jsonify, send_from_directory
from portfolio import Portfolio
from yahoo_finance import YahooFinanceAPI  # Import the new Yahoo Finance API class
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

yahoo_finance = YahooFinanceAPI()
portfolio = Portfolio()

@app.route('/add_stock', methods=['POST'])
def add_stock():
    data = request.json
    symbol = data.get('symbol')
    quantity = data.get('quantity')
    purchase_price = data.get('purchase_price')
    portfolio.add_stock(symbol, quantity, purchase_price)
    return jsonify({'status': 'Stock added successfully'})

@app.route('/view_portfolio', methods=['GET'])
def view_portfolio():
    price_data = {symbol: yahoo_finance.get_stock_price(symbol) for symbol in portfolio.view_portfolio().keys()}
    total_value = portfolio.calculate_portfolio_value(price_data)
    gains_losses = portfolio.calculate_gains_losses(price_data)
    return jsonify({'total_value': total_value, 'gains_losses': gains_losses})

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)

import yfinance as yf

class YahooFinanceAPI:
    def __init__(self):
        pass

    def get_stock_price(self, symbol):
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            return data['Close'].iloc[-1]
        else:
            print(f"Warning: No data found for symbol '{symbol}'.")
            return None

    def get_stock_history(self, symbol, period='5d'):
        stock = yf.Ticker(symbol)
        data = stock.history(period=period)
        return data

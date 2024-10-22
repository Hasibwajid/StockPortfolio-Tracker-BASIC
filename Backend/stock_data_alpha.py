import requests

class AlphaVantageAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_stock_price(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        # Extract the latest price
        try:
            latest_time = list(data['Time Series (5min)'].keys())[0]
            latest_price = data['Time Series (5min)'][latest_time]['1. open']
            return float(latest_price)
        except KeyError:
            return None

    def get_stock_history(self, symbol, interval='5min'):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data

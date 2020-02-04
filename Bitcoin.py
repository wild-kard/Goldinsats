import yfinance as yf

Bitcoin = yf.Ticker("BTC-USD")

history = Bitcoin.history(period="max")

print(history.to_csv())
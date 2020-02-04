import yfinance as yf

Bitcoin = yf.Ticker("GC=F")

history = Bitcoin.history(period="max")

print(history.to_csv())
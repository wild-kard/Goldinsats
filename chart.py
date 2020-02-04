import plotly.graph_objects as go 
import pandas

df = pandas.read_csv('Bitcoin.csv')

candlestick = go.Candlestick(x=df['Date'], open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])

figure = go.Figure(data=[candlestick])

figure.show()
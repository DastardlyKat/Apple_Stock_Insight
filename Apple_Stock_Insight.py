import pandas as pd
import matplotlib.pyplot as plt

stock_data=pd.read_csv("/Users/swaksharbora/Downloads/AAPL.csv")

stock_data['Date']=pd.to_datetime(stock_data['Date'])

stock_data.set_index("Date", inplace=True)

#Percentage Daily Returns
stock_data["Daily Return"]=stock_data['Adj Close'].pct_change()

#Calculating Moving Average
stock_data['20-Day MA']=stock_data['Adj Close'].rolling(window=20).mean()
stock_data['50-Day MA']=stock_data['Adj Close'].rolling(window=50).mean()

#Calculating Volatility
stock_data['Volatility']=stock_data['Daily Return'].rolling(window=20).std()

#Stock Price and Moving Average
plt.figure(figsize=(20, 10))
plt.plot(stock_data['Adj Close'], label='Adjusted Closing Price')
plt.plot(stock_data['20-Day MA'], label='20-Day Moving Average')
plt.plot(stock_data['50-Day MA'], label='30-Day Moving Average')
plt.title('Stock Price and Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

#Daily Returns
plt.figure(figsize=(20, 10))
plt.plot(stock_data['Daily Return'], label='Daily Return')
plt.title('Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.show()

#Stock Price Volaility
plt.figure(figsize=(20,10))
plt.plot(stock_data['Volatility'], label='20-Day Rolling Volatility')
plt.title('Stock Price Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()
import yfinance as yf
import pandas as pd

initInvest = 1000
tckr = input("Input Ticker: ")
stock = yf.Ticker(tckr)
data = stock.history(period="max")
start = data.head(1)
opening = (start.iloc[0])["Open"]
initShares = initInvest/opening
now = data.tail(1)

for i in range(data.shape[0]-2):
    i += 1
    row = data.iloc[i]
    if row["Dividends"] > 0:
        divEarnings = row["Dividends"] * initShares
        initShares += divEarnings / row["Close"]

closing = now["Close"]
initInvest = initShares*closing
initInvest = int(initInvest)
print('$',initInvest)

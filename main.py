import yfinance as yf
import pandas as pd
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# Stock list
stocks = [
    "AAPL",
    "MSFT",
    "TSLA",
    "NVDA",
    "GOOGL",
    "AMZN"
]

# Download stock data
data = yf.download(
    stocks,
    start="2020-01-01",
    end="2025-01-01"
)

# Extract close prices
close_prices = data["Close"]

# Display sample
print("\nStock Price Data:\n")

print(close_prices.head())

# Save dataset
close_prices.to_csv("data/stocks.csv")

print("\nstocks.csv saved successfully")
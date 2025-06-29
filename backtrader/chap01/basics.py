# -*- CODING: UTF-8 -*-

# chapter1_basics.py
# pip install backtrader yfinance pandas matplotlib
# Import necessary libraries

from __future__ import (absolute_import, division, print_function,
unicode_literals)
import backtrader as bt
import datetime
import pandas as pd
import yfinance as yf # Import yfinance

print("Libraries Imported Successfully!")


# DEFINE THE TICKER symbol and date range
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-12-31' # Use a date in the past
print(f"Downloading {ticker} data from {start_date} to {end_date}...")


# Download data using yfinance
try:
    # Use yf.download for simplicity
    dataframe = yf.download(ticker, start=start_date, end=end_date)
    dataframe.columns = dataframe.columns.droplevel(1)
    print(f"Data downloaded successfully. Shape: {dataframe.shape}")
    # Check the first few rows and column names
    print("\nDataFrame Head:")
    print(dataframe.head())
    print("\nDataFrame Info:")
    dataframe.info()
except Exception as e:
    print(f"Error downloading data: {e}")
    # Exit or handle error appropriately
    exit()

# Ensure the DataFrame index is a DatetimeIndex (yf.download usually does this)
if not isinstance(dataframe.index, pd.DatetimeIndex):
    print("Converting index to DatetimeIndex...")

dataframe.index = pd.to_datetime(dataframe.index)
print("\nData is ready in Pandas DataFrame format.")
'''
This is a utility class

from utils.py import get_data, scale_data, normalize_data, standardize_data, zero_shift, daily_returns, daily_change

'''

# !pip install yfinance
import yfinance as yf
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# // Jupter plotting and utils 
'''
# defaults for plt
%matplotlib inline
plt.style.use('fivethirtyeight')                # first, small enchancements, xlabels, ylabels, legand sizing...   
plt.rcParams['lines.linewidth'] = 2             # Change linewidth of plots
plt.rcParams['figure.figsize'] = (12, 8)        # Change the size of plots


# multiple outputs per cells. does not mix well with plt as they return stull that will be printed
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
'''


import datetime

if __name__ == '__main__':
    print('This is a utility class. dont run directly')

def get_data(tickers: list[str] = ['spy', 'qqq', 'xiu.to', 'aapl', 'amzn'],
            start = datetime.datetime(1990,1,1),
            end = datetime.date.today(), 
            use_log_return=False,
            drop_na=False) -> pd.DataFrame:
    """
    This function returns a dataframe with the data of the tickers
    @param tickers: list of tickers
    @param start: start date
    @param end: end date
    @param use_log_return: if True, the log return is used
    @param drop_na: if True, the dataframe is droped if there are NA
    """
    tickers  = list(set(tickers))
    
    for i in range(len(tickers)):
        tickers[i] = tickers[i].upper()

    data = {} 

    for i in tickers:
        arry = yf.download(i, start, end)

        data[i] = arry["Adj Close"]
        if use_log_return:
            data[i] =  pd.Series(np.diff(np.log(data[i])), index=arry.index[1:])

    stocks = pd.DataFrame(data)
    if drop_na:
        print(f'shape of the dataframe: {stocks.shape}')
        stocks.dropna(inplace=True)
        print(f'shape of the dataframe - after droping NA: {stocks.shape}')

    return stocks

def scale_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function scales (normalize) the data
    @param data: dataframe
    """
    print(f'Scaling data... via normalization `(data - data.min()) / (data.max() - data.min())`')
    return normalize_data(data)

def normalize_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function normalizes the data
    @param data: dataframe
    """
    print(f'Normalizing data... `(data - data.min()) / (data.max() - data.min())`')
    return (data - data.min()) / (data.max() - data.min())

def standardize_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function scales the data
    @param data: dataframe
    """
    print(f'Scaling data... `(data - data.mean()) / data.std()`')
    return (data - data.mean()) / data.std()

def zero_shift(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function shifts the data on the y-axis to ensure the first value is 0. Useful because stocks start is very different numbers
    @param data: dataframe
    """
    print(f'Ensure each column starts at 0 `data-data.iloc[0]`')
    return data-data.iloc[0]

def daily_returns(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function returns the daily returns
    @param data: dataframe
    """
    # print(f'Calculating daily RETURN by differencing the data... `(data/data.shift(1)`')
    # data = (data/data.shift(1))
    data = data/data.shift(1)
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data.dropna(inplace=True)
    return data

def daily_change(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function returns the daily change
    @param data: dataframe
    """
    # print(f'Calculating daily CHANGE by differencing the data... `(data.pct_change()`')
    # data = (data/data.shift(1))-1
    data = data.pct_change()
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data.dropna(inplace=True)
    return data
# def log_daily_returns(data: pd.DataFrame) -> pd.DataFrame:
# Notes

> Ugly and poorly formatted notes for quick reference  



## log returns 

`MSFT['log_return'] = np.log(MSFT['Adj Close'] / MSFT['Adj Close'].shift(1))`



## Cumulative returns 

`aapl['Cumulative'] = aapl['Close']/aapl['Close'].iloc[0]` 



## percentage change 

`tesla['returns'] = (tesla['Close'] / tesla['Close'].shift(1) ) - 1` 



## rolling mean

`gm['MA50'] = gm['Open'].rolling(50).mean()`
`gm['MA200'] = gm['Open'].rolling(200).mean()`
`gm[['Open','MA50','MA200']].plot(label='gm',figsize=(16,8))`



## Exp Moving avg 

`airline['EWMA12'] = airline['Thousands of Passengers'].ewm(span=12).mean()`
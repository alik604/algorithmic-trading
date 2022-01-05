# Notes

> Ugly and poorly formatted notes for quick reference  



## log returns 

`MSFT['log_return'] = np.log(MSFT['Adj Close'] / MSFT['Adj Close'].shift(1))`



## Cumulative returns 

`aapl['Cumulative'] = aapl['Close']/aapl['Close'].iloc[0]` 



## percentage change 

`tesla['returns'] = (tesla['Close'] / tesla['Close'].shift(1) ) - 1` 



## rolling mean

```python
gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm['Open'].rolling(200).mean()
gm[['Open','MA50','MA200']].plot(label='gm',figsize=(16,8))
```



## Exp Moving avg 

`airline['EWMA12'] = airline['Thousands of Passengers'].ewm(span=12).mean()`

## Sharpe ratio 
Take the return of the portfolio and subtract the risk free rate. 
devide by the standard deviation of the portfolio’s excess return

## Sortino ratio 
Take the return of the portfolio and subtract the risk free rate. 
devide by the standard deviation of the downside

> Because the Sortino ratio focuses only on the negative deviation of a portfolio's returns from the mean, it is thought to give a better view of a portfolio's risk-adjusted performance since positive volatility is a benefit.


## Maximum Drawdown (MDD)
The maximum observed loss from a peak to a trough of a portfolio, before a new peak is attained. Maximum drawdown is an indicator of downside risk over a specified time period.

> Basically the max loss seen in a portfolio over a specified time period.

## Calmar Ratio 
The average return of a portfolio divided by the MDD

## Jensen's Measure / Jensen's Alpha
```Alpha = R(i) - (R(f) + B x (R(m) - R(f)))```
Where:
R(i) = the realized return of the portfolio or investment
R(m) = the realized return of the appropriate market index
R(f) = the risk-free rate of return for the time period
B = the beta of the portfolio of investment with respect to the chosen market index
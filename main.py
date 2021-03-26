import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data import get_data
from dow_jones import dj_tickers

# Getting data from Quandl
table = get_data()

# Daily and annual returns + covariance
daily_returns = table.pct_change()
annual_returns = daily_returns.mean() * 365
daily_covariance = daily_returns.cov()
annual_covariance = daily_covariance * 365

# Important data points
returns = []
volatilities = []
weights = []
sharpe_ratios = []

asset_count = len(dj_tickers)
simulations = 50000

# Monte Carlo simulations
for _ in range(simulations):
    ws = np.random.random(asset_count)
    ws /= np.sum(ws)

    performance = np.dot(ws, annual_returns)
    volatility = np.sqrt(np.dot(ws.T, np.dot(annual_covariance, ws)))

    sharpe_ratio = performance / volatility
    print(sharpe_ratio)

    returns.append(performance)
    volatilities.append(volatility)
    sharpe_ratios.append(sharpe_ratio)
    weights.append(ws)

portfolio = {
    'Returns': returns,
    'Volatility': volatility,
    'Sharpe Ratio': sharpe_ratios
}

for counter, symbol in enumerate(dj_tickers):
    portfolio[f'{symbol} Weight'] = [Weight[counter] for Weight in weights]

df = pd.DataFrame(portfolio)
column_ordering = ['Returns', 'Volatility'] + [f'{asset} Weight' for asset in dj_tickers]

df = df[column_ordering]

plt.style.use('seaborn')
df.plot.scatter(x='Volatility', y='Returns', figsize=(10,8), grid=True)
plt.xlabel('Volatility (Standard Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier of Portfolios')
plt.show()
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
from os.path import join, dirname
from dotenv import load_dotenv

from dow_jones import tickers
from data import get_data


# Setting up Quandl API
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

QUANDL_API_KEY = os.environ.get('QUANDL_API_KEY')
quandl.ApiConfig.api_key = QUANDL_API_KEY

# Obtaining data from Quandl API
data = quandl.get_table('WIKI/PRICES', ticker = tickers,
                        qopts = { 'columns': ['date', 'ticker', 'adj_close'] },
                        date = { 'gte': '2016-1-1', 'lte': '2018-12-31' }, paginate=True)

# Cleaning data
by_date = data.set_index('date')
table = by_date.pivot(columns='ticker')

table.to_csv('data.csv', sep=',', encoding='utf-8')

print(table.head())

table = get_data()
print(table)
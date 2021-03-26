import quandl
import pandas as pd
import numpy as np
import os
from os.path import join, dirname
from dotenv import load_dotenv

from dow_jones import dj_tickers

def get_api_key():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get('QUANDL_API_KEY')

def get_data(tickers = dj_tickers):
    quandl.ApiConfig.api_key = get_api_key()
    data = quandl.get_table('WIKI/PRICES', ticker = tickers,
                            qopts = { 'columns': ['date', 'ticker', 'adj_close'] },
                            date = { 'gte': '2017-1-1', 'lte': '2018-12-31' }, paginate=True)
    
    table = data.set_index('date').pivot(columns='ticker')

    return table
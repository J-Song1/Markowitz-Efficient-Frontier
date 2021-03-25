import quandl
import pandas as pd
import numpy as np

import os
file_name = 'data.csv'

# Assumes Dow Jones data is being fetched
def get_data():
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
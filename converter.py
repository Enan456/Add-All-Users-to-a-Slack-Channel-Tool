#@author enan srivastava
#use for whatever
import pandas as pd
import os
import sys

df = pd.read_json('./users.json')
new_df = df['id']

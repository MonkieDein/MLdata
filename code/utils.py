
import pandas as pd
import numpy as np
import os 

# train_df = pd.read_feather('data/raw_data/AMEX/train_data.ftr/train_data.ftr')
# break_n_write_df(train_df,'data/split_data/AMEX/train/train_data',n=100)
def break_n_write_df(df,filename, n = 100):
    split = np.round(np.linspace(0,(len(df.index)),n+1)).astype('int')
    for i,s in enumerate(split[1:]):
        partial_df = df.iloc[split[i]:s,:].reset_index()
        partial_df.to_feather(f'{filename}_{i}.ftr')

# combine_df('data/split_data/AMEX/train/')
def combine_df(filename):
    files = os.listdir(filename)
    dfs = [pd.read_feather(f"{filename}{f}") for f in files]
    return pd.concat(dfs)

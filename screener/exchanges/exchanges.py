

#  Calls all the functions and constants needed for this module. This file should be called by main.py.

from exchanges.constants import ex_baselist
import pandas as pd


#  Turns the default exchanges list into a DataFrame and delivers it. Custom lists can be passed in through the arguments as well.
def df_ex_baselist(x=ex_baselist):
    df_ex_baselist = pd.DataFrame(x, columns=['mic', 'rank'])
    return df_ex_baselist


#  Gets passed the IEX Cloud exchanges data, and the baselist of exchanges, extracts only the exchange data for the baselist exchanges, and passes it pack as a DataFrame.
def extract_ex_details(baselist, iex_list):
    merged = baselist.merge(iex_list, how='inner', on='mic')
    return merged

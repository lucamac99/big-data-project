import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import datetime 
from datetime import date

# Importing the dataset
def data_preparation():

    df_rent = pd.read_csv('final.csv')

    # How to compose the final dataframe
    #df1 = pd.read_csv('housingtarget.csv')
    #df2 = pd.read_csv('housingtarget (2).csv')
    #df3 = pd.read_csv('housingtarget (3).csv')
    #frames = [df1, df2, df3]
    #result = pd.concat(frames)
    #result.to_csv('final.csv', sep='\t')

    return df_rent
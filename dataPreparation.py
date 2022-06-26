import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import datetime 
from datetime import date

def data_preparation():

    df = pd.read_csv('housingtarget.csv')
    #dfPrice = pd.read_csv('housingPrice.csv')
    #dfIndexes = pd.read_csv('housingIndexes.csv')

    return df
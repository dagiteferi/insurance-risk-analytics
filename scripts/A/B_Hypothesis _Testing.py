import pandas as pd
from scipy.stats import chi2_contingency , ttest_ind , f_oneway
import os

#function to load data
def data_load(filepath):
    
    return pd.read_csv(filepath)
#function to see the null values
def data_preprocess(data):
    return data.isnull().sum()
def categorical_outliers_detecting(data , column):
    return data[column].unique()
def handle_catagorical_outliers(data,column , valid_values , replecment_values=None):
    invalid_entries = data[~data[column].isin(valid_values)]


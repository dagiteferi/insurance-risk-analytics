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


#replace valid values
def handle_catagorical_outliers(data,column , valid_values , replecment_values=None):
    invalid_entries = data[~data[column].isin(valid_values)]
    if replecment_values is not None:
        data.loc[~data[column].isin(valid_values),column] = replecment_values
        return 'the outlier is replaced and here is the data', data
    else:
        data = data[data[column].isin(valid_values)]
        return 'remove rows with invalid rows' , data

# function to perform A/B Hypothesis testing to check if there are risk differences across provinces uses the chi- squared test for categorical data
def ab_test_provinces(data):
    

    #  create a contingency table for provinves and claims

    contingency_table = pd.crosstab(data['Province'],data['TotalClaims'])

    # perform chi-squared test 
    chi2,p_value, _, _ = chi2_contingency(contingency_table)

    return chi2,p_value,contingency_table

def ab_test_zipcodes(data):
    
    #perform A/B testing to check if there are risk differnces between zip codes
    #uses the chi-squared for categorical data
    
    # create a contingency table for zip codes and claims

    contingency_table = pd.crosstab(data['PostalCode'],data['TotalClaims'])

    # perform chi-squared test
    chi2 , p_value, _,_ = chi2_contingency(contingency_table)

    return chi2,p_value,contingency_table

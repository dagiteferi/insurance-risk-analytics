import pandas as pd
from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import OneHotEncoder
from scipy import sparse
from sklearn.decomposition import PCA

#function to load data
def data_load(path):
    return pd.read_csv(path)
#function to look the missing values
def missing_values(data):
    return data.isnull().sum()
#function to drop unwanted columns
def delete_unwanted_column(data ,columns_to_drop):
    data1 = data.drop(columns=columns_to_drop)
    return data1
#delete duplicated rows
def delete_duplicated_rows(data):
    data = data.drop_duplicates(keep="first")
    return data
#change object to number
def object_to_number(data,numeric_cols):
    dataframe = data.copy()
    dataframe[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')
    return dataframe
#encode the catagorical columns
def lable_encoding(data , catagoricalcols):
    dataframe = data.copy()
    le = LabelEncoder()
    for col in catagoricalcols:
        dataframe[col] = le.fit_transform(data[col])
    return dataframe

def one_hot_encoding(data,catagoricalcols):
    dataframe = data.copy()
    one_hot_encoder = OneHotEncoder(sparse_output=True)#convert categorical columns into one-hot encoded columns
    one_hot_encoded_matrix = one_hot_encoder.fit_transform(dataframe[catagoricalcols])#transforms them into a sparse matrix
    # Convert dense data (non-categorical) to sparse and combine
    rest_of_data = sparse.csr_matrix(dataframe.drop(columns=catagoricalcols))#converts the rest of the DataFrame (excluding the specified categorical columns) into a sparse matrix format.
    final_data = sparse.hstack([rest_of_data, one_hot_encoded_matrix])
    
    # reduce dimentinality
    # Apply PCA to reduce dimensions
    pca = PCA(n_components=100)  # Adjust n_components based on the explained variance
    reduced_data = pca.fit_transform(final_data.toarray())
    return reduced_data

def target_variable_and_features(data):#separates the target variable (TotalClaims) from the feature variables in the DataFrame.
    X= data.drop(columns=['TotalClaims'])
    y_claims = data['TotalClaims']
    return X ,y_claims
def train_test_split(X , y_claims):# splits the data into training and testing sets.
    x_train , x_test ,  y_train_claims , y_test_claims = train_test_split(X,y_claims , test_size=0.2, random_state=42)
    return x_train , x_test ,  y_train_claims , y_test_claims
def feature_scaling(x_train , x_test):#function scales the feature variables using standard scaling.
    scalar = StandardScaler()
    x_trian_scaled = scalar.fit_transform(x_train)
    x_test_scaled = scalar.transform(x_test)
    return x_trian_scaled ,x_test_scaled
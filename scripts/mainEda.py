#im
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class exploratory_data_analysis:
    def __init__(self,filepath) -> None:
        self.data = pd.read_csv(filepath,delimiter='|')
    def basic_info(self):
        print(f"info of the dataset{self.data.info()}")
        row ,col = self.data.shape
        print(f"the data has {col} X {row} ")
        print(f"discriptions of the data set  {self.data.describe()}")
    def basic_info_about_specified_colmn(self,*args):
        for ar in args:
            print(f"here is the discription about {ar} column {self.data[ar].describe()}")
    def missing_values(self):
        print(f' the missing value for each column {self.data.isnull().count()}')
        print(f'the total missing value for the dataset {self.data.isnull().sum()}')
    def handle_missing_values(self):
        numeric_col = self.data.select_dtypes(include=['number']).columns
        non_numeric_col = self.data.select_dtypes(exclude=['number']).columns
    
    #  filling missing values for the numeric cols
        for col in numeric_col:
            self.data[col].fillna(self.data[col].median(),inplace=True)
        
        # filling the missing value for the non numeric cols

        for col in non_numeric_col:
            self.data.fillna(self.data[col].mode()[0],inplace=True)
        
        return self.data.isnull().sum()
    def Univariate_analysis(self,column):
        # Histogram for Total Premium
        sns.histplot(self.data[column], bins=30)
        plt.title(f'Univariate Analysis of {column}')
        plt.show()
    def Bivariate_analysis(self,*args):
        # Scatter plot for Total Premium vs Total Claims
        sns.scatterplot(x=args[0], y=args[1], data=self.data)
        plt.title(f'Bivariate Analysis of {args[0]} and {args[1]}')
        plt.show()
    def Multivarite_analysis(self,*args):
        sns.pairplot(self.data[[ar for ar in args]])
        plt.show()
    def detecting_outliers(self,column):
        # Boxplot for Total Premium
        sns.boxplot(x=column, data=self.data)
        plt.title(f'Boxplot to Detect Outliers in {column}')
        plt.show()
    def handle_outliers(self,column):
        # Remove outliers based on TotalPremium values
        q1 = self.data[column].quantile(0.25)
        q3 = self.data[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        self.data = self.data[(self.data[column] >= lower_bound) & (self.data[column] <= upper_bound)]
        return "sucsess" , self.data
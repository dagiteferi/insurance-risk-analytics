import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class exploratory_data_analysis:
    def __init__(self, filepath) -> None:
        # Read the data
        self.data = pd.read_csv(filepath, delimiter='|')

    def _info(self):
        print(f"info of the dataset {self.data.info()}")
        row, col = self.data.shape
        print(f"The data has {col} columns and {row} rows.")
        print(f"Descriptions of the dataset: {self.data.describe()}")

    def _info_about_specified_colmn(self, *args):
        for ar in args:
            print(f"Here is the description of the {ar} column: {self.data[ar].describe()}")

    def missing_values(self):
        print(f"The missing value count for each column: {self.data.isnull().sum()}")
        print(f"The total missing value count for the dataset: {self.data.isnull().sum().sum()}")

    def handle_missing_values(self):
        numeric_col = self.data.select_dtypes(include=['number']).columns
        non_numeric_col = self.data.select_dtypes(exclude=['number']).columns
        
        # Filling missing values for the numeric columns
        for col in numeric_col:
            self.data[col] = self.data[col].fillna(self.data[col].median())
        
        # Filling the missing value for the non-numeric columns
        for col in non_numeric_col:
            self.data[col] = self.data[col].fillna(self.data[col].mode()[0])
        
        return self.data.isnull().sum()

    def Univariate_analysis(self, column):
        # Histogram for the specified column
        sns.histplot(self.data[column], bins=30)
        plt.title(f'Univariate Analysis of {column}')
        plt.show()

    def Bivariate_analysis(self, *args):
        # Scatter plot for the specified columns
        sns.scatterplot(x=args[0], y=args[1], data=self.data)
        plt.title(f'Bivariate Analysis of {args[0]} and {args[1]}')
        plt.show()

    def Multivarite_analysis(self, *args):
        sns.pairplot(self.data[[ar for ar in args]])
        plt.show()

    def detecting_outliers(self, column):
        # Boxplot for detecting outliers in the specified column
        sns.boxplot(x=column, data=self.data)
        plt.title(f'Boxplot to Detect Outliers in {column}')
        plt.show()
    def _basic_columns_ploting(self,*args):
        for ar in args:
            plt.figure(figsize=(10,6))
            sns.histplot(self.data[ar],bins=30,kde=True)
            plt.title(f" Distribution of the {ar}")
            plt.show()
    def two_columns_scatter_plot(self,*args):
        plt.figure(figsize=(10,6))
        sns.scatterplot(x=args[0],y=args[1],data=self.data)
        plt.title(f" {args[0]}  X {args[1]} ")
        plt.show()

    def handle_outliers(self, column):
        # Remove outliers based on the specified column's values
        q1 = self.data[column].quantile(0.25)
        q3 = self.data[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        self.data = self.data[(self.data[column] >= lower_bound) & (self.data[column] <= upper_bound)]
        return "success", self.data
    
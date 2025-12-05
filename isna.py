import pandas as pd
df=pd.read_csv('sales_data.csv')
#Check for missing values in each column.
df.isna().sum()

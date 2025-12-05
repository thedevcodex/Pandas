import pandas as pd
df=pd.read_csv('sales_data.csv')
#Show all unique product categories.
df["Category"].unique()

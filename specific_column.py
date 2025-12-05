import pandas as pd
df=pd.read_csv('sales_data.csv')
#Print only the Customer and Product columns.
df[['Customer',"Product"]]

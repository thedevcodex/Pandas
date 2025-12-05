import pandas as pd
df=pd.read_csv('sales_data.csv')
#Show statistics of numerical columns using describe().
df.describe()

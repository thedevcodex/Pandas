import pandas as pd
df=pd.read_csv('sales_data.csv')
#Filter rows where Payment Mode = "UPI".
df[df["Payment Mode"]=="UPI"]

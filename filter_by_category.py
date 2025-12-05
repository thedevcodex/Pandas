import pandas as pd
df=pd.read_csv('sales_data.csv')
#Filter rows where Category = "Electronics".
df[df["Category"]=="Electronics"]

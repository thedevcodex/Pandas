#Rank products by total revenue.
total_revnue=df.groupby('product_name')['total_amount'].sum().reset_index()
total_revnue
total_revnue["Rank"]=total_revnue['total_amount'].rank(ascending=False).astype(int)

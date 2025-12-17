#Find customer who spent the most money.
df.groupby('customer_name')["total_amount"].sum().sort_values(ascending=False).head(1)

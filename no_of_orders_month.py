#Find number of orders per month.
df.groupby('month')['order_id'].count().reset_index(name="no of orders")

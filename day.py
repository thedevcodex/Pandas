#Count number of orders per day.
df.groupby('date')['order_id'].count().reset_index(name="total_orders")

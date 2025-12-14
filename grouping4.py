#Count number of orders per category.
df.groupby("category")["order_id"].count().reset_index()

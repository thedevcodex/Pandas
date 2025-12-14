#Find average price of products.
df.groupby("product_name")["price"].mean()

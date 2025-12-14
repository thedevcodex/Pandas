#Find total revenue per product.
df.groupby("product_name")[["price"]].sum()

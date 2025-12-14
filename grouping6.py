#Find average quantity per order.
df.groupby("product_name")["quantity"].mean()

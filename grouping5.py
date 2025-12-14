#Find total quantity sold for each product.
df.groupby("product_name")["quantity"].sum().reset_index()

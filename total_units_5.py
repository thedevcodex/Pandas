#Find products sold more than 5 units in total.
df.groupby("product_name")["quantity"].sum().reset_index().query("quantity>5")

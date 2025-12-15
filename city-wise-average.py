#Find city-wise average quantity.
df.groupby("city")["quantity"].mean().reset_index(name="QTY AVG")

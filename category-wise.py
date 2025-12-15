#Find category-wise average price.
df.groupby("category")["price"].mean().reset_index(name="Avg")

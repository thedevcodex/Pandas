#Find total revenue per city.
df.groupby("city")[["price"]].sum()

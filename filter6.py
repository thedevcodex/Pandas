#Find total sales for Electronics category only.
df[df["category"]=="Electronics"][["price"]].sum()

#Find total sales by female customers.
df[df["gender"]=="F"][["price"]].sum()

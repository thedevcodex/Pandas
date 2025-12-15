#Find total sales by male customers.
df[df["gender"]=="M"][["price"]].sum()

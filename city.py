#Find number of Laptop orders per city.
df[df["product_name"]=="Laptop"].groupby("city")["product_name"].count().reset_index(name="order_count")

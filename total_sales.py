#Find total sales amount (price × quantity).
df["total_amount"]=df["price"]*df["quantity"]
total_sales=df["total_amount"].sum()
total_sales

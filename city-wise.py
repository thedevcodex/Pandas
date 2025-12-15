#Find city-wise total sales where sales > 50,000.
df.groupby("city")["total_amount"].sum().reset_index().query("total_amount>50000")

#Find top 5 highest total_amount orders.
df.sort_values('total_amount',ascending=False).head(5)

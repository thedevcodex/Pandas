#Find city with highest total sales.
df.groupby("city")['total_amount'].sum().sort_values(ascending=False).reset_index(name="total_amount").head(1)

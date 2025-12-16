#Find total sales per month.
df.groupby('month')['total_amount'].sum().reset_index(name="total_sales")

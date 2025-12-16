#Find total sales for February 2024.
df[(df["month"]=="February") & (df['year']==2024)][['total_amount']].sum().reset_index(name="Feb_sales")

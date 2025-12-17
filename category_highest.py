#Find category contributing highest revenue.
df.groupby('category')["total_amount"].sum().sort_values(ascending=False).reset_index(name="highest_total").head(1)

#Find total revenue generated in Chennai.
df.groupby("city")["total_amount"].sum().reset_index().query('`city`=="Chennai"')

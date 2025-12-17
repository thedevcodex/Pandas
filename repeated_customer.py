#Find repeat customers (customers appearing more than once).
df["customer_name"].value_counts()[df["customer_name"].value_counts()>1]

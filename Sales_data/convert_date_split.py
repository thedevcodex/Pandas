#convert date data
df['order_date']=pd.to_datetime(df["order_date"])
#split date
df["date"]=df["order_date"].dt.day
#split month
df["month"]=df["order_date"].dt.month_name()
df["year"]=df["order_date"].dt.year

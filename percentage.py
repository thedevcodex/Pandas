#Find percentage contribution of each category to total sales.

percentage_cal=df.groupby('category')['total_amount'].sum().reset_index()
percentage_cal['percentage']=(percentage_cal['total_amount']/percentage_cal["total_amount"].sum())*100
percentage_cal["percentage"]=percentage_cal['percentage'].round(2)
percentage_cal.sort_values('percentage',ascending=False).head(1)

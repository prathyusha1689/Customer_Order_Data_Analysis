import pandas as pd
df = pd.read_csv("cleaned_orders.csv")
print(df.head())
total_revenue = df["total_amount"].sum()
print("Total Revenue:", total_revenue)
revenue_by_category = df.groupby("category")["total_amount"].sum()
print(revenue_by_category)
revenue_by_status = df.groupby("status")["total_amount"].sum()
print(revenue_by_status)
orders_by_status = df["status"].value_counts()
print(orders_by_status)
revenue_by_customer = df.groupby("customer_id")["total_amount"].sum().sort_values(ascending=False)
print(revenue_by_customer)
revenue_by_product = df.groupby("product")["total_amount"].sum().sort_values(ascending=False)
print(revenue_by_product)
quantity_by_product = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
print(quantity_by_product)
average_order_value = df["total_amount"].mean()
print("Average Order Value:", average_order_value)
highest_order = df["total_amount"].max()
print("Highest Order Value:", highest_order)
highest_order_details = df[df["total_amount"] == df["total_amount"].max()]
print(highest_order_details)
lowest_order = df["total_amount"].min()
print("Lowest Order Value:", lowest_order)

lowest_order_details = df[df["total_amount"] == df["total_amount"].min()]
print(lowest_order_details)
unique_customers = df["customer_id"].nunique()
print("Number of Unique Customers:", unique_customers)
orders_per_customer = df["customer_id"].value_counts()
print(orders_per_customer)
average_revenue_per_customer = total_revenue / unique_customers
print("Average Revenue Per Customer:", average_revenue_per_customer)
revenue_percentage_by_status = (revenue_by_status / total_revenue) * 100
print(revenue_percentage_by_status)
total_orders = len(df)

completed_orders = (df["status"] == "Completed").sum()

completion_rate = (completed_orders / total_orders) * 100

print("Total Orders:", total_orders)
print("Completed Orders:", completed_orders)
print("Order Completion Rate:", completion_rate)
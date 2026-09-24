import pandas as pd

df = pd.read_csv("orders.csv")

print(df.head())

df.info()
df["order_date"] = pd.to_datetime(df["order_date"])
print(df["order_date"].dtype)
print(df.isnull().sum())
print(df.duplicated().sum())
df["status"] = df["status"].str.strip()
print(df["status"].unique())
df["customer_id"] = df["customer_id"].str.strip()
df["product"] = df["product"].str.strip()
df["category"] = df["category"].str.strip()
print(df[["quantity", "price"]].describe())


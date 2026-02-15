import pandas as pd

# Load data
df = pd.read_csv("train.csv")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y", errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y", errors="coerce")

# Fill missing Postal Code with 0
df["Postal Code"] = df["Postal Code"].fillna(0).astype(int)

# Create new time features
df["Order_Year"] = df["Order Date"].dt.year
df["Order_Month"] = df["Order Date"].dt.month
df["Order_MonthName"] = df["Order Date"].dt.month_name()

# Remove duplicates (safety)
df = df.drop_duplicates()

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned successfully!")
print("Rows:", len(df))

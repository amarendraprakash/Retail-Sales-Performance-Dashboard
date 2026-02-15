import pandas as pd
from sqlalchemy import create_engine

# CHANGE password here
username = "MySql_USERNAME"
password = "YOUR_PASSWORD_FOR_MySQL"
host = "localhost"
database = "retail_analytics"

# Connection string
engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
)

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Upload to MySQL
df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Data uploaded successfully to MySQL!")

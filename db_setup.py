import sqlite3
import pandas as pd

# Load your CSV
df = pd.read_csv("File 1.csv")

# Connect to (create) database
conn = sqlite3.connect("ma_deals.db")

# Save data into SQL table
df.to_sql("acquisitions", conn, if_exists="replace", index=False)

print("Database created successfully!")
print("Total records loaded:", len(df))

conn.close()
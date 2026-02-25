import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("ma_deals.db")

# Query 1 — Who acquires the most?
query1 = """
    SELECT "Parent Company", 
           COUNT(*) AS total_acquisitions
    FROM acquisitions
    GROUP BY "Parent Company"
    ORDER BY total_acquisitions DESC
"""

result1 = pd.read_sql(query1, conn)
print("=== Acquisition Count by Company ===")
print(result1)

# Query 2 — Acquisitions by Year (market cycle trend)
query2 = """
    SELECT "Acquisition Year",
           COUNT(*) AS total_acquisitions
    FROM acquisitions
    GROUP BY "Acquisition Year"
    ORDER BY "Acquisition Year" ASC
"""

result2 = pd.read_sql(query2, conn)
print("\n=== Acquisitions by Year ===")
print(result2.to_string())

# Query 3 — Which countries are targeted most?
query3 = """
    SELECT Country,
           COUNT(*) AS total_acquisitions
    FROM acquisitions
    WHERE Country != '-'
    GROUP BY Country
    ORDER BY total_acquisitions DESC
    LIMIT 10
"""

result3 = pd.read_sql(query3, conn)
print("\n=== Top 10 Target Countries ===")
print(result3)

conn.close()
import sqlite3
import pandas as pd

conn = sqlite3.connect("ma_deals.db")

print("=" * 60)
print("M&A STRATEGIC INTELLIGENCE REPORT")
print("=" * 60)

# ---- Insight 1: Most Aggressive Acquirer ----
query1 = """
    SELECT "Parent Company", COUNT(*) AS total
    FROM acquisitions
    GROUP BY "Parent Company"
    ORDER BY total DESC
    LIMIT 1
"""
df1 = pd.read_sql(query1, conn)
print(f"\n📊 INSIGHT 1 — MOST AGGRESSIVE ACQUIRER")
print(f"{df1.iloc[0]['Parent Company']} leads with {df1.iloc[0]['total']} acquisitions")
print("This reflects Microsoft's inorganic growth strategy —")
print("acquiring capabilities rather than building them internally.")

# ---- Insight 2: Dot-com Bubble Evidence ----
query2 = """
    SELECT "Acquisition Year", COUNT(*) AS total
    FROM acquisitions
    WHERE "Acquisition Year" IN ('1999', '2000', '2001')
    GROUP BY "Acquisition Year"
    ORDER BY "Acquisition Year"
"""
df2 = pd.read_sql(query2, conn)
print(f"\n📊 INSIGHT 2 — DOT-COM BUBBLE IMPACT")
print(df2.to_string(index=False))
print("41 deals in 1999 crashed to 20 in 2000 —")
print("consistent with capital markets freezing post dot-com burst.")

# ---- Insight 3: Post-Financial Crisis Boom ----
query3 = """
    SELECT "Acquisition Year", COUNT(*) AS total
    FROM acquisitions
    WHERE "Acquisition Year" BETWEEN '2009' AND '2014'
    GROUP BY "Acquisition Year"
    ORDER BY "Acquisition Year"
"""
df3 = pd.read_sql(query3, conn)
print(f"\n📊 INSIGHT 3 — POST CRISIS ACQUISITION BOOM")
print(df3.to_string(index=False))
print("Acquisitions surged from 38 in 2009 to 100 in 2014.")
print("Low interest rates post-2008 made deal financing cheap —")
print("directly linked to quantitative easing and monetary policy.")

# ---- Insight 4: US Dominance ----
query4 = """
    SELECT Country, COUNT(*) AS total
    FROM acquisitions
    WHERE Country != '-'
    GROUP BY Country
    ORDER BY total DESC
    LIMIT 5
"""
df4 = pd.read_sql(query4, conn)
print(f"\n📊 INSIGHT 4 — GEOGRAPHIC CONCENTRATION")
print(df4.to_string(index=False))
print("248 out of all international deals target US companies —")
print("reflecting Silicon Valley's dominance in tech innovation.")

# ---- Insight 5: Peak Year ----
query5 = """
    SELECT "Acquisition Year", COUNT(*) AS total
    FROM acquisitions
    WHERE "Acquisition Year" != '-'
    GROUP BY "Acquisition Year"
    ORDER BY total DESC
    LIMIT 1
"""
df5 = pd.read_sql(query5, conn)
print(f"\n📊 INSIGHT 5 — PEAK ACQUISITION YEAR")
print(f"Peak year was {df5.iloc[0]['Acquisition Year']} with {df5.iloc[0]['total']} deals")
print("2014 represented peak cheap money era —")
print("Fed funds rate near zero, debt financing at historic lows.")

print("\n" + "=" * 60)
print("END OF REPORT")
print("=" * 60)

conn.close()
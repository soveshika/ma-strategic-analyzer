import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to database
conn = sqlite3.connect("ma_deals.db")

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ---- Chart 1: Acquisitions by Company ----
query1 = """
    SELECT "Parent Company", COUNT(*) AS total
    FROM acquisitions
    GROUP BY "Parent Company"
    ORDER BY total DESC
"""
df1 = pd.read_sql(query1, conn)

plt.figure()
sns.barplot(data=df1, x='total', y='Parent Company', palette='Blues_d')
plt.title('Total Acquisitions by Company', fontsize=16, fontweight='bold')
plt.xlabel('Number of Acquisitions')
plt.ylabel('Company')
plt.tight_layout()
plt.savefig('chart1_by_company.png')
plt.show()
print("Chart 1 saved!")

# ---- Chart 2: Acquisitions by Year ----
query2 = """
    SELECT "Acquisition Year", COUNT(*) AS total
    FROM acquisitions
    WHERE "Acquisition Year" != '-'
    AND "Acquisition Year" >= 1995
    GROUP BY "Acquisition Year"
    ORDER BY "Acquisition Year" ASC
"""
df2 = pd.read_sql(query2, conn)
df2['Acquisition Year'] = df2['Acquisition Year'].astype(int)

plt.figure()
plt.plot(df2['Acquisition Year'], df2['total'], marker='o', color='steelblue', linewidth=2)

# Mark key market events
plt.axvline(x=2000, color='red', linestyle='--', alpha=0.7, label='Dot-com Crash')
plt.axvline(x=2008, color='orange', linestyle='--', alpha=0.7, label='Financial Crisis')
plt.axvline(x=2020, color='green', linestyle='--', alpha=0.7, label='COVID-19')

plt.title('M&A Activity Over Time — Market Cycles', fontsize=16, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Acquisitions')
plt.legend()
plt.tight_layout()
plt.savefig('chart2_by_year.png')
plt.show()
print("Chart 2 saved!")

# ---- Chart 3: Top 10 Target Countries ----
query3 = """
    SELECT Country, COUNT(*) AS total
    FROM acquisitions
    WHERE Country != '-'
    GROUP BY Country
    ORDER BY total DESC
    LIMIT 10
"""
df3 = pd.read_sql(query3, conn)

plt.figure()
sns.barplot(data=df3, x='total', y='Country', palette='Greens_d')
plt.title('Top 10 Target Countries in M&A Deals', fontsize=16, fontweight='bold')
plt.xlabel('Number of Acquisitions')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('chart3_by_country.png')
plt.show()
print("Chart 3 saved!")
# ---- Chart 4: Acquisition Activity by Company Over Time ----
query4 = """
    SELECT "Parent Company", "Acquisition Year", COUNT(*) AS total
    FROM acquisitions
    WHERE "Acquisition Year" != '-'
    AND "Acquisition Year" >= 2000
    GROUP BY "Parent Company", "Acquisition Year"
    ORDER BY "Acquisition Year" ASC
"""
df4 = pd.read_sql(query4, conn)
df4['Acquisition Year'] = df4['Acquisition Year'].astype(int)

plt.figure(figsize=(14, 7))
companies = df4['Parent Company'].unique()

for company in companies:
    company_data = df4[df4['Parent Company'] == company]
    plt.plot(company_data['Acquisition Year'], 
             company_data['total'], 
             marker='o', 
             linewidth=2, 
             label=company)

plt.title('Acquisition Race — Who Was Buying When?', fontsize=16, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Acquisitions')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('chart4_company_race.png')
plt.show()
print("Chart 4 saved!")

conn.close()
print("\nAll charts saved successfully!")

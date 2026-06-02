import pandas as pd
import sqlite3

df = pd.read_csv('sip_portfolio_ready.csv')
conn = sqlite3.connect('wealth_tracker.sqlite')
df.to_sql('portfolio', conn, if_exists='replace', index=False)

print("--- SIP Portfolio and SQL Analsis ---\n")

query1 = """
SELECT 
    MAX(Total_Invested) AS Total_Investment_INR,
    MAX(Portfolio_Value) AS Current_Value_INR,
    ROUND(MAX(Portfolio_Value) - MAX(Total_Invested), 2) AS Net_Profit_INR,
    ROUND(((MAX(Portfolio_Value) - MAX(Total_Invested)) / MAX(Total_Invested)) * 100, 2) AS Absolute_Return_Percent
FROM portfolio;
"""

print("Total Benifit and Return (%)")
print(pd.read_sql(query1, conn))
print("-" * 60)

query2 = """
SELECT Date, Close, ROUND(Units_Bought, 2) AS Units_Purchased
FROM portfolio
ORDER BY Close ASC
LIMIT 3;
"""
print("2. Top 3 Cheapest Months (Best Buying Opportunities):")
print(pd.read_sql(query2, conn))

conn.close()
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print("Data are downloading ! Plaese wait...")

# Step 1: Extract 
start_date = "2026-01-01"
end_date = "2026-06-01"

nifty_data = yf.download('^NSEI', start=start_date, end=end_date)
gold_data = yf.download('GC=F', start=start_date, end=end_date)
oil_data = yf.download('CL=F', start=start_date, end=end_date)

# Step 2: Transform 
df_nifty = nifty_data[['Close']].rename(columns={'Close': 'Nifty50'})
df_gold = gold_data[['Close']].rename(columns={'Close': 'Gold'})
df_oil = oil_data[['Close']].rename(columns={'Close': 'CrudeOil'})

market_data = df_nifty.join([df_gold, df_oil], how='outer')

# यहाँ हमने bfill() जोड़ दिया है
market_data = market_data.ffill().bfill()

market_data_normalized = (market_data / market_data.iloc[0]) * 100

# Step 3: Load
print("\Our cleaning data in first 5 rows ---")
print(market_data_normalized.head())

market_data_normalized.to_csv('cleaned_market_data.csv')
print("\nडेटा 'cleaned_market_data.csv' फाइल में सेव हो गया है।")

# Step 4: Visualize
plt.figure(figsize=(12, 6))
plt.plot(market_data_normalized.index, market_data_normalized['Nifty50'], label='Nifty 50 (Stocks)', color='blue')
plt.plot(market_data_normalized.index, market_data_normalized['Gold'], label='Gold', color='gold')
plt.plot(market_data_normalized.index, market_data_normalized['CrudeOil'], label='Crude Oil', color='red')

plt.title('Global News Impact on Markets')
plt.xlabel('Date')
plt.ylabel('Normalized Price (Base 100)')
plt.legend()
plt.grid(True)
plt.show()
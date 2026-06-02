import pandas as pd

print("Data Transform and SIP are calculating ...")

# 1. डेटा लोड करें
df = pd.read_csv('niftybees_5yr_data.csv')
df = df.iloc[:, [0, 1]] 
df.columns = ['Date', 'Close']

# --- नया फिक्स (Error Resolver) ---
# 'Close' कॉलम को ज़बरदस्ती नंबर्स (Float) में बदलना
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
# जो एक्स्ट्रा टेक्स्ट NaN बन गया है, उस पूरी लाइन को डिलीट कर देना
df.dropna(inplace=True)
# ----------------------------------

# 2. Date कॉलम को सही फॉर्मेट (Datetime) में बदलें
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 3. डेली डेटा को 'मंथली' (Monthly) डेटा में बदलें
df_monthly = df.resample('ME').last()

# 4. SIP का लॉजिक (हर महीने ₹5,000 इन्वेस्ट)
sip_amount = 5000

df_monthly['Units_Bought'] = sip_amount / df_monthly['Close']
df_monthly['Total_Units'] = df_monthly['Units_Bought'].cumsum()
df_monthly['Invested_Amount'] = sip_amount
df_monthly['Total_Invested'] = df_monthly['Invested_Amount'].cumsum()
df_monthly['Portfolio_Value'] = df_monthly['Total_Units'] * df_monthly['Close']

df_monthly = df_monthly.round(2)

print("Ready SIP Portfolio-")
print(df_monthly[['Close', 'Total_Invested', 'Portfolio_Value']].tail())

# 5. Load
df_monthly.to_csv('sip_portfolio_ready.csv')
print("'sip_portfolio_ready.csv' are saved")
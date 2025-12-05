code = """import json, pandas as pd

# Load full trade data from file
file_path = var_call_wALYIwiNVILD8UFTQ1TozZbS
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Parse dates robustly
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter from 2000-01-01
start_date = pd.Timestamp('2000-01-01')
df = df[df['Date'] >= start_date].copy()

# Ensure numeric CloseUSD
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Monthly investment strategy: invest fixed 1 unit of currency per month at first available trading day
# For each Index and calendar month, find first trading day, compute units bought and final value at last date

# Add year-month column
df['year_month'] = df['Date'].dt.to_period('M')

# First trading day per index and month
first_days = df.sort_values('Date').groupby(['Index','year_month']).first().reset_index()[['Index','year_month','Date','CloseUSD']]
first_days.rename(columns={'Date':'buy_date','CloseUSD':'buy_price'}, inplace=True)

# Last available price per index (for final valuation)
last_prices = df.sort_values('Date').groupby('Index').last().reset_index()[['Index','Date','CloseUSD']]
last_prices.rename(columns={'Date':'final_date','CloseUSD':'final_price'}, inplace=True)

# Assume 1 USD invested per month per index
first_days['units'] = 1.0 / first_days['buy_price']

# Total units accumulated per index
units_per_index = first_days.groupby('Index')['units'].sum().reset_index()

# Merge with final prices
result = pd.merge(units_per_index, last_prices, on='Index', how='inner')

# Compute final portfolio value per index
result['final_value'] = result['units'] * result['final_price']

# Sort and take top 5
top5 = result.sort_values('final_value', ascending=False).head(5)

out = top5[['Index','final_value']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_t2GFqfZ0RndPOXVW6QUoLy6L': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}], 'var_call_wALYIwiNVILD8UFTQ1TozZbS': 'file_storage/call_wALYIwiNVILD8UFTQ1TozZbS.json'}

exec(code, env_args)

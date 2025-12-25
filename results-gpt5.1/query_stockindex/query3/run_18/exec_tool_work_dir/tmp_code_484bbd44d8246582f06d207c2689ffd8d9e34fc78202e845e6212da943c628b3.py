code = """import pandas as pd, json, os

# Load full large result from file
file_path = var_call_Ea8GE82G5lTmdQImdVwpdLDK
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize date column to pandas datetime, coerce errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for dates >= 2000-01-01
start_date = pd.Timestamp('2000-01-01')
df = df[df['Date'] >= start_date].copy()

# Use Adj Close as price. Simulate investing 1 unit of currency at the first trading day of each month.
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')

# Drop rows with missing prices
df = df.dropna(subset=['Adj Close'])

# Extract year-month
df['YearMonth'] = df['Date'].dt.to_period('M')

# For each index and month, pick the first trading day price
first_prices = df.sort_values(['Index', 'Date']).groupby(['Index', 'YearMonth']).first().reset_index()

# For each index, compute total shares accumulated and final value at last date
results = []
for idx, grp in first_prices.groupby('Index'):
    # 1 unit invested each month
    monthly_invest = 1.0
    shares = (monthly_invest / grp['Adj Close']).sum()
    # get final price for this index from df
    idx_data = df[df['Index'] == idx]
    if idx_data.empty:
        continue
    final_price = idx_data.sort_values('Date')['Adj Close'].iloc[-1]
    final_value = shares * final_price
    total_invested = monthly_invest * len(grp)
    total_return = final_value / total_invested - 1.0
    results.append({'Index': idx, 'final_value_per_1_unit_monthly': float(final_value), 'total_return': float(total_return), 'months': int(len(grp))})

res_df = pd.DataFrame(results)

# Keep indices that have data from at least Jan 2000 to some reasonable end, say at least 200 months (~16.7 years)
res_df = res_df[res_df['months'] >= 200]

# Get top 5 by final value
top5 = res_df.sort_values('final_value_per_1_unit_monthly', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WRoboxY7tpquHRgiR8Z3Ug2y': [{'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00'}, {'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00'}], 'var_call_Ea8GE82G5lTmdQImdVwpdLDK': 'file_storage/call_Ea8GE82G5lTmdQImdVwpdLDK.json'}

exec(code, env_args)

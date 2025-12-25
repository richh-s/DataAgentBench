code = """import pandas as pd, json
import os

# Load full index trade data from file
path = var_call_JTpjKWuFIGcC7slGc59nlzqG
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure correct dtypes
df['Adj Close'] = pd.to_numeric(df['Adj Close'])
# Use errors='coerce' to handle any bad date formats
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

# Define monthly DCA: invest 1 unit of currency at the last trading day of each month
# For each index and month, get last available trading day
df['YearMonth'] = df['Date'].dt.to_period('M')

last_per_month = df.sort_values('Date').groupby(['Index','YearMonth']).tail(1)

# For each index, simulate investing 1 per month: units bought = 1 / price
last_per_month['units'] = 1.0 / last_per_month['Adj Close']

# Aggregate per index
agg = last_per_month.groupby('Index').agg(
    total_invested=('units', 'size'),  # 1 per month
    total_units=('units', 'sum')
).reset_index()

# Need latest price for each index
latest_price = df.sort_values('Date').groupby('Index').tail(1)[['Index','Adj Close']]
latest_price = latest_price.rename(columns={'Adj Close':'latest_price'})

result = agg.merge(latest_price, on='Index', how='left')
result['final_value'] = result['total_units'] * result['latest_price']
result['return_multiple'] = result['final_value'] / result['total_invested']

# Top 5 indices by return multiple
top5 = result.sort_values('return_multiple', ascending=False).head(5)

# Map index symbol to country using general knowledge (hard-coded mapping for common indices)
country_map = {
    'N225': 'Japan',
    '000001.SS': 'China',
    'HSI': 'Hong Kong',
    '^GSPC': 'United States',
    '^DJI': 'United States',
    '^IXIC': 'United States',
    '^GDAXI': 'Germany',
    '^FCHI': 'France',
    '^FTSE': 'United Kingdom',
    '^BSESN': 'India',
    '^KS11': 'South Korea',
    '^TWII': 'Taiwan',
    '^AXJO': 'Australia',
    '^BVSP': 'Brazil',
}

top5['Country'] = top5['Index'].map(country_map).fillna('Unknown')

out = top5[['Index','Country','return_multiple']]

res = out.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_JTpjKWuFIGcC7slGc59nlzqG': 'file_storage/call_JTpjKWuFIGcC7slGc59nlzqG.json', 'var_call_TmzIa6Kar98AL2NDmrDfyYMt': ['index_info']}

exec(code, env_args)

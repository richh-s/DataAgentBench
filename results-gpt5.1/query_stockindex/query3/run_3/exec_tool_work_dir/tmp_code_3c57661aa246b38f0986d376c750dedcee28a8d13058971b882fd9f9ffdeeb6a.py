code = """import json, pandas as pd
from datetime import datetime

file_path = var_call_BSuOFlH8Iu9y6ZmdXR714pPX
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse heterogeneous date formats, coerce errors
for fmt in ['%Y-%m-%d', '%d %b %Y, %H:%M', '%B %d, %Y at %I:%M %p']:
    mask = df['Date'].notna() & df['Date'].astype(str).str.contains(',')

# Just let pandas infer
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter from 2000-01-01
start = pd.Timestamp('2000-01-01')
monthly = df[df['Date_parsed'] >= start].copy()

# Ensure numeric prices
monthly['Adj Close'] = pd.to_numeric(monthly['Adj Close'], errors='coerce')
monthly = monthly.dropna(subset=['Adj Close', 'Date_parsed'])

# Get month-end price per index
monthly['year_month'] = monthly['Date_parsed'].dt.to_period('M')
idx = monthly.sort_values(['Index','Date_parsed']).groupby(['Index','year_month']).tail(1)

# Assume invest 1 unit of currency each month; compute total units bought and final value
# For each index, units bought each month = 1 / price
idx['units'] = 1.0 / idx['Adj Close']
summary = idx.groupby('Index').agg(total_units=('units','sum'), final_price=('Adj Close','last'), n_months=('units','size')).reset_index()
summary['final_value'] = summary['total_units'] * summary['final_price']

# Rank by final_value
top5 = summary.sort_values('final_value', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BSuOFlH8Iu9y6ZmdXR714pPX': 'file_storage/call_BSuOFlH8Iu9y6ZmdXR714pPX.json'}

exec(code, env_args)

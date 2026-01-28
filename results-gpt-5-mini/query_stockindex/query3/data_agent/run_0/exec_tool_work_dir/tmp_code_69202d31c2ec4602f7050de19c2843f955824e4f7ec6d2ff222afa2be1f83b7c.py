code = """import json
import pandas as pd

# Load data from previous query result file
data_path = var_call_FENNapoieD7wD1ghxbQftmMP
with open(data_path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Robust parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# Ensure CloseUSD numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Drop rows with invalid date or price
df = df.dropna(subset=['Date', 'CloseUSD']).copy()

# Filter from 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

# Known mapping of index symbol to country (inferred)
index_country = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'IXIC': 'United States',
    'N100': 'Euronext (multiple countries)',
    '399001.SZ': 'China'
}

results = []

for idx, group in df.groupby('Index'):
    g = group.sort_values('Date').copy()
    if g.empty:
        continue
    # YearMonth period
    g['YearMonth'] = g['Date'].dt.to_period('M')
    # For each YearMonth, pick the row with the earliest Date
    first_in_month_idx = g.groupby('YearMonth')['Date'].idxmin()
    monthly = g.loc[first_in_month_idx].sort_values('YearMonth')
    # Only include months >= 2000-01
    monthly = monthly[monthly['YearMonth'] >= pd.Period('2000-01')]
    if monthly.empty:
        continue
    # Simulate investing $1 each month at that month's first close price
    monthly['Units'] = 1.0 / monthly['CloseUSD']
    total_units = monthly['Units'].sum()
    total_invested = float(len(monthly)) * 1.0
    # final value based on last available CloseUSD for that index
    last_close = float(g.iloc[-1]['CloseUSD'])
    final_value = total_units * last_close
    multiple = final_value / total_invested if total_invested > 0 else None
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, 'Unknown'),
        'MonthsInvested': int(len(monthly)),
        'TotalInvested': total_invested,
        'FinalValue': final_value,
        'ReturnMultiple': multiple
    })

# Rank by ReturnMultiple descending
results_sorted = sorted(results, key=lambda x: (x['ReturnMultiple'] if x['ReturnMultiple'] is not None else -999), reverse=True)

top5 = results_sorted[:5]

# Prepare output - round numeric values for readability
for r in top5:
    r['FinalValue'] = round(r['FinalValue'], 6)
    r['ReturnMultiple'] = round(r['ReturnMultiple'], 6)

out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Vo3LQYicZx6g3AxKv9OabBKv': ['index_trade'], 'var_call_uFLc1r1fLWZ5EQxixBWR8IpQ': ['index_info'], 'var_call_SuIG4Cb5dW7WmytnNgUNH8nU': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_4q4kvoeJ3005YzZ6smtzjOQr': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_FENNapoieD7wD1ghxbQftmMP': 'file_storage/call_FENNapoieD7wD1ghxbQftmMP.json'}

exec(code, env_args)

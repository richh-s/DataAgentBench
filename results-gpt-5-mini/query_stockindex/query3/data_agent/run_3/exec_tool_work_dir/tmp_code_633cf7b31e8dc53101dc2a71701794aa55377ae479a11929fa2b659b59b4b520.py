code = """import pandas as pd
import json

# load data from the stored JSON file path variable
filepath = var_call_O0sNfYwWWnfN6tfD51SZOon6
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Normalize column names
# Parse dates
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)
# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Drop rows with missing values in Date or CloseUSD
df = df.dropna(subset=['Date', 'CloseUSD'])
# Filter for data since 2000-01-01
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]

results = []
for idx, group in df.groupby('Index'):
    g = group.sort_values('Date').reset_index(drop=True)
    # Determine first trading day of each month in the available range
    if g.empty:
        continue
    g['period'] = g['Date'].dt.to_period('M')
    # For each month, pick the earliest date's CloseUSD
    first_trades = g.loc[g.groupby('period')['Date'].idxmin()]
    months_count = len(first_trades)
    if months_count == 0:
        continue
    # monthly contribution amount (assume $1 per month)
    contrib = 1.0
    shares_bought = (contrib / first_trades['CloseUSD']).sum()
    final_price = g['CloseUSD'].iloc[-1]
    final_value = shares_bought * final_price
    total_invested = months_count * contrib
    # return factor (multiple of invested capital)
    return_factor = final_value / total_invested if total_invested > 0 else None
    results.append({
        'Index': idx,
        'months_invested': months_count,
        'total_invested': total_invested,
        'final_value': final_value,
        'return_factor': return_factor,
        'start_date': g['Date'].iloc[0].strftime('%Y-%m-%d'),
        'end_date': g['Date'].iloc[-1].strftime('%Y-%m-%d')
    })

# sort by return_factor desc
results_sorted = sorted([r for r in results if r['return_factor'] is not None], key=lambda x: x['return_factor'], reverse=True)
top5 = results_sorted[:5]

# map indices to countries (inferred)
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'TWII': 'Taiwan',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GSPTSE': 'Canada',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'N100': 'Netherlands/Europe',
    'J203.JO': 'South Africa',
    'NSEI': 'India'
}

final_list = []
for r in top5:
    idx = r['Index']
    country = country_map.get(idx, 'Unknown')
    final_list.append({
        'Index': idx,
        'Country': country,
        'months_invested': r['months_invested'],
        'total_invested': round(r['total_invested'], 2),
        'final_value': round(r['final_value'], 2),
        'return_factor': round(r['return_factor'], 4),
        'start_date': r['start_date'],
        'end_date': r['end_date']
    })

output = json.dumps(final_list)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_9NZzpj7uSadDYNR3J3B8iVCe': [{'Index': 'J203.JO', 'start_date': '01 Apr 2016, 00:00', 'end_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'N225', 'start_date': '01 Apr 1971, 00:00', 'end_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'GSPTSE', 'start_date': '01 Apr 1981, 00:00', 'end_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'NSEI', 'start_date': '01 Apr 2014, 00:00', 'end_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'GDAXI', 'start_date': '01 Apr 1992, 00:00', 'end_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'start_date': '01 Apr 1992, 00:00', 'end_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'IXIC', 'start_date': '01 Apr 1974, 00:00', 'end_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'NYA', 'start_date': '01 Apr 1969, 00:00', 'end_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'start_date': '01 Apr 2003, 00:00', 'end_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'SSMI', 'start_date': '01 Apr 1996, 00:00', 'end_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'start_date': '01 Apr 2004, 00:00', 'end_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N100', 'start_date': '01 Apr 2003, 00:00', 'end_date': 'September 30, 2019 at 12:00 AM'}, {'Index': '399001.SZ', 'start_date': '01 Apr 2004, 00:00', 'end_date': 'September 30, 2015 at 12:00 AM'}], 'var_call_O0sNfYwWWnfN6tfD51SZOon6': 'file_storage/call_O0sNfYwWWnfN6tfD51SZOon6.json'}

exec(code, env_args)

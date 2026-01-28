code = """import json
import pandas as pd

# Load the monthly data file from storage
path = var_call_Iq339CCDNt9nvLswoOgJpgEN
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)
# Ensure correct types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# parse dates safely
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', infer_datetime_format=True)

# For each index, simulate $1 monthly investment at each month's CloseUSD
results = []
for idx, g in df.groupby('idx'):
    g = g.sort_values('Date')
    # Only include months from 2000-01-01 onward (data already filtered)
    # Consider months where CloseUSD is positive
    g = g[g['CloseUSD'] > 0]
    # drop rows with NaT dates
    g = g[~g['Date'].isna()]
    if g.empty:
        continue
    months = len(g)
    contributions = months * 1.0
    # Shares bought each month = 1 / CloseUSD
    g = g.copy()
    g['shares'] = 1.0 / g['CloseUSD']
    total_shares = g['shares'].sum()
    last_price = g.iloc[-1]['CloseUSD']
    final_value = total_shares * last_price
    if contributions == 0:
        continue
    return_factor = final_value / contributions
    total_return_pct = (final_value - contributions) / contributions * 100.0
    results.append({
        'Index': idx,
        'Months': int(months),
        'Contributed_USD': round(contributions, 4),
        'Final_Value_USD': round(float(final_value), 4),
        'Return_Factor': round(float(return_factor), 6),
        'Total_Return_pct': round(float(total_return_pct), 2)
    })

# Sort by return factor descending
results_sorted = sorted(results, key=lambda x: x['Return_Factor'], reverse=True)
# Keep top 5
top5 = results_sorted[:5]

# Map indices to countries using knowledge-based mapping
mapping = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'NYA': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands',
    '399001.SZ': 'China'
}

out = []
for r in top5:
    country = mapping.get(r['Index'], 'Unknown')
    out.append({
        'Index': r['Index'],
        'Country': country,
        'Total_Return_Factor': r['Return_Factor'],
        'Total_Return_%': r['Total_Return_pct'],
        'Final_Value_USD': r['Final_Value_USD'],
        'Total_Contributed_USD': r['Contributed_USD'],
        'Months': r['Months']
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_oG7GGGtBKqLngxBBYEp8kLmU': ['index_trade'], 'var_call_1GM68aTkhLcTvW1ZJWjMz6Tm': [{'idx': 'J203.JO'}, {'idx': 'N225'}, {'idx': 'GSPTSE'}, {'idx': 'NSEI'}, {'idx': 'GDAXI'}, {'idx': 'IXIC'}, {'idx': 'NYA'}, {'idx': 'HSI'}, {'idx': '000001.SS'}, {'idx': 'SSMI'}, {'idx': 'TWII'}, {'idx': 'N100'}, {'idx': '399001.SZ'}], 'var_call_Iq339CCDNt9nvLswoOgJpgEN': 'file_storage/call_Iq339CCDNt9nvLswoOgJpgEN.json'}

exec(code, env_args)

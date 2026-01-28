code = """import pandas as pd
import json
from datetime import datetime

# Load the large query result from storage path variable
path = var_call_Xy0U1Xmzm5NHHhUGP3sRjuHN
with open(path, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Ensure types
df['Date'] = pd.to_datetime(df['Date'])
# Some CloseUSD may be strings; convert
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter to dates >= 2000-01-01 just in case
df = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# Map index symbols to countries/exchanges using knowledge
index_country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong (China)',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Euronext (Europe)',
    'J203.JO': 'South Africa'
}

results = []
for idx, group in df.groupby('Index'):
    g = group.sort_values('Date').copy()
    # Determine first trading day in each month
    g['year_month'] = g['Date'].dt.to_period('M')
    first_days = g.groupby('year_month').first().reset_index()
    # Invest $1 at each month's first available close price
    first_days = first_days[first_days['CloseUSD'].notna()]
    if first_days.empty:
        continue
    investments = 1.0  # $1 per month
    shares_bought = (investments / first_days['CloseUSD']).sum()
    # Final price: use last available CloseUSD for that index
    final_price = g['CloseUSD'].dropna().iloc[-1]
    final_value = shares_bought * final_price
    total_invested = investments * len(first_days)
    return_ratio = final_value / total_invested if total_invested>0 else None
    results.append({
        'Index': idx,
        'Country': index_country_map.get(idx, 'Unknown'),
        'months_invested': int(len(first_days)),
        'total_invested_usd': round(total_invested,6),
        'final_value_usd': round(float(final_value),6),
        'return_ratio': round(float(return_ratio),6)
    })

# Sort by return_ratio descending
results_sorted = sorted(results, key=lambda x: x['return_ratio'], reverse=True)
# Take top 5
top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_EWciS2c8L5V5VuLqxe8H8XP6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_Xy0U1Xmzm5NHHhUGP3sRjuHN': 'file_storage/call_Xy0U1Xmzm5NHHhUGP3sRjuHN.json', 'var_call_z7eJ6ngynBekR6C4CTWk8naC': ['index_info'], 'var_call_kTuHXBlYI3D5v5nPH0iS7vt4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

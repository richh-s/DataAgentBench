code = """import pandas as pd
import json

# Load the large query result from storage
path = var_call_Jm9PstBK3KWAMYrcN8eQngz7
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Convert types
df['Date'] = pd.to_datetime(df['Date'])
# Some CloseUSD might be strings; convert to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter to dates >= 2000-01-01 just in case
df = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# month period
df['year_month'] = df['Date'].dt.to_period('M')

# Get first trading day per month per index
df_sorted = df.sort_values(['Index', 'Date'])
monthly_first = df_sorted.groupby(['Index', 'year_month'], as_index=False).first()

results = []

# mapping index -> country
country_map = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Euronext (Europe)',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

for idx, grp in monthly_first.groupby('Index'):
    months_invested = len(grp)
    if months_invested == 0:
        continue
    # invest $1 each month on the first trading day's CloseUSD
    # avoid zero or NaN prices
    grp = grp.dropna(subset=['CloseUSD'])
    if len(grp) == 0:
        continue
    shares_bought = (1.0 / grp['CloseUSD']).sum()
    # final price = last available CloseUSD for this index
    final_row = df_sorted[df_sorted['Index'] == idx].dropna(subset=['CloseUSD']).iloc[-1]
    final_price = float(final_row['CloseUSD'])
    final_date = final_row['Date'].strftime('%Y-%m-%d')
    final_value = shares_bought * final_price
    total_invested = months_invested * 1.0
    multiple = final_value / total_invested if total_invested != 0 else None
    results.append({
        'Index': idx,
        'country': country_map.get(idx, 'Unknown'),
        'months_invested': months_invested,
        'total_invested': total_invested,
        'final_date': final_date,
        'final_value': round(float(final_value), 6),
        'multiple': round(float(multiple), 6)
    })

# Sort by multiple descending
results_sorted = sorted(results, key=lambda x: x['multiple'] if x['multiple'] is not None else -999, reverse=True)

top5 = results_sorted[:5]

# Prepare JSON string
out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Jm9PstBK3KWAMYrcN8eQngz7': 'file_storage/call_Jm9PstBK3KWAMYrcN8eQngz7.json', 'var_call_erHwVmsvGIaVs49c3kAXkwnk': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_dPKuKDfcsKLcHqimovC2Jpw3': ['index_info'], 'var_call_jd3RpYBJY0gUdxMa7wvggvZ6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

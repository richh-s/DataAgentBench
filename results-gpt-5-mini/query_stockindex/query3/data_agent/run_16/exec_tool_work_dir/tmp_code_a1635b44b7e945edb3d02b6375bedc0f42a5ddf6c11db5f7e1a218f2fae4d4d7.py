code = """import json
import pandas as pd
from pathlib import Path

# Load the large query result from storage variable
data_path = Path(var_call_4NJeogCD9g5qnkgMJMXBiW8H)
with open(data_path, 'r') as f:
    records = json.load(f)

# Build DataFrame
df = pd.DataFrame(records)
# Parse Date safely
df['Date'] = pd.to_datetime(df.get('Date'), errors='coerce')
# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df.get('CloseUSD'), errors='coerce')
# Drop rows without Date or CloseUSD
df = df.dropna(subset=['Date', 'CloseUSD']).copy()
# Filter from 2000-01-01
df = df[df['Date'] >= pd.to_datetime('2000-01-01')].copy()

# Create year-month period
df['period'] = df['Date'].dt.to_period('M')

results = []

# Manual mapping from index symbol to country (inferred)
index_country = {
    'J203.JO': 'South Africa',
    'IXIC': 'United States',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'NYA': 'United States',
    'N100': 'Euronext (Europe)',
    '399001.SZ': 'China'
}

for idx, group in df.groupby('Index'):
    g = group.sort_values('Date')
    # First trading day each month -> keep first row per period
    firsts = g.drop_duplicates(subset=['period'], keep='first')
    months = len(firsts)
    if months == 0:
        continue
    # Invest $1 each month -> shares purchased each month
    shares_each = (1.0 / firsts['CloseUSD']).sum()
    # Final price = last available CloseUSD for this index
    last_row = g.loc[g['Date'].idxmax()]
    last_price = last_row['CloseUSD']
    final_value = shares_each * last_price
    invested = months * 1.0
    return_ratio = final_value / invested if invested != 0 else None
    return_pct = (final_value - invested) / invested * 100 if invested != 0 else None
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, None),
        'MonthsInvested': int(months),
        'Invested': round(invested, 2),
        'FinalValue': round(float(final_value), 6),
        'ReturnRatio': round(float(return_ratio), 6) if return_ratio is not None else None,
        'ReturnPercent': round(float(return_pct), 2) if return_pct is not None else None
    })

# Sort by ReturnRatio desc and take top 5
results_sorted = sorted(results, key=lambda x: (x['ReturnRatio'] if x['ReturnRatio'] is not None else -9999), reverse=True)
top5 = results_sorted[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_VBzFvPTfGokuwTkYBPYdW1oh': ['index_trade'], 'var_call_T3ezKguFTKXziw19cpQ5p2KL': ['index_info'], 'var_call_k1fyNmq1x5GGwk3UbcXiE8w5': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_BizVkTlSGj95pA92IYDGDDit': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_4NJeogCD9g5qnkgMJMXBiW8H': 'file_storage/call_4NJeogCD9g5qnkgMJMXBiW8H.json'}

exec(code, env_args)

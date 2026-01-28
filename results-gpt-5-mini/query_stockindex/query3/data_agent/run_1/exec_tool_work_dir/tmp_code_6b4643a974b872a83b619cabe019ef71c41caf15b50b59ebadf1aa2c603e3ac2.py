code = """import json
import pandas as pd

# Load the large query result from the provided file path variable
fp = var_call_3Wq7PB0nciGeUWzgAoqEv9JC
with open(fp, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure types
df['Date'] = pd.to_datetime(df['Date'])
# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter from 2000-01 onwards
df = df[df['Date'] >= pd.Timestamp('2000-01-01')].copy()

# Prepare mapping from index symbol to country (based on common index knowledge and the index_info table)
index_country = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'HSI': 'Hong Kong',
    'IXIC': 'United States',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Netherlands',
    '399001.SZ': 'China'
}

results = []
for idx, grp in df.groupby('Index'):
    g = grp.sort_values('Date').copy()
    if g.empty:
        continue
    g['YearMonth'] = g['Date'].dt.to_period('M')
    # first trading day of each month
    monthly_first = g.sort_values('Date').groupby('YearMonth', as_index=False).first()
    # keep months from 2000-01 onwards
    monthly_first = monthly_first[monthly_first['YearMonth'] >= pd.Period('2000-01')]
    months = len(monthly_first)
    if months == 0:
        continue
    # contribute $1 per month
    contributions = months * 1.0
    # shares purchased each month
    monthly_first = monthly_first[monthly_first['CloseUSD'] > 0]
    shares = (1.0 / monthly_first['CloseUSD']).sum()
    # final price = last available CloseUSD for that index
    final_price = g.sort_values('Date', ascending=False).iloc[0]['CloseUSD']
    final_value = shares * final_price
    return_multiplier = final_value / contributions if contributions > 0 else None
    return_pct = (final_value - contributions) / contributions * 100.0 if contributions > 0 else None
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, 'Unknown'),
        'MonthsInvested': int(months),
        'TotalContributedUSD': round(contributions, 2),
        'FinalValueUSD': round(float(final_value), 2),
        'ReturnPct': round(float(return_pct), 2),
        'ReturnMultiplier': round(float(return_multiplier), 4)
    })

# pick top 5 by ReturnMultiplier
res_df = pd.DataFrame(results).sort_values('ReturnMultiplier', ascending=False).head(5)
out = res_df.to_dict(orient='records')

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_8D88pE5beN83xswrYf3l65yU': ['index_trade'], 'var_call_3ktx5mEb86dlh4ud1m9swEUk': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_QXQyiyMiXmHYrbQwhQzXA9iD': ['index_info'], 'var_call_RYyQQMSMAVFp1KRu1twNcccO': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_3Wq7PB0nciGeUWzgAoqEv9JC': 'file_storage/call_3Wq7PB0nciGeUWzgAoqEv9JC.json'}

exec(code, env_args)

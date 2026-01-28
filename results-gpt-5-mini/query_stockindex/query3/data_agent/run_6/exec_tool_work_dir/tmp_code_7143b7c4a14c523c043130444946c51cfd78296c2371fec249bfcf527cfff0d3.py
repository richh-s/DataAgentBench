code = """import json
import pandas as pd

# Load monthly data from the query result file path stored in var_call_ZU044jQ4W6u56fjDY1Vkjuar
path = var_call_ZU044jQ4W6u56fjDY1Vkjuar
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Sort
df = df.sort_values(['Index','ym'])

# Mapping of index symbols to countries (based on common knowledge / hints)
country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong (China)',
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'IXIC': 'United States',
    'NYA': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands'
}

results = []
for idx, g in df.groupby('Index'):
    g = g.dropna(subset=['CloseUSD']).copy()
    months = len(g)
    if months == 0:
        continue
    last_price = float(g['CloseUSD'].iloc[-1])
    # Avoid division by zero
    g = g[g['CloseUSD'] > 0]
    if len(g) == 0:
        continue
    sum_shares = (1.0 / g['CloseUSD']).sum()
    final_value = last_price * sum_shares
    multiplier = final_value / months  # final value per $1 invested monthly
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'MonthsInvested': months,
        'FinalValueUSD': round(float(final_value), 6),
        'ReturnPerDollarInvested': round(float(multiplier), 6)
    })

# Sort by ReturnPerDollarInvested descending and take top 5
results_sorted = sorted(results, key=lambda x: x['ReturnPerDollarInvested'], reverse=True)
top5 = results_sorted[:5]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_ZU044jQ4W6u56fjDY1Vkjuar': 'file_storage/call_ZU044jQ4W6u56fjDY1Vkjuar.json', 'var_call_MXPcDzDKc0wYSwXYmF5rbixE': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_nC7DrQCkCRrQALc54gewtLqk': ['index_info'], 'var_call_m6TNluBYYoZCbWXNlrH4Gs22': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

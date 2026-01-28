code = """import pandas as pd
import json
path = var_call_eetEPnjnx9N4TUl9PTLlLsRS
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Robust date parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# Convert CloseUSD
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Drop rows with invalid dates or CloseUSD
df = df.dropna(subset=['Date', 'CloseUSD']).copy()
# Sort
df = df.sort_values(['Index', 'Date']).reset_index(drop=True)
# YearMonth
df['YearMonth'] = df['Date'].dt.to_period('M')
# First trading day per month per index
first_days = df.groupby(['Index', 'YearMonth'], as_index=False).first()
# Filter positive prices
first_days = first_days[first_days['CloseUSD'] > 0].copy()
first_days['shares'] = 1.0 / first_days['CloseUSD']
# Aggregate
agg = first_days.groupby('Index', as_index=False).agg(
    months_invested=('YearMonth', 'count'),
    total_shares=('shares', 'sum')
)
# Last close per index
last_close = df.groupby('Index', as_index=False).last()[['Index', 'CloseUSD']]
agg = agg.merge(last_close, on='Index', how='left')
agg['final_value'] = agg['total_shares'] * agg['CloseUSD']
agg['total_invested'] = agg['months_invested'] * 1.0
agg['return_multiplier'] = agg['final_value'] / agg['total_invested']

mapping = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    'IXIC': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe',
    '399001.SZ': 'China'
}
agg['country'] = agg['Index'].map(mapping).fillna('Unknown')
# Top 5 by return multiplier? The user asked highest overall returns — interpret as final value per $ invested (multiplier) or absolute final value? Clarify: we'll use return multiplier (final_value / total invested)
# But instruction earlier computed top5 by final_value. User asked "which 5 indices would have produced the highest overall returns" - we'll use return multiplier to reflect returns per invested dollar.
top5 = agg.sort_values('return_multiplier', ascending=False).head(5)

out = []
for _, r in top5.iterrows():
    out.append({
        'Index': str(r['Index']),
        'Country': str(r['country']),
        'ReturnMultiplier': round(float(r['return_multiplier']), 4) if pd.notnull(r['return_multiplier']) else None,
        'FinalValue': round(float(r['final_value']), 2) if pd.notnull(r['final_value']) else None,
        'MonthsInvested': int(r['months_invested'])
    })

result_json = json.dumps(out)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_ehUdlbmbRjffsIAoV9wiqDX0': ['index_trade'], 'var_call_s9HK2nlzfQ8fnMC7dGT4K1r0': ['index_info'], 'var_call_NI4d7Q2XpQ1CShEWmjwvkCiL': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_jVLmKsq4EAbRrB5ZwDq9cPbu': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_eetEPnjnx9N4TUl9PTLlLsRS': 'file_storage/call_eetEPnjnx9N4TUl9PTLlLsRS.json'}

exec(code, env_args)

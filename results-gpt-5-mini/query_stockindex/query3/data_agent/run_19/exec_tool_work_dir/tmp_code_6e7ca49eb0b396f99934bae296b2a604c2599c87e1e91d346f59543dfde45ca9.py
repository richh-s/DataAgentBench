code = """import pandas as pd
import json
# Load the large query result from provided storage path
path = var_call_eetEPnjnx9N4TUl9PTLlLsRS
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Ensure proper types
df['Date'] = pd.to_datetime(df['Date'])
# Some CloseUSD may be strings, convert
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Sort
df = df.sort_values(['Index', 'Date']).reset_index(drop=True)
# Consider first trading day of each month for monthly investments
df['YearMonth'] = df['Date'].dt.to_period('M')
first_days = df.groupby(['Index', 'YearMonth'], as_index=False).first()
# Invest $1 each month at that month's first trading day's CloseUSD
first_days = first_days[first_days['CloseUSD'] > 0].copy()
first_days['shares'] = 1.0 / first_days['CloseUSD']
# Aggregate per index
agg = first_days.groupby('Index', as_index=False).agg(
    months_invested=('YearMonth', 'count'),
    total_shares=('shares', 'sum')
)
# Get last available CloseUSD per index to value holdings
last_close = df.groupby('Index', as_index=False).last()[['Index', 'CloseUSD']]
agg = agg.merge(last_close, on='Index', how='left')
agg['final_value'] = agg['total_shares'] * agg['CloseUSD']
agg['total_invested'] = agg['months_invested'] * 1.0
agg['return_multiplier'] = agg['final_value'] / agg['total_invested']

# Map indices to countries based on known mappings
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
# Select top 5 by final_value
top5 = agg.sort_values('final_value', ascending=False).head(5)
# Prepare output
out = []
for _, r in top5.iterrows():
    out.append({
        'Index': str(r['Index']),
        'Country': str(r['country']),
        'FinalValue': round(float(r['final_value']), 2),
        'TotalInvested': round(float(r['total_invested']), 2),
        'MonthsInvested': int(r['months_invested']),
        'ReturnMultiplier': round(float(r['return_multiplier']), 4)
    })

print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print('print(' + json.dumps(out) + ')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_ehUdlbmbRjffsIAoV9wiqDX0': ['index_trade'], 'var_call_s9HK2nlzfQ8fnMC7dGT4K1r0': ['index_info'], 'var_call_NI4d7Q2XpQ1CShEWmjwvkCiL': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_jVLmKsq4EAbRrB5ZwDq9cPbu': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_eetEPnjnx9N4TUl9PTLlLsRS': 'file_storage/call_eetEPnjnx9N4TUl9PTLlLsRS.json'}

exec(code, env_args)

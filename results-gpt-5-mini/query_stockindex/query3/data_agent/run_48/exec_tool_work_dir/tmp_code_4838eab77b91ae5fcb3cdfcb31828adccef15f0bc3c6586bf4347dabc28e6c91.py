code = """import json
import pandas as pd

# Load the large query result from storage
path = var_call_MfZKUzcWdIGTTYTJGOimrIPy
with open(path, 'r') as f:
    records = json.load(f)

# Create DataFrame
df = pd.DataFrame(records)
# Convert types
df['Date'] = pd.to_datetime(df['Date'])
# Some CloseUSD may be strings; convert, coerce errors
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Mapping of index symbols to countries (inferred)
index_country = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

results = []
for idx, grp in df.groupby('Index'):
    g = grp.sort_values('Date').copy()
    if g.empty:
        continue
    # Determine first trading day of each month present
    g['year_month'] = g['Date'].dt.to_period('M')
    first_days = g.groupby('year_month').first().reset_index()
    # Only include months from 2000-01 onwards (data already filtered)
    # Assume investing $1 on the first trading day of each month present
    invest_amount = 1.0
    shares = 0.0
    months_invested = 0
    for _, row in first_days.iterrows():
        price = row['CloseUSD']
        if pd.isna(price) or price <= 0:
            continue
        shares += invest_amount / price
        months_invested += 1
    if months_invested == 0:
        continue
    last_price = g.iloc[-1]['CloseUSD']
    if pd.isna(last_price) or last_price <= 0:
        continue
    final_value = shares * last_price
    total_invested = months_invested * invest_amount
    multiple = final_value / total_invested
    results.append({
        'Index': idx,
        'Country': index_country.get(idx, 'Unknown'),
        'MonthsInvested': months_invested,
        'FinalValue': final_value,
        'TotalInvested': total_invested,
        'Multiple': multiple
    })

# Sort by Multiple descending and take top 5
results_sorted = sorted(results, key=lambda x: x['Multiple'], reverse=True)
top5 = results_sorted[:5]
# Round numeric fields for readability
for r in top5:
    r['FinalValue'] = round(r['FinalValue'], 4)
    r['TotalInvested'] = round(r['TotalInvested'], 4)
    r['Multiple'] = round(r['Multiple'], 4)

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_fH0hHjMphJqB9QXdbnez61xF': ['index_trade'], 'var_call_CMTxKgKoWIQ3Ao2yyOou1T0Q': ['index_info'], 'var_call_EqluSvX4FnnWjOsQbrPhDkFe': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_MfZKUzcWdIGTTYTJGOimrIPy': 'file_storage/call_MfZKUzcWdIGTTYTJGOimrIPy.json'}

exec(code, env_args)

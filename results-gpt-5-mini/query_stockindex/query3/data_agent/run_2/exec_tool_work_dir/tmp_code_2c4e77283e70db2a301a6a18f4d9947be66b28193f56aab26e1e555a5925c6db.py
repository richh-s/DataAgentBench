code = """import pandas as pd
import json
from datetime import datetime

# Load the query result from storage
data_path = var_call_6AU4tO7m8exrSnnNB3NfS9Zg
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Ensure types
df['Date'] = pd.to_datetime(df['Date'])
# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
# Filter from 2000-01-01
df = df[df['Date'] >= pd.to_datetime('2000-01-01')]

# Mapping of index symbols to countries (inferred from common index names)
country_map = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    'N100': 'Netherlands',
    '399001.SZ': 'China',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

results = []
# For each index, compute monthly DCA with $1 per month on the first trading day of each month
for idx, g in df.groupby('Index'):
    gg = g.sort_values('Date').copy()
    if gg['CloseUSD'].isna().all():
        continue
    # resample by month: pick first trading day of each month available
    gg['year_month'] = gg['Date'].dt.to_period('M')
    first_days = gg.groupby('year_month').first().reset_index()
    # exclude months before 2000-01 if any (we already filtered)
    # exclude entries with non-positive or NaN CloseUSD
    first_days = first_days[first_days['CloseUSD'] > 0]
    months_invested = len(first_days)
    if months_invested == 0:
        continue
    # invest $1 each month
    first_days['units'] = 1.0 / first_days['CloseUSD']
    total_units = first_days['units'].sum()
    # final price = last available CloseUSD for that index
    last_price = gg.loc[gg['Date'].idxmax(), 'CloseUSD']
    final_value = total_units * last_price
    total_invested = months_invested * 1.0
    factor = final_value / total_invested
    pct_return = (final_value - total_invested) / total_invested * 100.0
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'MonthsInvested': months_invested,
        'FinalValuePerDollarInvested': factor,
        'TotalReturnPercent': pct_return
    })

# Sort and take top 5 by FinalValuePerDollarInvested
results_sorted = sorted(results, key=lambda x: x['FinalValuePerDollarInvested'], reverse=True)
top5 = results_sorted[:5]

# Prepare printable JSON
output = json.dumps(top5)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_sBKtm2u1440dTFHyVK9JLZyh': ['index_trade'], 'var_call_rYeoZR27ABOg1SwhQBenKe4V': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_nyo1qnWBb7bz0A4WBccEr4lg': ['index_info'], 'var_call_6AU4tO7m8exrSnnNB3NfS9Zg': 'file_storage/call_6AU4tO7m8exrSnnNB3NfS9Zg.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Load the large query result from file path stored in var_call_GD88nZrO2F8X0CmVtoBosBaU
with open(var_call_GD88nZrO2F8X0CmVtoBosBaU, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# Convert types
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])

results = []
for idx, group in df.groupby('Index'):
    g = group.sort_values('Date').copy()
    # consider months from 2000-01 onward
    g = g[g['Date'] >= pd.Timestamp('2000-01-01')]
    if g.empty:
        continue
    # first trading day of each month: group by period
    g['Month'] = g['Date'].dt.to_period('M')
    first_days = g.groupby('Month')['Date'].min().reset_index()
    # merge to get prices on those first trading days
    first_prices = pd.merge(first_days, g[['Date', 'CloseUSD']], on='Date', how='left')
    # For each month buy $1 worth at CloseUSD
    first_prices = first_prices.dropna(subset=['CloseUSD'])
    first_prices['Shares'] = 1.0 / first_prices['CloseUSD']
    total_shares = first_prices['Shares'].sum()
    months = len(first_prices)
    total_invested = float(months * 1.0)
    last_price = float(g.sort_values('Date').iloc[-1]['CloseUSD'])
    final_value = total_shares * last_price
    return_factor = final_value / total_invested if total_invested > 0 else None
    results.append({
        'Index': idx,
        'MonthsInvested': months,
        'TotalInvestedUSD': round(total_invested,6),
        'FinalValueUSD': round(final_value,6),
        'ReturnFactor': round(return_factor,6)
    })

# sort by ReturnFactor descending and take top 5
results_sorted = sorted(results, key=lambda x: x['ReturnFactor'] if x['ReturnFactor'] is not None else -999, reverse=True)
top5 = results_sorted[:5]

# mapping of indices to countries (inferred)
mapping = {
    '000001.SS': 'China (Shanghai)',
    '399001.SZ': 'China (Shenzhen)',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Netherlands (Euronext)',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

for r in top5:
    r['Country'] = mapping.get(r['Index'], 'Unknown')

# Prepare JSON string
output = json.dumps(top5)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_kJSHfvObhmOf58GZOKODpS9d': ['index_trade'], 'var_call_ZFvaSRHt0Z2IWqpJGaySXdN7': ['index_info'], 'var_call_GD88nZrO2F8X0CmVtoBosBaU': 'file_storage/call_GD88nZrO2F8X0CmVtoBosBaU.json', 'var_call_OVljXQhPLnuT4Dh4ZEKGH2Av': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_5FvZ85P86u66nCxdPCn4CiEe': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

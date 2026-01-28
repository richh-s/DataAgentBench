code = """import pandas as pd
import json

# Load the large query result file for index trades since 2000
path = var_call_9FHjEVTFp6CUcRnWXgc1OXN7
df = pd.read_json(path)

# Clean and prepare
df = df[['Index', 'Date', 'CloseUSD']].dropna()
# Convert types
df['Date'] = pd.to_datetime(df['Date'])
# Some CloseUSD are strings; convert to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

df = df.dropna(subset=['CloseUSD'])

# Monthly investment simulation: invest $1 on the first trading day of each month (earliest date in each month having data)
results = []
monthly_amount = 1.0

for idx, grp in df.groupby('Index'):
    grp = grp.sort_values('Date')
    grp['year_month'] = grp['Date'].dt.to_period('M')
    # get first trading day row for each month
    first_days = grp.loc[grp.groupby('year_month')['Date'].idxmin()]
    # Filter months starting from 2000-01 (data already restricted) but ensure year_month >= 2000-01
    first_days = first_days[first_days['year_month'] >= pd.Period('2000-01', freq='M')]
    months_invested = len(first_days)
    if months_invested == 0:
        continue
    # accumulate shares
    shares = (monthly_amount / first_days['CloseUSD']).sum()
    # final price = last available CloseUSD
    last_price = grp['CloseUSD'].iloc[-1]
    final_value = shares * last_price
    total_invested = monthly_amount * months_invested
    return_factor = final_value / total_invested
    results.append({
        'Index': idx,
        'months_invested': int(months_invested),
        'total_invested': float(total_invested),
        'final_value': float(final_value),
        'return_factor': float(return_factor)
    })

res_df = pd.DataFrame(results).sort_values('return_factor', ascending=False)

# Map indices to countries (inferred mapping)
mapping = {
    'IXIC': 'United States',
    'NYA': 'United States',
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Euronext (Europe)',
    'J203.JO': 'South Africa'
}

# Prepare top 5
top5 = []
for _, row in res_df.head(5).iterrows():
    idx = row['Index']
    country = mapping.get(idx, 'Unknown')
    top5.append({
        'Index': idx,
        'Country': country,
        'MonthsInvested': int(row['months_invested']),
        'TotalInvestedUSD': round(row['total_invested'], 2),
        'FinalValueUSD': round(row['final_value'], 2),
        'ReturnFactor': round(row['return_factor'], 4)
    })

output = {'top5': top5}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_GoNXOQYURcUvXk4BYhj6zlkN': ['index_trade'], 'var_call_3TJmNRurfccaLBR1UyLBcdLA': ['index_info'], 'var_call_9FHjEVTFp6CUcRnWXgc1OXN7': 'file_storage/call_9FHjEVTFp6CUcRnWXgc1OXN7.json', 'var_call_i8pW9iEVWftpjrEC9YxZuvpF': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_nYeMadOaZqpTfTv0emvfGeJJ': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}]}

exec(code, env_args)

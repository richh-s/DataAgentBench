code = """import json
import pandas as pd

# Get the data from storage
result_data = locals()['var_functions.query_db:8']

# Load from file path if needed
if isinstance(result_data, str):
    with open(result_data, 'r') as f:
        all_data = json.load(f)
else:
    all_data = result_data

# Process data
print('Loading price data...')

df_list = []
for record in all_data:
    try:
        df_list.append({
            'Index': record['Index'],
            'Date': str(record['Date']),
            'CloseUSD': float(record['CloseUSD'])
        })
    except:
        continue

df = pd.DataFrame(df_list)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()
print(f'Loaded {len(df)} records for {df["Index"].nunique()} indices')

# Get monthly data
monthly = df.groupby(['Index', pd.Grouper(key='Date', freq='M')]).agg({'CloseUSD': 'last'}).reset_index()
monthly = monthly[monthly['Date'] >= pd.to_datetime('2000-01-01')]
print(f'Monthly data: {len(monthly)} records from 2000 onwards')

# Calculate returns for monthly investments
results = []
for idx in monthly['Index'].unique():
    idx_data = monthly[monthly['Index'] == idx].sort_values('Date')
    if len(idx_data) < 12:
        continue
    
    total_invested = 0
    shares = 0
    for _, row in idx_data.iterrows():
        total_invested += 100
        shares += 100 / row['CloseUSD']
    
    final_value = shares * idx_data.iloc[-1]['CloseUSD']
    total_return = final_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    results.append({
        'Index': idx,
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Total_Return': round(total_return, 2),
        'Return_Percent': round(return_pct, 2)
    })

# Sort by return
top_indices = sorted(results, key=lambda x: x['Return_Percent'], reverse=True)[:5]

# Map to countries
index_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'IXIC': 'USA',
    'NYA': 'USA',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'N100': 'Netherlands',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

output = []
for i, item in enumerate(top_indices, 1):
    output.append({
        'Rank': i,
        'Index': item['Index'],
        'Country': index_country.get(item['Index'], 'Unknown'),
        'Return_Percent': item['Return_Percent']
    })

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

code = """import json, pandas as pd, numpy as np

file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna().sort_values(['Index', 'Date'])

country_map = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'HSI': 'Hong Kong',
    'N225': 'Japan',
    'GDAXI': 'Germany',
    'N100': 'Netherlands',
    'IXIC': 'USA',
    'NYA': 'USA',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

results = []
for index in df['Index'].unique():
    df_idx = df[df['Index'] == index].copy()
    df_idx = df_idx[df_idx['Date'] >= '2000-01-01']
    
    if len(df_idx) < 100:
        continue
    
    monthly_data = df_idx.groupby([df_idx['Date'].dt.year, df_idx['Date'].dt.month]).first()
    
    if len(monthly_data) < 12:
        continue
    
    monthly_investment = 100
    total_shares = sum(monthly_investment / price for price in monthly_data['CloseUSD'])
    total_invested = len(monthly_data) * monthly_investment
    current_price = df_idx['CloseUSD'].iloc[-1]
    current_value = total_shares * current_price
    total_return = current_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    results.append({
        'Index': index,
        'Country': country_map.get(index, 'Unknown'),
        'Return_Pct': return_pct,
        'Total_Return': total_return,
        'Total_Invested': total_invested,
        'Months': len(monthly_data)
    })

results_df = pd.DataFrame(results).sort_values('Return_Pct', ascending=False)

# Display analysis
print('Total indices analyzed:', len(results_df))
for _, row in results_df.head(5).iterrows():
    print(f"{row['Index']} ({row['Country']}): {row['Return_Pct']:.1f}% return over {row['Months']} months")

print('__RESULT__:')
print(results_df.head(5).to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['index_trade'], 'var_functions.list_db:2': ['index_info'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:20': {'count': 67948, 'indices': ['J203.JO', 'TWII', 'GSPTSE', 'NYA', 'GDAXI', 'HSI', 'N225', 'IXIC', 'NSEI', 'N100', '399001.SZ', 'SSMI', '000001.SS']}}

exec(code, env_args)

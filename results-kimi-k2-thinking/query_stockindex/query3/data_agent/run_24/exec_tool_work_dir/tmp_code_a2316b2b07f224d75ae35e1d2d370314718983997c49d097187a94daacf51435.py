code = """import json
import pandas as pd

# Load trade data
trade_info = locals()['var_functions.query_db:8']
if isinstance(trade_info, str):
    with open(trade_info, 'r') as file:
        trade_data = json.load(file)
else:
    trade_data = trade_info

df = pd.DataFrame(trade_data)

# Convert types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Country mapping for each index
index_country = {
    'N225': 'Japan', 'HSI': 'Hong Kong', '000001.SS': 'China', 
    '399001.SZ': 'China', 'GDAXI': 'Germany', 'IXIC': 'USA', 
    'NYA': 'USA', 'N100': 'Netherlands', 'NSEI': 'India', 
    'TWII': 'Taiwan', 'GSPTSE': 'Canada', 'J203.JO': 'South Africa', 
    'SSMI': 'Switzerland'
}

df['Country'] = df['Index'].map(index_country)
df_2000 = df[df['Date'] >= '2000-01-01'].copy()

# Calculate monthly investment returns
results = []
for idx in df_2000['Index'].unique():
    data = df_2000[df_2000['Index'] == idx].sort_values('Date')
    
    if len(data) < 100:
        continue
    
    # Monthly data (last trading day of each month)
    data['YearMonth'] = data['Date'].dt.to_period('M')
    monthly = data.groupby('YearMonth')['CloseUSD'].last().reset_index()
    
    # Dollar cost averaging: $100 monthly
    invested = 0
    shares = 0
    for _, row in monthly.iterrows():
        price = row['CloseUSD']
        if price > 0:
            shares += 100 / price
            invested += 100
    
    final_price = monthly['CloseUSD'].iloc[-1]
    final_value = shares * final_price
    roi = ((final_value - invested) / invested * 100) if invested > 0 else 0
    
    results.append({
        'Index': idx, 
        'Country': index_country.get(idx, 'Unknown'),
        'ROI': round(roi, 2),
        'Final_Value': round(final_value, 2),
        'Months': len(monthly)
    })

top5 = pd.DataFrame(results).sort_values('ROI', ascending=False).head(5)

print('__RESULT__:')
print(top5.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

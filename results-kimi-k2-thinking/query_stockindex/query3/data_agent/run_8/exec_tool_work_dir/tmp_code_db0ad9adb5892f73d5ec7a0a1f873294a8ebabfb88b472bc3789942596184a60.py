code = """import json
import pandas as pd
import numpy as np

# Read the full data from the file
file_path = locals()['var_functions.query_db:8'] if 'var_functions.query_db:8' in locals() else None
if file_path and isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
else:
    data = locals().get('var_functions.query_db:8', [])

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Date to datetime and other fields to numeric
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
for col in ['Close', 'CloseUSD']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Filter from 2000-01-01 onwards
df = df[df['Date'] >= '2000-01-01'].copy()

# Sort by Date
df = df.sort_values(['Index', 'Date'])

# Index to country mapping
index_to_country = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'IXIC': 'United States',
    'NYA': 'United States',
    'GDAXI': 'Germany',
    'N100': 'Netherlands',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa',
    'NSEI': 'India',
    'GSPTSE': 'Canada'
}

# DCA calculations
monthly_investment = 100
dca_results = []

for index in df['Index'].unique():
    index_data = df[df['Index'] == index].copy()
    index_data = index_data.set_index('Date')
    
    # Resample to monthly - take the first day of each month
    monthly_data = index_data.resample('M').first()
    
    if len(monthly_data) == 0:
        continue
    
    # Calculate DCA
    shares = 0
    total_invested = 0
    
    # Use CloseUSD if available, otherwise use Close
    price_col = 'CloseUSD' if not monthly_data['CloseUSD'].isna().all() else 'Close'
    
    for date, row in monthly_data.iterrows():
        price = row[price_col]
        if pd.isna(price) or price <= 0:
            continue
            
        shares += monthly_investment / price
        total_invested += monthly_investment
    
    if total_invested == 0:
        continue
    
    # Final portfolio value
    final_price = index_data.iloc[-1][price_col]
    final_value = shares * final_price
    total_return = final_value - total_invested
    return_percentage = (total_return / total_invested) * 100
    
    # Annualized return (approximate)
    years = (index_data.index[-1] - index_data.index[0]).days / 365.25
    if years > 0:
        annualized_return = ((final_value / total_invested) ** (1 / years) - 1) * 100
    else:
        annualized_return = 0
    
    dca_results.append({
        'Index': index,
        'Country': index_to_country.get(index, 'Unknown'),
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return': total_return,
        'Return_Percentage': return_percentage,
        'Years': years,
        'Annualized_Return': annualized_return,
        'Months': len(monthly_data),
        'Shares': shares
    })

# Sort by total return and get top 5
dca_results.sort(key=lambda x: x['Return_Percentage'], reverse=True)
top_5 = dca_results[:5]

# Prepare output
output = {
    'top_5_indices': top_5,
    'all_results': sorted(dca_results, key=lambda x: x['Return_Percentage'], reverse=True)
}

print('__RESULT__:')
print(json.dumps(output, default=str))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'status': 'Data loaded successfully', 'total_records': 21342, 'num_indices': 13, 'indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII'], 'date_range': {'start': '2000-01-03 00:00:00', 'end': '2021-06-02 00:00:00'}}}

exec(code, env_args)

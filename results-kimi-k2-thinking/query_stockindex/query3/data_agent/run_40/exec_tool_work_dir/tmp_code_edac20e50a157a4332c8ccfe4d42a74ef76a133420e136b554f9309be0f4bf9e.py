code = """import json
import pandas as pd

# Load data
price_data_file = locals()['var_functions.query_db:8']
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Data cleaning
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()

# Filter from 2000 onwards
df = df[df['Date'] >= '2000-01-01']

# Map exchanges to countries (based on standard financial knowledge)
exchange_countries = {
    '000001.SS': 'China',
    '399001.SZ': 'China', 
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'IXIC': 'United States',
    'J203.JO': 'South Africa',
    'N100': 'Euronext',
    'N225': 'Japan',
    'NSEI': 'India',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan'
}

# Calculate DCA returns for each index
dca_results = []
monthly_amount = 100  # Fixed monthly investment amount

for index in df['Index'].unique():
    index_data = df[df['Index'] == index].copy()
    
    # Ensure data is sorted by date
    index_data = index_data.sort_values('Date')
    
    # Get first trading day of each month
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    monthly_prices = index_data.groupby('YearMonth').first().reset_index()
    
    # Only start from months that have data
    if len(monthly_prices) < 12:
        continue
    
    # Calculate DCA
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_prices.iterrows():
        price = row['CloseUSD']
        if price > 0:
            total_invested += monthly_amount
            total_shares += monthly_amount / price
    
    # Get final value
    if len(index_data) > 0:
        final_price = index_data.iloc[-1]['CloseUSD']
        final_value = total_shares * final_price
        total_return = final_value - total_invested
        return_percentage = (total_return / total_invested) * 100 if total_invested > 0 else 0
        
        dca_results.append({
            'Index': index,
            'Country': exchange_countries.get(index, 'Unknown'),
            'Total_Invested': total_invested,
            'Final_Value': final_value,
            'Total_Return': total_return,
            'Return_Percentage': return_percentage,
            'Months_Invested': len(monthly_prices)
        })

# Sort by return percentage
dca_results = sorted(dca_results, key=lambda x: x['Return_Percentage'], reverse=True)

top_5 = dca_results[:5]

print('__RESULT__:')
print(json.dumps({
    'top_5_indices': top_5,
    'all_results': dca_results
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:7': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}, {'Index': 'IXIC'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': {'variables': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:7', 'var_functions.query_db:8', '__builtins__', 'json']}, 'var_functions.execute_python:28': {'status': 'success', 'message': 'Data loaded: 21342 records from 2000-01-03 00:00:00 to 2021-06-02 00:00:00', 'indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)

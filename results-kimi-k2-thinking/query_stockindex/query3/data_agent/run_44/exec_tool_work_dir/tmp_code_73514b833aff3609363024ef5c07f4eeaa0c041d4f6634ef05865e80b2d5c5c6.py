code = """import json
import pandas as pd

# Get the stored result from previous query
storage_key = 'var_functions.query_db:8'
result_data = globals().get(storage_key) or locals().get(storage_key)

if isinstance(result_data, str) and result_data.endswith('.json'):
    with open(result_data, 'r') as f:
        data = json.load(f)
else:
    data = result_data

# Convert to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['Date', 'CloseUSD'])

# Index to country mapping
index_country_map = {
    'N225': 'Japan', 'HSI': 'Hong Kong', '000001.SS': 'China',
    '399001.SZ': 'China', 'NYA': 'United States', 'IXIC': 'United States',
    'GDAXI': 'Germany', 'GSPTSE': 'Canada', 'SSMI': 'Switzerland',
    'NSEI': 'India', 'J203.JO': 'South Africa', 'TWII': 'Taiwan', 'N100': 'Europe'
}

# Index to full name mapping
index_name_map = {
    'N225': 'Nikkei 225',
    'HSI': 'Hang Seng Index',
    '000001.SS': 'Shanghai Composite',
    '399001.SZ': 'Shenzhen Component Index',
    'NYA': 'NYSE Composite',
    'IXIC': 'NASDAQ Composite',
    'GDAXI': 'DAX',
    'GSPTSE': 'S&P/TSX Composite',
    'SSMI': 'Swiss Market Index',
    'NSEI': 'Nifty 50',
    'J203.JO': 'FTSE/JSE All Share Index',
    'TWII': 'Taiwan Weighted Index',
    'N100': 'Euronext 100'
}

# Calculate DCA returns for all indices
monthly_investment = 100
all_results = []

for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx].copy()
    idx_data = idx_data[idx_data['Date'] >= pd.Timestamp('2000-01-01')]
    
    if idx_data.empty: continue
    
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly = idx_data.groupby('YearMonth')['CloseUSD'].first().reset_index()
    monthly['Date'] = monthly['YearMonth'].dt.to_timestamp()
    monthly = monthly.sort_values('Date')
    
    if monthly.empty: continue
    
    monthly['Units'] = monthly_investment / monthly['CloseUSD']
    monthly['Total_Units'] = monthly['Units'].cumsum()
    monthly['Total_Invested'] = monthly_investment * (monthly.index + 1)
    
    final_value = monthly['Total_Units'].iloc[-1] * monthly['CloseUSD'].iloc[-1]
    total_invested = monthly['Total_Invested'].iloc[-1]
    total_return = final_value - total_invested
    return_pct = ((final_value - total_invested) / total_invested) * 100
    
    # Get first and last prices
    first_price = monthly['CloseUSD'].iloc[0]
    last_price = monthly['CloseUSD'].iloc[-1]
    price_return = ((last_price - first_price) / first_price) * 100
    
    all_results.append({
        'Index': idx,
        'Full_Name': index_name_map.get(idx, idx),
        'Country': index_country_map.get(idx, 'Unknown'),
        'Months_Invested': len(monthly),
        'Total_Invested': round(total_invested, 2),
        'Final_Value': round(final_value, 2),
        'Total_Return': round(total_return, 2),
        'Return_Percentage': round(return_pct, 2),
        'Price_Return_Only': round(price_return, 2)
    })

all_results_df = pd.DataFrame(all_results)
all_results_df = all_results_df.sort_values('Return_Percentage', ascending=False)

print('__RESULT__:')
print(all_results_df.to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': [{'Index': 'IXIC', 'Country': 'United States', 'Return_Percentage': 378.6}, {'Index': '399001.SZ', 'Country': 'China', 'Return_Percentage': 134.45}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return_Percentage': 131.94}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return_Percentage': 131.52}, {'Index': 'NSEI', 'Country': 'India', 'Return_Percentage': 121.47}]}

exec(code, env_args)

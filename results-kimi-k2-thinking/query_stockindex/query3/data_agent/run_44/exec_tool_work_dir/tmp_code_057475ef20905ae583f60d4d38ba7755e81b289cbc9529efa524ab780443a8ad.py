code = """import json
import pandas as pd

# Read the data from storage
storage_val = var_functions.query_db:8
if isinstance(storage_val, str) and storage_val.endswith('.json'):
    with open(storage_val, 'r') as f:
        data = json.load(f)
else:
    data = storage_val

# Convert to DataFrame
df = pd.DataFrame(data)
# Handle datetime parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Remove rows with invalid data
df = df.dropna(subset=['Date', 'CloseUSD'])

# Index to country mapping
index_country_map = {
    'N225': 'Japan',
    'HSI': 'Hong Kong', 
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'NYA': 'United States',
    'IXIC': 'United States',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'NSEI': 'India',
    'J203.JO': 'South Africa',
    'TWII': 'Taiwan',
    'N100': 'Europe'
}

# Calculate monthly DCA returns
monthly_investment = 100
results = []

for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx].copy()
    if idx_data.empty: continue
    
    # Filter from 2000 onwards
    idx_data = idx_data[idx_data['Date'] >= pd.Timestamp('2000-01-01')]
    if idx_data.empty: continue
    
    # Get first trading day of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly = idx_data.groupby('YearMonth')['CloseUSD'].first().reset_index()
    monthly['Date'] = monthly['YearMonth'].dt.to_timestamp()
    monthly = monthly.sort_values('Date')
    
    if monthly.empty: continue
    
    # DCA calculation
    monthly['Units'] = monthly_investment / monthly['CloseUSD']
    monthly['Total_Units'] = monthly['Units'].cumsum()
    monthly['Total_Invested'] = monthly_investment * (monthly.index + 1)
    
    # Final results
    final_value = monthly['Total_Units'].iloc[-1] * monthly['CloseUSD'].iloc[-1]
    total_invested = monthly['Total_Invested'].iloc[-1]
    return_pct = ((final_value - total_invested) / total_invested) * 100
    
    results.append({
        'Index': idx,
        'Country': index_country_map.get(idx, 'Unknown'),
        'Months': len(monthly),
        'Return_Percentage': round(return_pct, 2)
    })

# Sort and get top 5
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return_Percentage', ascending=False)
top5 = results_df.head(5)

print('__RESULT__:')
print(top5.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

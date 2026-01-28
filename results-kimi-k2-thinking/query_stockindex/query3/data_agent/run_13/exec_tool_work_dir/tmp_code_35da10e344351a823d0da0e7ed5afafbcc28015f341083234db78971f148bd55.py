code = """import json
import pandas as pd

# Load the trade data from file
file_path = 'file_storage/functions.query_db:8.json'

# Read the trade data
trade_data = []
try:
    with open(file_path, 'r') as f:
        # Try to parse as complete JSON array
        try:
            trade_data = json.load(f)
        except:
            # If that fails, try line by line
            f.seek(0)
            for line in f:
                line = line.strip()
                if line:
                    try:
                        trade_data.append(json.loads(line))
                    except:
                        continue
except Exception as e:
    print('Error loading file:', e)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert data types
if not df.empty:
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    if 'CloseUSD' in df.columns:
        df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Filter from 2000 onwards
start_date = '2000-01-01'
df_filtered = df[(df['Date'] >= start_date) & df['Date'].notna() & df['CloseUSD'].notna()].copy()

# Get first trading day of each month for each index
df_filtered['YearMonth'] = df_filtered['Date'].dt.to_period('M')
monthly_data = df_filtered.groupby(['Index', 'YearMonth']).first().reset_index()

# DCA return calculation
def calculate_dca_return(prices):
    if len(prices) < 2:
        return None
    
    monthly_investment = 100
    total_invested = 0
    total_shares = 0
    
    for price in prices:
        if pd.notna(price) and price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    if total_invested == 0:
        return None
    
    final_price = prices.iloc[-1]
    final_value = total_shares * final_price
    return (final_value / total_invested - 1) * 100

# Calculate returns for each index
results = []
for index in monthly_data['Index'].unique():
    index_data = monthly_data[monthly_data['Index'] == index].sort_values('Date')
    if len(index_data) >= 12:  # At least 1 year of data
        return_pct = calculate_dca_return(index_data['CloseUSD'])
        if return_pct is not None:
            results.append({
                'Index': index,
                'Total_Return_Pct': return_pct,
                'Start_Date': str(index_data['Date'].min()),
                'End_Date': str(index_data['Date'].max()),
                'Months_of_Data': len(index_data)
            })

# Sort by return
top_5_indices = sorted(results, key=lambda x: x['Total_Return_Pct'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5_indices, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:20': {'trade_indices': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'info_data': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}, 'var_functions.execute_python:26': {'type': "<class 'str'>", 'is_list': False, 'is_string': True, 'value': 'file_storage/functions.query_db:8.json'}}

exec(code, env_args)

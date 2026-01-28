code = """import json
import pandas as pd

# Load the full trade data from the file path stored in the variable
file_path = var_functions.query_db:8

# Read the JSON file
data = pd.read_json(file_path)

# Convert Date to datetime and CloseUSD to float
data['Date'] = pd.to_datetime(data['Date'])
data['CloseUSD'] = pd.to_numeric(data['CloseUSD'])

# Filter data from 2000 onwards
data = data[data['Date'] >= '2000-01-01'].copy()
data = data.sort_values(['Index', 'Date']).reset_index(drop=True)

# Group by index to get the first trading day of each month for each index
def get_monthly_dates(df):
    df['YearMonth'] = df['Date'].dt.to_period('M')
    # Get the first trading day of each month
    monthly = df.groupby(['Index', 'YearMonth']).first().reset_index()
    return monthly

monthly_data = get_monthly_dates(data)

# Calculate returns for regular monthly investment (dollar cost averaging)
def calculate_dca_return(df):
    if len(df) < 2:
        return None
    
    # Assume $100 invested each month
    monthly_investment = 100
    total_invested = 0
    total_shares = 0
    
    for _, row in df.iterrows():
        price = row['CloseUSD']
        if pd.notna(price):
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    if total_invested == 0:
        return None
    
    # Final value
    final_price = df['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    
    # Total return
    return (final_value / total_invested - 1) * 100

# Calculate returns for each index
results = []
for index in monthly_data['Index'].unique():
    index_data = monthly_data[monthly_data['Index'] == index].sort_values('Date')
    if len(index_data) > 0:
        # Calculate DCA return since first available date (should be 2000 or close to it)
        return_pct = calculate_dca_return(index_data)
        if return_pct is not None:
            results.append({
                'Index': index,
                'Total_Return_Pct': return_pct,
                'Start_Date': index_data['Date'].min(),
                'End_Date': index_data['Date'].max(),
                'Months': len(index_data)
            })

# Sort by total return and get top 5
top_indices = sorted(results, key=lambda x: x['Total_Return_Pct'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_indices, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

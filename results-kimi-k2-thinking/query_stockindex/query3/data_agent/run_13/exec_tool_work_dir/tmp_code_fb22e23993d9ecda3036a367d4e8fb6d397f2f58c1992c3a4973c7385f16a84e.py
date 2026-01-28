code = """import json
import pandas as pd

# Load the data from storage
file_path = locals()['var_functions.query_db:8']

# Read the JSON file
with open(file_path, 'r') as f:
    data_list = json.load(f)

# Create DataFrame
df = pd.DataFrame(data_list)

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter from 2000 onwards
df = df[df['Date'] >= '2000-01-01'].copy()

# Get first trading day of each month for each index
df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_data = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate DCA returns
def calculate_dca_return(group_df):
    if len(group_df) < 2:
        return None
    
    monthly_investment = 100
    total_invested = 0
    total_shares = 0
    
    for _, row in group_df.iterrows():
        price = row['CloseUSD']
        if pd.notna(price) and price > 0:
            shares = monthly_investment / price
            total_shares += shares
            total_invested += monthly_investment
    
    if total_invested == 0:
        return None
    
    final_price = group_df['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    return (final_value / total_invested - 1) * 100

results = []
for index in monthly_data['Index'].unique():
    index_data = monthly_data[monthly_data['Index'] == index].sort_values('Date')
    if len(index_data) > 0:
        return_pct = calculate_dca_return(index_data)
        if return_pct is not None:
            results.append({
                'Index': index,
                'Total_Return_Pct': return_pct,
                'Start_Date': str(index_data['Date'].min()),
                'End_Date': str(index_data['Date'].max()),
                'Months': len(index_data)
            })

# Sort and get top 5
top_indices = sorted(results, key=lambda x: x['Total_Return_Pct'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_indices, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

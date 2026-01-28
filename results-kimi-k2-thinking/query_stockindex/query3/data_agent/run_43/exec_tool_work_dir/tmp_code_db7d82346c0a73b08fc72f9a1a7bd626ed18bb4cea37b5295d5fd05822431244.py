code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Load data
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    all_trades = json.load(f)

df = pd.DataFrame(all_trades)
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Filter from 2000 onwards
df = df[df['Date'] >= '2000-01-01'].copy()

# Sort by index and date
df = df.sort_values(['Index', 'Date'])

# For each index, get first trading day of each month
first_of_month = df.groupby(['Index', df['Date'].dt.to_period('M')]).first().reset_index()
first_of_month['Year'] = first_of_month['Date'].dt.year
first_of_month['Month'] = first_of_month['Date'].dt.month

# Calculate DCA returns - assume $1000 invested monthly
def calculate_dca_returns(group):
    monthly_investment = 1000  # USD
    
    # Calculate shares bought each month
    group['Shares'] = monthly_investment / group['CloseUSD']
    group['Cumulative_Shares'] = group['Shares'].cumsum()
    group['Cumulative_Invested'] = monthly_investment * np.arange(1, len(group) + 1)
    
    # Final value
    final_shares = group['Shares'].sum()
    final_price = group['CloseUSD'].iloc[-1]
    final_value = final_shares * final_price
    total_invested = len(group) * monthly_investment
    
    total_return = (final_value - total_invested) / total_invested * 100
    
    return {
        'Index': group['Index'].iloc[0],
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Total_Return_Pct': total_return,
        'Months': len(group),
        'Start_Date': str(group['Date'].iloc[0]),
        'End_Date': str(group['Date'].iloc[-1])
    }

# Calculate returns for each index
results = []
for idx in first_of_month['Index'].unique():
    idx_data = first_of_month[first_of_month['Index'] == idx].copy()
    if len(idx_data) > 12:  # At least 1 year of data
        result = calculate_dca_returns(idx_data)
        results.append(result)

# Sort by total return
results_sorted = sorted(results, key=lambda x: x['Total_Return_Pct'], reverse=True)

top_5 = results_sorted[:5]

output = {
    'top_5_indices': top_5,
    'all_results': results_sorted
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:22': {'total_records': 50271, 'unique_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII'], 'date_min': '2000-01-03 00:00:00', 'date_max': '2021-06-03 00:00:00'}}

exec(code, env_args)

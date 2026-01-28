code = """import json
import pandas as pd
import numpy as np
from datetime import datetime
import re

# Load trade data
result_file_path = locals()['var_functions.query_db:8']
df_trade = pd.read_json(result_file_path)

# Parse dates and filter from 2000 onwards
df_trade['Date'] = pd.to_datetime(df_trade['Date'])
df_trade = df_trade[df_trade['Date'] >= '2000-01-01'].copy()

# Sort by index and date
df_trade = df_trade.sort_values(['Index', 'Date']).reset_index(drop=True)

# For each index, simulate monthly DCA
monthly_amount = 100  # Assume $100 invested monthly

def calculate_dca_returns(df):
    results = []
    
    for idx in df['Index'].unique():
        idx_data = df[df['Index'] == idx].copy()
        
        # Get first trading day of each month
        idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
        monthly_data = idx_data.groupby('YearMonth').first().reset_index()
        
        if len(monthly_data) < 12:  # Skip indices with less than 1 year of data
            continue
            
        # Simulate DCA: invest on first trading day of each month
        units_purchased = monthly_amount / monthly_data['CloseUSD']
        total_units = units_purchased.sum()
        total_invested = monthly_amount * len(monthly_data)
        
        # Current value (using latest available price)
        current_value = total_units * monthly_data['CloseUSD'].iloc[-1]
        
        # Calculate CAGR for DCA
        years = len(monthly_data) / 12.0
        total_return = (current_value - total_invested) / total_invested
        
        if years > 0:
            cagr = ((current_value / total_invested) ** (1/years)) - 1
        else:
            cagr = 0
            
        # Calculate simple total return for comparison
        first_price = monthly_data['CloseUSD'].iloc[0]
        last_price = monthly_data['CloseUSD'].iloc[-1]
        simple_return = (last_price - first_price) / first_price
        
        results.append({
            'Index': idx,
            'Total_Years': years,
            'Total_Invested': total_invested,
            'Current_Value': current_value,
            'Total_Return_Pct': total_return * 100,
            'CAGR': cagr * 100,
            'Simple_Return_Pct': simple_return * 100,
            'First_Price': first_price,
            'Last_Price': last_price,
            'Months': len(monthly_data)
        })
    
    return pd.DataFrame(results)

returns_df = calculate_dca_returns(df_trade)

# Get top 5 indices by total return
top_5_indices = returns_df.nlargest(5, 'Total_Return_Pct')

print('__RESULT__:')
print(top_5_indices.to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:9': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'index_info_sample': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'index_symbols': ['J203.JO', 'N225', 'GSPTSE', 'NSEI', 'GDAXI', 'IXIC', 'HSI', '000001.SS', 'SSMI', 'TWII', 'NYA', 'N100', '399001.SZ'], 'trade_data_columns': ['Index', 'Date', 'CloseUSD'], 'trade_data_row_count': 67948, 'unique_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}}

exec(code, env_args)

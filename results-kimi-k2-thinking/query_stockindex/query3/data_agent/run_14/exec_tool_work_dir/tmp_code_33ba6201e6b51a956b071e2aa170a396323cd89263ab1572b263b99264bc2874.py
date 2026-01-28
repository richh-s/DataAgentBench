code = """import json
import pandas as pd
import numpy as np

# Get the file path from storage
trade_file_path = locals()['var_functions.query_db:14']

# Read the JSON file
with open(trade_file_path, 'r') as f:
    trade_data = json.load(f)

print(f"Loaded {len(trade_data)} records from file")

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert CloseUSD to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Parse dates - handle mixed format
import warnings
warnings.filterwarnings('ignore')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print(f"DataFrame created with {len(df)} rows")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Indices: {sorted(df['Index'].unique())}")

# Save DataFrame to continue with analysis
with open('/tmp/trade_df.json', 'w') as f:
    json.dump(df.to_json(orient='records'), f)

# Calculate returns for each index (monthly dollar-cost averaging)
results = []

for index_symbol in df['Index'].unique():
    # Get data for this index
    index_data = df[df['Index'] == index_symbol].copy()
    
    # Sort by date
    index_data = index_data.sort_values('Date')
    
    # Get first trading day of each month
    index_data['YearMonth'] = index_data['Date'].dt.to_period('M')
    first_of_month = index_data.groupby('YearMonth')['Date'].first()
    
    # Filter to get monthly records
    monthly_data = index_data[index_data['Date'].isin(first_of_month)]
    
    if len(monthly_data) > 12:  # Need at least 12 months of data
        # Simulate dollar-cost averaging: invest $100 each month
        total_invested = 0
        total_shares = 0
        
        for idx, row in monthly_data.iterrows():
            price = row['CloseUSD']
            if price > 0 and not pd.isna(price):
                total_invested += 100  # Invest $100 each month
                total_shares += 100 / price
        
        # Calculate final value using last available price
        if len(index_data) > 0:
            final_price = index_data['CloseUSD'].iloc[-1]
            final_value = total_shares * final_price
            
            # Calculate total return
            total_return = (final_value - total_invested) / total_invested * 100 if total_invested > 0 else 0
            
            # Calculate annualized return
            years = len(monthly_data) / 12
            annualized_return = ((1 + total_return/100) ** (1/years) - 1) * 100 if years > 0 else 0
            
            results.append({
                'Index': index_symbol,
                'TotalInvested': total_invested,
                'FinalValue': final_value,
                'TotalReturn': total_return,
                'AnnualizedReturn': annualized_return,
                'Months': len(monthly_data),
                'Years': years
            })

# Sort by total return descending
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('TotalReturn', ascending=False)

print("Top 5 indices by total return:")
for i, row in results_df.head(5).iterrows():
    print(f"{row['Index']}: {row['TotalReturn']:.2f}% total return ({row['AnnualizedReturn']:.2f}% annualized)")

print("__RESULT__:")
print(results_df.head(5).to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.list_db:8': ['index_info'], 'var_functions.execute_python:12': [{'Index': 'N225', 'Exchange': 'Tokyo Stock Exchange', 'Country': 'Japan', 'Currency': 'JPY'}, {'Index': 'HSI', 'Exchange': 'Hong Kong Stock Exchange', 'Country': 'Hong Kong', 'Currency': 'HKD'}, {'Index': '000001.SS', 'Exchange': 'Shanghai Stock Exchange', 'Country': 'China', 'Currency': 'CNY'}, {'Index': '399001.SZ', 'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China', 'Currency': 'CNY'}, {'Index': 'NYA', 'Exchange': 'New York Stock Exchange', 'Country': 'USA', 'Currency': 'USD'}, {'Index': 'IXIC', 'Exchange': 'NASDAQ', 'Country': 'USA', 'Currency': 'USD'}, {'Index': 'GDAXI', 'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany', 'Currency': 'EUR'}, {'Index': 'N100', 'Exchange': 'Euronext', 'Country': 'Europe', 'Currency': 'EUR'}, {'Index': 'GSPTSE', 'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada', 'Currency': 'CAD'}, {'Index': 'NSEI', 'Exchange': 'National Stock Exchange of India', 'Country': 'India', 'Currency': 'INR'}, {'Index': 'SSMI', 'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland', 'Currency': 'CHF'}, {'Index': 'TWII', 'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan', 'Currency': 'TWD'}, {'Index': 'J203.JO', 'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa', 'Currency': 'ZAR'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': {'success': True, 'count': 67948}}

exec(code, env_args)

code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Load the data from the previous query
file_path = var_functions.query_db:8
if isinstance(file_path, str):
    with open(file_path, 'r') as f:
        price_data = json.load(f)
else:
    price_data = var_functions.query_db:8

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# DCA parameters
monthly_investment = 100  # Fixed monthly investment in USD
results = []

for index in df['Index'].unique():
    # Get data for this index
    idx_data = df[df['Index'] == index].copy()
    idx_data = idx_data.sort_values('Date')
    
    if idx_data.empty:
        continue
    
    # Get first trading date of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_first_dates = idx_data.groupby('YearMonth').first().reset_index()
    
    # Filter from 2000-01 to current
    monthly_first_dates = monthly_first_dates[
        monthly_first_dates['Date'] >= '2000-01-01'
    ]
    
    if monthly_first_dates.empty:
        continue
    
    # Simulate DCA
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_first_dates.iterrows():
        price = row['CloseUSD']
        if pd.notna(price) and price > 0:
            shares_bought = monthly_investment / price
            total_shares += shares_bought
            total_invested += monthly_investment
    
    # Calculate current value and returns
    current_price = idx_data['CloseUSD'].iloc[-1]
    current_value = total_shares * current_price
    total_return_pct = ((current_value - total_invested) / total_invested) * 100 if total_invested > 0 else 0
    
    # Get first and last dates for calculating annualized return
    first_date = monthly_first_dates['Date'].iloc[0]
    last_date = idx_data['Date'].iloc[-1]
    years = (last_date - first_date).days / 365.25
    
    # Annualized return
    if years > 0 and total_invested > 0:
        total_growth_factor = current_value / total_invested
        annualized_return = (total_growth_factor ** (1/years) - 1) * 100
    else:
        annualized_return = 0
    
    results.append({
        'Index': index,
        'Total_Invested': total_invested,
        'Current_Value': current_value,
        'Total_Return_Pct': total_return_pct,
        'Annualized_Return_Pct': annualized_return,
        'Months': len(monthly_first_dates)
    })

# Convert results to DataFrame and sort by total return
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Pct', ascending=False)

# Get top 5 indices
top_5_indices = results_df.head(5)

__RESULT__:
print(top_5_indices.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

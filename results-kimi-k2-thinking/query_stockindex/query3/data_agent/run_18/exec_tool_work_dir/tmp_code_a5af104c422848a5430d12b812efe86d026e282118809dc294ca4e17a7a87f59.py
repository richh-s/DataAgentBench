code = """# Access the query result using locals() to handle special characters in variable name
query_key = 'var_functions.query_db:22'
query_result = locals().get(query_key)

if query_result is None:
    raise ValueError(f"Could not find query result with key: {query_key}")

import json, pandas as pd
from datetime import datetime

# Load the data
if isinstance(query_result, str):
    with open(query_result, 'r') as f:
        price_data = json.load(f)
else:
    price_data = query_result

# Process the data
df = pd.DataFrame(price_data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

print(f"Loaded data for {df['Index'].nunique()} indices")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")

# Group by index and calculate DCA returns
monthly_investment = 100
results = []

for index in df['Index'].unique():
    idx_data = df[df['Index'] == index].copy()
    idx_data = idx_data.sort_values('Date')
    
    if idx_data.empty:
        continue
    
    # Get first trading date of each month from 2000 onwards
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_first_dates = idx_data.groupby('YearMonth').first().reset_index()
    monthly_first_dates = monthly_first_dates[monthly_first_dates['Date'] >= '2000-01-01']
    
    if monthly_first_dates.empty:
        continue
    
    # Simulate DCA - invest monthly_investment on first trading day of each month
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
    
    # Calculate annualized return
    first_date = monthly_first_dates['Date'].iloc[0]
    last_date = idx_data['Date'].iloc[-1]
    years = (last_date - first_date).days / 365.25
    
    if years > 0 and total_invested > 0:
        total_growth_factor = current_value / total_invested
        annualized_return = (total_growth_factor ** (1/years) - 1) * 100
    else:
        annualized_return = 0
    
    results.append({
        'Index': index,
        'Total_Invested': round(total_invested, 2),
        'Current_Value': round(current_value, 2),
        'Total_Return_Pct': round(total_return_pct, 2),
        'Annualized_Return_Pct': round(annualized_return, 2),
        'Months': len(monthly_first_dates)
    })

# Create DataFrame and get top 5
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Pct', ascending=False)
top_5_indices = results_df.head(5)

# Print results for debugging
print("\nTop 5 indices by total DCA return:")
for _, row in top_5_indices.iterrows():
    print(f"{row['Index']}: {row['Total_Return_Pct']:.2f}% total, {row['Annualized_Return_Pct']:.2f}% annualized")

# Output the result in required format
result_json = top_5_indices.to_json(orient='records')
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:20': ['index_info'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

code = """# Access query result
query_result = locals()['var_functions.query_db:22']

import json
import pandas as pd

# Load data
if isinstance(query_result, str):
    with open(query_result, 'r') as f:
        price_data = json.load(f)
else:
    price_data = query_result

# Convert to DataFrame
df = pd.DataFrame(price_data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Calculate DCA returns for each index
monthly_investment = 100
results = []

for index in df['Index'].unique():
    idx_data = df[df['Index'] == index].copy().sort_values('Date')
    
    if idx_data.empty:
        continue
    
    # Get monthly first dates from 2000
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_first = idx_data.groupby('YearMonth').first().reset_index()
    monthly_first = monthly_first[monthly_first['Date'] >= '2000-01-01']
    
    if monthly_first.empty:
        continue
    
    # DCA simulation
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_first.iterrows():
        price = row['CloseUSD']
        if pd.notna(price) and price > 0:
            total_shares += monthly_investment / price
            total_invested += monthly_investment
    
    # Calculate returns
    current_price = idx_data['CloseUSD'].iloc[-1]
    current_value = total_shares * current_price
    total_return_pct = ((current_value - total_invested) / total_invested * 100) if total_invested > 0 else 0
    
    # Annualized return
    years = (idx_data['Date'].iloc[-1] - monthly_first['Date'].iloc[0]).days / 365.25
    annualized = 0
    if years > 0 and total_invested > 0:
        annualized = ((current_value / total_invested) ** (1/years) - 1) * 100
    
    results.append({
        'Index': index,
        'Total_Return_Pct': round(total_return_pct, 2),
        'Annualized_Return_Pct': round(annualized, 2),
        'Months': len(monthly_first)
    })

# Get top 5
results_df = pd.DataFrame(results).sort_values('Total_Return_Pct', ascending=False)
top_5 = results_df.head(5)

# Output
result_str = top_5.to_json(orient='records')
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:20': ['index_info'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

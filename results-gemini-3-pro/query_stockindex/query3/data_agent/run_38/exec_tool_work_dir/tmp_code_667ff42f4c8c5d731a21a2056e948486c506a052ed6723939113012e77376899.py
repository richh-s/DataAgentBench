code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-11112950162314494458'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Filter for date >= 2000-01-01 (already done in query, but good to ensure)
df = df[df['Date'] >= '2000-01-01']

# Define function to calculate return
def calculate_dca_return(group):
    # Sort by date
    group = group.sort_values('Date')
    
    # Resample to get the first trading day of each month
    # We can do this by grouping by Year-Month and taking the first entry
    group['YearMonth'] = group['Date'].dt.to_period('M')
    monthly_investments = group.groupby('YearMonth').first().reset_index()
    
    # Check start date
    start_date = group['Date'].min()
    # If start date is significantly after 2000-01-01, note it.
    # But for ranking, we just calculate what we can.
    
    # Simulation
    # Invest 1 unit each month
    units_accumulated = 0
    months_invested = 0
    
    for _, row in monthly_investments.iterrows():
        price = row['Close']
        if pd.notnull(price) and price > 0:
            units = 1.0 / price
            units_accumulated += units
            months_invested += 1
            
    # Final value
    last_price = group.iloc[-1]['Close']
    total_value = units_accumulated * last_price
    
    # Overall return (percentage increase)
    if months_invested > 0:
        overall_return = (total_value - months_invested) / months_invested
    else:
        overall_return = 0
        
    return overall_return

# Calculate returns for each index
results = []
indices = df['Index'].unique()

for idx in indices:
    group = df[df['Index'] == idx].copy()
    ret = calculate_dca_return(group)
    results.append({'Index': idx, 'Return': ret})

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-8000534823580807906': ['index_info'], 'var_function-call-8000534823580808341': ['index_trade'], 'var_function-call-9672975509357680590': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-9672975509357679569': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_function-call-11112950162314494458': 'file_storage/function-call-11112950162314494458.json'}

exec(code, env_args)

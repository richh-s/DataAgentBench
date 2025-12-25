code = """import pandas as pd
import json
from dateutil import parser

# Load the data
file_path = locals()['var_function-call-16330929568168581514']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert CloseUSD to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Parse dates
# Given the mixed format, we can try pd.to_datetime. 
# It's usually smart enough. If it fails, we might need dateutil.
# Let's try pd.to_datetime first.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for dates >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Drop rows with NaN CloseUSD or Date
df = df.dropna(subset=['CloseUSD', 'Date'])

# Create a YearMonth column to facilitate monthly grouping
df['YearMonth'] = df['Date'].dt.to_period('M')

# Sort by Date
df = df.sort_values(['Index', 'Date'])

# Group by Index and YearMonth, take the first entry (first trading day of the month)
monthly_investments = df.groupby(['Index', 'YearMonth']).first().reset_index()

# Calculate returns
results = []
indices = monthly_investments['Index'].unique()

for idx in indices:
    idx_data = monthly_investments[monthly_investments['Index'] == idx].sort_values('Date')
    
    if idx_data.empty:
        continue
    
    # Investment: $100 each month
    # Shares bought = 100 / CloseUSD
    # Using 100 as the fixed amount.
    idx_data = idx_data.copy()
    idx_data['Shares'] = 100.0 / idx_data['CloseUSD']
    
    total_shares = idx_data['Shares'].sum()
    total_invested = len(idx_data) * 100.0
    
    # Final value: Total Shares * Last available CloseUSD
    # We should get the very last price available in the dataset for this index, 
    # not necessarily the first day of the last month. 
    # The monthly_investments df only has first days.
    # So I should get the last price from the original filtered df.
    
    last_price_row = df[df['Index'] == idx].sort_values('Date').iloc[-1]
    last_price = last_price_row['CloseUSD']
    final_date = last_price_row['Date']
    
    final_value = total_shares * last_price
    
    overall_return = (final_value - total_invested) / total_invested * 100.0
    
    results.append({
        'Index': idx,
        'Return': overall_return,
        'LastDate': str(final_date),
        'TotalInvested': total_invested,
        'FinalValue': final_value
    })

# Convert to DataFrame
res_df = pd.DataFrame(results)
res_df = res_df.sort_values('Return', ascending=False)

print("__RESULT__:")
print(res_df.to_json(orient='records'))"""

env_args = {'var_function-call-2311047995070987928': ['index_info'], 'var_function-call-2311047995070984741': ['index_trade'], 'var_function-call-8045809154294584040': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}], 'var_function-call-8045809154294587039': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}], 'var_function-call-6651292033751510829': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-13449016031599948060': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-13449016031599950325': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15857135813775900604': [{'count_star()': '104224'}], 'var_function-call-16330929568168581514': 'file_storage/function-call-16330929568168581514.json'}

exec(code, env_args)

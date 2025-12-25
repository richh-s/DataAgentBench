code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-4703909687357535419'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# robust date conversion
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Sort
df = df.sort_values(['Index', 'Date'])

# Create YearMonth
df['YearMonth'] = df['Date'].dt.to_period('M')

# Group by Index and YearMonth, pick the first trading day
monthly_investments = df.groupby(['Index', 'YearMonth']).head(1)

# Calculate investment
monthly_investments['InvestedAmount'] = 100.0
monthly_investments['Units'] = 100.0 / monthly_investments['CloseUSD']

# Aggregate per index
results = []
indices = df['Index'].unique()

for idx in indices:
    idx_investments = monthly_investments[monthly_investments['Index'] == idx]
    total_invested = idx_investments['InvestedAmount'].sum()
    total_units = idx_investments['Units'].sum()
    
    # Get last price
    last_price_row = df[df['Index'] == idx].iloc[-1]
    final_value = total_units * last_price_row['CloseUSD']
    
    roi = (final_value - total_invested) / total_invested if total_invested > 0 else 0
    
    results.append({
        'Index': idx,
        'TotalInvested': total_invested,
        'FinalValue': final_value,
        'ROI': roi
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('ROI', ascending=False)

# Map to countries
country_map = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe',
    '399001.SZ': 'China'
}

top_5 = results_df.head(5).copy()
top_5['Country'] = top_5['Index'].map(country_map)

print("__RESULT__:")
print(top_5[['Index', 'Country', 'ROI']].to_json(orient='records'))"""

env_args = {'var_function-call-1472751431662541386': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-1472751431662541697': [{'column_name': 'Index', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Date', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Open', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'High', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Low', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Close', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Adj Close', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseUSD', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-3265391502792838996': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-3265391502792835131': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4703909687357535419': 'file_storage/function-call-4703909687357535419.json'}

exec(code, env_args)

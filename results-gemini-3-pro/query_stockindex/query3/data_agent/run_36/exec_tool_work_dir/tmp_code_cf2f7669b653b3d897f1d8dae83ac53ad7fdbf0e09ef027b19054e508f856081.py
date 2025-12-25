code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-6795954848509195129']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Handle Date conversion robustly
# Try simple conversion first, if fails, use errors='coerce'
try:
    df['Date'] = pd.to_datetime(df['Date'])
except:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df.dropna(subset=['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Filter for data starting 2000
df = df[df['Date'] >= '2000-01-01']

# Country Mapping
country_map = {
    'J203.JO': 'South Africa', 
    'N225': 'Japan', 
    'GSPTSE': 'Canada', 
    'NSEI': 'India', 
    'GDAXI': 'Germany', 
    'HSI': 'Hong Kong', 
    'NYA': 'United States', 
    '000001.SS': 'China', 
    'SSMI': 'Switzerland', 
    'TWII': 'Taiwan', 
    'N100': 'Europe', 
    '399001.SZ': 'China', 
    'IXIC': 'United States'
}

# Group by Index
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].sort_values('Date')
    if sub.empty:
        continue
    
    start_date = sub['Date'].min()
    end_date = sub['Date'].max()
    
    # Resample
    sub_indexed = sub.set_index('Date')
    # Get first available price of each month
    # We can group by Year-Month and take first
    sub_indexed['YYYYMM'] = sub_indexed.index.to_period('M')
    monthly = sub_indexed.groupby('YYYYMM').first().reset_index()
    
    monthly_investment = 100
    monthly['Units'] = monthly_investment / monthly['CloseUSD']
    total_units = monthly['Units'].sum()
    total_invested = len(monthly) * monthly_investment
    
    # Final Value
    last_price = sub.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    if total_invested == 0:
        roi = 0
    else:
        roi = (final_value - total_invested) / total_invested
        
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'Start Date': str(start_date.date()),
        'End Date': str(end_date.date()),
        'ROI %': round(roi * 100, 2)
    })

results_df = pd.DataFrame(results).sort_values('ROI %', ascending=False)

print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-14702660799195933244': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-14702660799195933693': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-6795954848509195129': 'file_storage/function-call-6795954848509195129.json'}

exec(code, env_args)

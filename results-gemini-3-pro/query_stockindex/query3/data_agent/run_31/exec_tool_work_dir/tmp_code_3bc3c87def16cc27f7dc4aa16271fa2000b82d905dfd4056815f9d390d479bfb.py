code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-8540390000505140219'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# The dates are mixed format strings.
# Some are "31 Dec 1986, 00:00", others "January 02, 1987 at 12:00 AM"
# pd.to_datetime is usually smart enough.
df['Date'] = pd.to_datetime(df['Date'], format='mixed', utc=True)

# Filter >= 2000-01-01
df = df[df['Date'] >= pd.to_datetime('2000-01-01', utc=True)]

# Sort
df = df.sort_values(['Index', 'Date'])

# Define country mapping
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

results = []

for idx, group in df.groupby('Index'):
    # Resample to get the first trading day of each month
    # We want to simulate monthly investment.
    # Approach: Create a Year-Month column, group by it, take first date.
    group['YM'] = group['Date'].dt.to_period('M')
    monthly_data = group.groupby('YM').first().reset_index()
    
    # Calculate investment
    # Invest 1 unit of currency each month
    invest_amount = 1.0
    
    # Price
    # Use Adj Close
    prices = monthly_data['Adj Close'].astype(float).values
    
    if len(prices) == 0:
        continue
        
    # Units bought
    units = invest_amount / prices
    total_units = units.sum()
    total_invested = len(units) * invest_amount
    
    # Final value
    # Price at the very last available date in the dataset for this index
    last_price = float(group.iloc[-1]['Adj Close'])
    
    final_value = total_units * last_price
    
    # Return
    ret = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'Return': ret,
        'Total_Invested': total_invested,
        'Final_Value': final_value,
        'Start_Date': monthly_data['Date'].min().strftime('%Y-%m-%d'),
        'End_Date': group['Date'].max().strftime('%Y-%m-%d')
    })

# Sort by Return descending
results_df = pd.DataFrame(results).sort_values('Return', ascending=False)

print("__RESULT__:")
print(json.dumps(results_df.head(10).to_dict(orient='records')))"""

env_args = {'var_function-call-200894980028602229': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-200894980028601412': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-8540390000505140219': 'file_storage/function-call-8540390000505140219.json'}

exec(code, env_args)

code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-12711502332547647924'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns
# Clean CloseUSD - some might be strings
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Convert Date
# Using mixed format inference
# Note: In some pandas versions, format='mixed' is required for mixed formats, in others it's automatic or not available.
# We will try without arguments first, if it raises or is slow, we might need a custom parser.
# Given the formats, dateutil parser is usually used by pandas.
try:
    df['Date'] = pd.to_datetime(df['Date'], utc=True, format='mixed')
except:
    df['Date'] = pd.to_datetime(df['Date'], utc=True)

df = df.dropna(subset=['CloseUSD', 'Date'])

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Sort
df = df.sort_values(['Index', 'Date'])

# DCA Logic
results = []
indices = df['Index'].unique()

for idx in indices:
    sub = df[df['Index'] == idx].copy()
    if sub.empty:
        continue
    
    # Resample to monthly investment
    # We'll assign a 'YearMonth' column
    sub['YearMonth'] = sub['Date'].dt.to_period('M')
    
    # Take the first entry of each month
    monthly_investments = sub.groupby('YearMonth').first().reset_index()
    
    # Investment details
    monthly_amt = 100.0
    total_invested = len(monthly_investments) * monthly_amt
    
    if total_invested == 0:
        continue

    # Units bought
    # Check for 0 price to avoid division by zero (unlikely for indices but good practice)
    valid_investments = monthly_investments[monthly_investments['CloseUSD'] > 0]
    units = (monthly_amt / valid_investments['CloseUSD']).sum()
    
    # Final value: Total units * Price at the very end
    last_price = sub.iloc[-1]['CloseUSD']
    final_value = units * last_price
    
    roi = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'FinalValue': final_value,
        'TotalInvested': total_invested
    })

results_df = pd.DataFrame(results)
top5 = results_df.sort_values('ROI', ascending=False).head(5)

# Map Countries
country_map = {
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'J203.JO': 'South Africa',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'NYA': 'United States',
    'N100': 'Europe',
    '399001.SZ': 'China'
}

top5['Country'] = top5['Index'].map(country_map)

print('__RESULT__:')
print(top5[['Index', 'Country', 'ROI']].to_json(orient='records'))"""

env_args = {'var_function-call-4158167173827908362': ['index_info'], 'var_function-call-4158167173827909643': ['index_trade'], 'var_function-call-16339520425098077836': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-16933895561841424957': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-14659251180660056152': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8058352929469743033': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_function-call-12711502332547647924': 'file_storage/function-call-12711502332547647924.json'}

exec(code, env_args)

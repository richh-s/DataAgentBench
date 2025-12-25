code = """import pandas as pd
import json

# Load trade data
file_path = locals()['var_function-call-15375229801885648491']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime
# The formats are mixed. pandas to_datetime with errors='coerce' or distinct format parsing is needed.
# Let's try flexible parsing.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates (if any)
df = df.dropna(subset=['Date'])

# Filter for dates starting from 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Convert CloseUSD to float
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Sort
df = df.sort_values(by=['Index', 'Date'])

# Simulate Monthly Investment
results = []
indices = df['Index'].unique()

for idx in indices:
    sub_df = df[df['Index'] == idx].copy()
    
    # Identify investment dates: first available trading day of each month
    # Create a 'YearMonth' column
    sub_df['YearMonth'] = sub_df['Date'].dt.to_period('M')
    
    # Group by YearMonth and pick the first entry
    investments = sub_df.groupby('YearMonth').first().reset_index()
    
    # We assume investment happens at the Close price of the first trading day
    # Investment amount = 1 USD (arbitrary, cancels out)
    investments['Units'] = 1.0 / investments['CloseUSD']
    
    total_units = investments['Units'].sum()
    total_invested = len(investments)
    
    # Final Value
    # Latest price in the dataset for this index
    latest_price = sub_df.iloc[-1]['CloseUSD']
    final_value = total_units * latest_price
    
    # ROI
    roi = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'TotalInvested': total_invested,
        'FinalValue': final_value
    })

# Convert to DataFrame for ranking
res_df = pd.DataFrame(results)
res_df = res_df.sort_values(by='ROI', ascending=False)
top_5 = res_df.head(5)

# Mapping dictionary
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

top_5_list = []
for _, row in top_5.iterrows():
    idx = row['Index']
    country = country_map.get(idx, 'Unknown')
    top_5_list.append({
        'Index': idx,
        'Country': country,
        'ROI': row['ROI']
    })

print("__RESULT__:")
print(json.dumps(top_5_list))"""

env_args = {'var_function-call-16926035926398991743': ['index_info'], 'var_function-call-5731442589089595122': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-2454512273551659864': ['index_trade'], 'var_function-call-5462741048995157926': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-7432320520164462616': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Close': '2460.5', 'CloseUSD': '319.865'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM', 'Close': '2533.899902', 'CloseUSD': '329.40698726000005'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00', 'Close': '2536.899902', 'CloseUSD': '329.79698726000004'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM', 'Close': '2499.399902', 'CloseUSD': '324.92198726000004'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM', 'Close': '2484.399902', 'CloseUSD': '322.97198726000005'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00', 'Close': '2524.0', 'CloseUSD': '328.12'}], 'var_function-call-14062724753856073466': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-15615224378772696323': [{'count_star()': '104224'}], 'var_function-call-15375229801885648491': 'file_storage/function-call-15375229801885648491.json'}

exec(code, env_args)

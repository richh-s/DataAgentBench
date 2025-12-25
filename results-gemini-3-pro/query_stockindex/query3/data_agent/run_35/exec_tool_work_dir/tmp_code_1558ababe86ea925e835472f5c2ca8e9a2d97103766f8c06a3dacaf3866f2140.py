code = """import pandas as pd
import json

# Load data
with open('var_function-call-12225257955498936507.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

# Filter for dates starting from 2000-01-01
df = df[df['Date'] >= '2000-01-01']
# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Get list of indices
indices = df['Index'].unique()

results = []

for idx in indices:
    # Sort by date
    sub = df[df['Index'] == idx].sort_values('Date')
    if sub.empty:
        continue
    
    # Resample to monthly investment (first trading day of each month)
    sub['YM'] = sub['Date'].dt.to_period('M')
    monthly_investments = sub.groupby('YM').first().reset_index()
    
    monthly_amt = 1000.0
    total_invested = 0.0
    total_units = 0.0
    
    for _, row in monthly_investments.iterrows():
        price = row['CloseUSD']
        if price > 0:
            units = monthly_amt / price
            total_units += units
            total_invested += monthly_amt
            
    # Value at the end of the period (using the last available price in the dataset)
    last_price = sub.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    if total_invested > 0:
        overall_return = (final_value - total_invested) / total_invested
    else:
        overall_return = 0.0
        
    results.append({
        'Index': idx,
        'Return': overall_return,
        'Total Invested': total_invested,
        'Final Value': final_value
    })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)

# Mapping
mapping = {
    "NYA": "United States",
    "IXIC": "United States",
    "HSI": "Hong Kong",
    "000001.SS": "China",
    "N225": "Japan",
    "399001.SZ": "China",
    "GSPTSE": "Canada",
    "NSEI": "India",
    "GDAXI": "Germany",
    "SSMI": "Switzerland",
    "TWII": "Taiwan",
    "N100": "Europe",
    "J203.JO": "South Africa"
}

results_df['Country'] = results_df['Index'].map(mapping)

print('__RESULT__:')
print(results_df.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-8480507928447206026': ['index_info'], 'var_function-call-8480507928447208137': ['index_trade'], 'var_function-call-12583267149633058560': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-12583267149633056817': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-1714024378285467501': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-4806133388083031469': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-12225257955498936507': 'file_storage/function-call-12225257955498936507.json'}

exec(code, env_args)

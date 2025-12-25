code = """import json
import pandas as pd
from dateutil import parser

# Load data
file_path = locals()['var_function-call-6499139532502453844']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# The dates are in mixed format. dateutil.parser.parse is slow on list comprehension for large data. 
# pd.to_datetime with errors='coerce' might be faster if formats are standard, but here they are mixed.
# Let's try pd.to_datetime, it usually handles mixed formats well.
df['Date'] = pd.to_datetime(df['Date'], format='mixed', utc=True)

# Filter for >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Sort by Date
df = df.sort_values(['Index', 'Date'])

# Mapping
index_country_map = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'N225': 'Japan',
    'N100': 'Europe', # Euronext
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'TWII': 'Taiwan',
    'SSMI': 'Switzerland',
    'J203.JO': 'South Africa'
}

# Function to calculate return
results = []

for idx, group in df.groupby('Index'):
    # Resample to monthly start (taking the first trading day of the month)
    # create a month period
    group['YearMonth'] = group['Date'].dt.to_period('M')
    # take the first entry per month
    monthly_data = group.drop_duplicates(subset='YearMonth', keep='first').copy()
    
    # Check start date
    first_date = monthly_data['Date'].iloc[0]
    # Allow a small buffer, e.g., if data starts in Jan 2000.
    if first_date > pd.Timestamp('2000-02-01', tz='UTC'):
        # Index started later than Jan 2000, skip it based on "since 2000" requirement
        continue
    
    # Calculate investment
    # Invest 1 unit of currency (USD) each month
    # Units bought = 1 / Price
    monthly_data['Units'] = 1 / monthly_data['CloseUSD'].astype(float)
    
    total_units = monthly_data['Units'].sum()
    total_invested = len(monthly_data)
    
    # Final value
    final_price = group['CloseUSD'].astype(float).iloc[-1] # Use the very last available price, not just the monthly start
    final_value = total_units * final_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Country': index_country_map.get(idx, 'Unknown'),
        'Return': overall_return,
        'FinalValue': final_value,
        'Invested': total_invested
    })

# Convert to DataFrame
res_df = pd.DataFrame(results)
res_df = res_df.sort_values('Return', ascending=False)

print("__RESULT__:")
print(res_df.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-7298216697624936112': ['index_info'], 'var_function-call-7298216697624936091': ['index_trade'], 'var_function-call-4885089669788374823': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-4885089669788375530': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-8519188745840322015': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-4714276876713809212': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4714276876713808055': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-6499139532502453844': 'file_storage/function-call-6499139532502453844.json'}

exec(code, env_args)

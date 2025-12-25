code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-16511267577190411835'], 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Function to parse dates
def parse_date(date_str):
    # Common cleanups
    date_str = str(date_str)
    # Remove ' at 12:00 AM' or similar time components to simplify
    date_str = re.sub(r' at \d{1,2}:\d{2} [AP]M', '', date_str)
    date_str = re.sub(r', \d{2}:\d{2}', '', date_str)
    date_str = date_str.split(' ')[0] if '-' in date_str and ':' in date_str else date_str # For YYYY-MM-DD HH:MM:SS
    return date_str

df['clean_date'] = df['Date'].apply(parse_date)
# Now use to_datetime. It should be easier.
df['dt'] = pd.to_datetime(df['clean_date'], errors='coerce')

# Filter >= 2000-01-01
df_filtered = df[df['dt'] >= '2000-01-01'].copy()
df_filtered['Adj Close'] = pd.to_numeric(df_filtered['Adj Close'], errors='coerce')
df_filtered = df_filtered.dropna(subset=['Adj Close', 'dt'])

# Sort
df_filtered = df_filtered.sort_values(by=['Index', 'dt'])

# Define function to calculate returns
results = []
indices = df_filtered['Index'].unique()

monthly_investment = 100.0

for idx in indices:
    sub = df_filtered[df_filtered['Index'] == idx].copy()
    sub['Year'] = sub['dt'].dt.year
    sub['Month'] = sub['dt'].dt.month
    
    # Identify investment days: First available day of each month
    # Group by Year, Month and take the first entry
    invest_days = sub.groupby(['Year', 'Month']).first().reset_index()
    
    # Simulate Investment
    # Units bought = Investment / Price
    invest_days['Units'] = monthly_investment / invest_days['Adj Close']
    
    total_units = invest_days['Units'].sum()
    total_invested = len(invest_days) * monthly_investment
    
    # Final Value
    last_price = sub.iloc[-1]['Adj Close']
    final_value = total_units * last_price
    
    if total_invested > 0:
        overall_return = (final_value - total_invested) / total_invested
    else:
        overall_return = 0
        
    results.append({
        'Index': idx,
        'Return': overall_return,
        'TotalInvested': total_invested,
        'FinalValue': final_value
    })

results_df = pd.DataFrame(results).sort_values(by='Return', ascending=False)
top_5 = results_df.head(5).to_dict(orient='records')

# Mapping
mapping = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'N225': 'Japan',
    'GDAXI': 'Germany',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa',
    'N100': 'Europe',
    '399001.SZ': 'China'
}

final_output = []
for item in top_5:
    idx = item['Index']
    country = mapping.get(idx, 'Unknown')
    final_output.append({
        'Index': idx,
        'Return': item['Return'],
        'Country': country
    })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-7580508971202642257': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-7580508971202644492': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-11595469588490585805': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-12650114581479672954': [{'count_star()': '104224'}], 'var_function-call-16511267577190411835': 'file_storage/function-call-16511267577190411835.json', 'var_function-call-16511267577190409320': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)

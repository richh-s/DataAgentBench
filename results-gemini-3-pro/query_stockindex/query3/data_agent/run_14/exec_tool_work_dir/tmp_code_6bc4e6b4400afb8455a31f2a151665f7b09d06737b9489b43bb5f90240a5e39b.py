code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-6337830110883095881'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# Using infer_datetime_format=True or just let pandas guess.
# Given mixed formats with month names, pandas is usually good.
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
except:
    # Fallback for older pandas if 'mixed' not supported
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['Date'])

# Filter for >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Calculate returns for each index
results = []
indices = df['Index'].unique()

for idx in indices:
    sub_df = df[df['Index'] == idx].sort_values('Date')
    if sub_df.empty:
        continue
    
    # Identify monthly investment dates (first trading day of each month)
    sub_df['YearMonth'] = sub_df['Date'].dt.to_period('M')
    
    # Group by YearMonth and take the first entry
    monthly_investments = sub_df.groupby('YearMonth').first().reset_index()
    
    # Calculate
    monthly_amount = 1000.0
    total_invested = len(monthly_investments) * monthly_amount
    
    units_bought = monthly_amount / monthly_investments['CloseUSD']
    total_units = units_bought.sum()
    
    final_price = sub_df.iloc[-1]['CloseUSD']
    final_value = total_units * final_price
    
    roi = (final_value - total_invested) / total_invested
    
    results.append({'Index': idx, 'Return': roi})

# Sort top 5
results_df = pd.DataFrame(results).sort_values('Return', ascending=False).head(5)

# Map to countries
country_map = {
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'NYA': 'United States',
    'SSMI': 'Switzerland',
    'HSI': 'Hong Kong'
}

final_list = []
for _, row in results_df.iterrows():
    idx = row['Index']
    country = country_map.get(idx, 'Unknown')
    final_list.append({'Index': idx, 'Country': country, 'Return': row['Return']})

print('__RESULT__:')
print(json.dumps(final_list))"""

env_args = {'var_function-call-10035367016368413966': [{'Index': 'J203.JO', 'start_date': '01 Apr 2016, 00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'count': '2346'}, {'Index': 'N225', 'start_date': '01 Apr 1971, 00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'count': '13874'}, {'Index': 'GSPTSE', 'start_date': '01 Apr 1981, 00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'count': '10526'}, {'Index': 'NSEI', 'start_date': '01 Apr 2014, 00:00', 'end_date': 'September 30, 2014 at 12:00 AM', 'count': '3346'}, {'Index': 'GDAXI', 'start_date': '01 Apr 1992, 00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'count': '8438'}, {'Index': 'IXIC', 'start_date': '01 Apr 1974, 00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'count': '12690'}, {'Index': 'NYA', 'start_date': '01 Apr 1969, 00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'count': '13947'}, {'Index': '000001.SS', 'start_date': '01 Apr 2003, 00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'count': '5791'}, {'Index': 'SSMI', 'start_date': '01 Apr 1996, 00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'count': '7671'}, {'Index': 'TWII', 'start_date': '01 Apr 2004, 00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'count': '5869'}, {'Index': 'HSI', 'start_date': '01 Apr 1992, 00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'count': '8492'}, {'Index': 'N100', 'start_date': '01 Apr 2003, 00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'count': '5474'}, {'Index': '399001.SZ', 'start_date': '01 Apr 2004, 00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'count': '5760'}], 'var_function-call-10035367016368410749': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-27186830941620162': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'CloseUSD': '335.16599363'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'CloseUSD': '319.865'}, {'Index': 'HSI', 'Date': '20 Jan 1987, 00:00', 'CloseUSD': '318.48698726000003'}, {'Index': 'HSI', 'Date': 'January 21, 1987 at 12:00 AM', 'CloseUSD': '329.40698726000005'}, {'Index': 'HSI', 'Date': '22 Jan 1987, 00:00', 'CloseUSD': '329.79698726000004'}, {'Index': 'HSI', 'Date': 'January 23, 1987 at 12:00 AM', 'CloseUSD': '324.92198726000004'}, {'Index': 'HSI', 'Date': 'January 26, 1987 at 12:00 AM', 'CloseUSD': '322.97198726000005'}, {'Index': 'HSI', 'Date': '27 Jan 1987, 00:00', 'CloseUSD': '328.12'}, {'Index': 'HSI', 'Date': 'January 28, 1987 at 12:00 AM', 'CloseUSD': '331.92900637'}], 'var_function-call-6337830110883095881': 'file_storage/function-call-6337830110883095881.json'}

exec(code, env_args)

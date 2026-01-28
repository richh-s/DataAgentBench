code = """import json
import pandas as pd
from datetime import datetime

# Get the file path from the storage
file_path = locals()['var_functions.query_db:20']

# Read the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)
print('Data shape:', df.shape)
print('Columns:', df.columns.tolist())
print('Unique indices:', sorted(df['Index'].unique()))

# Parse dates - the format varies, so we'll try multiple approaches
def parse_date(date_str):
    try:
        # Try ISO format first
        return pd.to_datetime(date_str)
    except:
        try:
            # Try removing 'at' and commas
            cleaned = date_str.replace(' at ', ' ').replace(',', '')
            return pd.to_datetime(cleaned)
        except:
            # Return None if parsing fails
            return None

# Apply date parsing
df['Date_parsed'] = df['Date'].apply(parse_date)

# Check for successful parsing
successful_parsing = df['Date_parsed'].notna().sum()
print('Successfully parsed dates:', successful_parsing, 'out of', len(df))

# Filter for 2020+ data
recent_data = df[df['Date_parsed'] >= '2020-01-01']
print('Data from 2020 onwards:', len(recent_data))

if len(recent_data) > 0:
    print('Date range for 2020+ data:')
    print('Min date:', recent_data['Date_parsed'].min())
    print('Max date:', recent_data['Date_parsed'].max())
    print('Indices with 2020+ data:', sorted(recent_data['Index'].unique()))

# Calculate intraday volatility for all data
# Convert string columns to numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Calculate intraday volatility
df['intraday_volatility'] = (df['High'] - df['Low']) / df['Open']

# Filter for Asia indices
asia_indices = ['HSI', 'N225', '000001.SS', 'NSEI', 'TWII', '399001.SZ']
asia_data = df[df['Index'].isin(asia_indices) & df['Date_parsed'].notna()]

# Group by index and calculate average volatility since 2020
volatility_2020 = []
for idx in asia_indices:
    idx_data = asia_data[(asia_data['Index'] == idx) & (asia_data['Date_parsed'] >= '2020-01-01')]
    if len(idx_data) > 0:
        avg_vol = idx_data['intraday_volatility'].mean()
        volatility_2020.append({
            'Index': idx,
            'avg_volatility': avg_vol,
            'data_points': len(idx_data)
        })

print('Average intraday volatility since 2020:')
for item in volatility_2020:
    print(f"{item['Index']}: {item['avg_volatility']:.6f} ({item['data_points']} days)")

# Find the highest
if volatility_2020:
    highest = max(volatility_2020, key=lambda x: x['avg_volatility'])
    print(f"Highest volatility: {highest['Index']} with {highest['avg_volatility']:.6f}")

result = json.dumps(volatility_2020)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}], 'var_functions.query_db:16': [{'Index': 'N225', 'Date': 'September 30, 2020 at 12:00 AM', 'Open': '23478.84961', 'High': '23522.38086', 'Low': '23170.89063'}, {'Index': 'TWII', 'Date': 'September 30, 2020 at 12:00 AM', 'Open': '12483.65039', 'High': '12568.67969', 'Low': '12466.58008'}, {'Index': 'HSI', 'Date': 'September 30, 2019 at 12:00 AM', 'Open': '25844.71094', 'High': '26161.69922', 'Low': '25786.28906'}, {'Index': 'HSI', 'Date': 'September 30, 2016 at 12:00 AM', 'Open': '23435.28906', 'High': '23484.36914', 'Low': '23239.35938'}, {'Index': '399001.SZ', 'Date': 'September 30, 2015 at 12:00 AM', 'Open': '10004.79981', 'High': '10048.86035', 'Low': '9890.709961'}, {'Index': '000001.SS', 'Date': 'September 30, 2015 at 12:00 AM', 'Open': '3052.841064', 'High': '3073.300049', 'Low': '3039.741943'}, {'Index': '000001.SS', 'Date': 'September 30, 2014 at 12:00 AM', 'Open': '2361.318115', 'High': '2365.490967', 'Low': '2354.268066'}, {'Index': 'NSEI', 'Date': 'September 30, 2014 at 12:00 AM', 'Open': '7948.799805', 'High': '8030.899902', 'Low': '7923.850098'}, {'Index': 'TWII', 'Date': 'September 30, 2014 at 12:00 AM', 'Open': '8954.580078', 'High': '8998.830078', 'Low': '8860.169922'}, {'Index': 'TWII', 'Date': 'September 30, 2011 at 12:00 AM', 'Open': '7222.160156', 'High': '7251.870117', 'Low': '7163.75'}, {'Index': 'N225', 'Date': 'September 30, 2011 at 12:00 AM', 'Open': '8713.910156', 'High': '8756.0', 'Low': '8653.620117'}, {'Index': '000001.SS', 'Date': 'September 30, 2011 at 12:00 AM', 'Open': '2368.397949', 'High': '2377.541992', 'Low': '2348.217041'}, {'Index': '399001.SZ', 'Date': 'September 30, 2010 at 12:00 AM', 'Open': '11154.83984', 'High': '11468.78027', 'Low': '11125.49023'}, {'Index': 'N225', 'Date': 'September 30, 2010 at 12:00 AM', 'Open': '9554.830078', 'High': '9566.839844', 'Low': '9369.349609'}, {'Index': 'N225', 'Date': 'September 30, 2009 at 12:00 AM', 'Open': '10105.16992', 'High': '10138.04004', 'Low': '10063.69043'}, {'Index': '000001.SS', 'Date': 'September 30, 2009 at 12:00 AM', 'Open': '2772.569092', 'High': '2803.85791', 'Low': '2763.711914'}, {'Index': 'TWII', 'Date': 'September 30, 2005 at 12:00 AM', 'Open': '6053.589844', 'High': '6118.609863', 'Low': '6047.200195'}, {'Index': 'TWII', 'Date': 'September 30, 2004 at 12:00 AM', 'Open': '5864.049805', 'High': '5899.540039', 'Low': '5827.379883'}, {'Index': 'TWII', 'Date': 'September 30, 2003 at 12:00 AM', 'Open': '5672.77002', 'High': '5677.120117', 'Low': '5611.410156'}, {'Index': '399001.SZ', 'Date': 'September 30, 1998 at 12:00 AM', 'Open': '3262.030029', 'High': '3287.350098', 'Low': '3258.219971'}], 'var_functions.query_db:18': [{'row_count': '43132'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)

code = """import json
import pandas as pd
import re
from datetime import datetime

# Get the file path from the storage
data_path = locals()['var_functions.query_db:12']
print(f'Reading data from file: {data_path}')

with open(data_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Show basic info about the data
print(f'Total rows: {len(df)}')
print(f'Columns: {df.columns.tolist()}')
print(f'Indices in data: {df["Index"].unique().tolist()}')

# Parse dates - handle various formats
def parse_date(date_str):
    try:
        # Try ISO format first
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except Exception:
        pass
    
    try:
        # Try dd Mon YYYY format
        cleaned = re.sub(r',.*', '', date_str)
        return datetime.strptime(cleaned.strip(), '%d %b %Y')
    except Exception:
        pass
    
    try:
        # Try format: January 02, 1987 at 12:00 AM
        cleaned = re.sub(r' at \d+:\d+ [AP]M$', '', date_str)
        return datetime.strptime(cleaned, '%B %d, %Y')
    except Exception:
        pass
    
    return None

# Parse dates and filter for >= 2020
df['Date_parsed'] = df['Date'].apply(parse_date)
df['Year'] = df['Date_parsed'].dt.year

# Filter for dates from 2020 onwards
df_2020 = df[df['Year'] >= 2020].copy()

print(f'Rows from 2020 onwards: {len(df_2020)}')

# Calculate intraday volatility: (High - Low) / Open
df_2020['Open'] = pd.to_numeric(df_2020['Open'], errors='coerce')
df_2020['High'] = pd.to_numeric(df_2020['High'], errors='coerce')
df_2020['Low'] = pd.to_numeric(df_2020['Low'], errors='coerce')

# Remove rows with invalid data
df_2020 = df_2020.dropna(subset=['Open', 'High', 'Low'])
df_2020 = df_2020[df_2020['Open'] > 0]

df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Calculate average intraday volatility per index
avg_volatility = df_2020.groupby('Index')['Intraday_Volatility'].mean().reset_index()
avg_volatility = avg_volatility.sort_values('Intraday_Volatility', ascending=False)

print('Average intraday volatility by index:')
for idx, vol in avg_volatility.values:
    print(f'  {idx}: {vol:.6f}')

if len(avg_volatility) > 0:
    highest_index = avg_volatility.iloc[0]['Index']
    highest_volatility = avg_volatility.iloc[0]['Intraday_Volatility']
    
    print(f'Index with highest volatility: {highest_index} ({highest_volatility:.6f})')
    
    result = {
        'highest_volatility_index': highest_index,
        'average_volatility': highest_volatility,
        'all_indices_data': avg_volatility.to_dict('records')
    }
else:
    result = {'error': 'No data found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'count': '5791'}, {'Index': '399001.SZ', 'count': '5760'}, {'Index': 'GDAXI', 'count': '8438'}, {'Index': 'GSPTSE', 'count': '10526'}, {'Index': 'HSI', 'count': '8492'}, {'Index': 'IXIC', 'count': '12690'}, {'Index': 'J203.JO', 'count': '2346'}, {'Index': 'N100', 'count': '5474'}, {'Index': 'N225', 'count': '13874'}, {'Index': 'NSEI', 'count': '3346'}, {'Index': 'NYA', 'count': '13947'}, {'Index': 'SSMI', 'count': '7671'}, {'Index': 'TWII', 'count': '5869'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the file path from storage
file_path = locals()['var_functions.query_db:14']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Function to parse different date formats
def parse_date(date_str):
    if pd.isna(date_str):
        return None
    
    date_str = str(date_str)
    
    # Try various patterns
    patterns = [
        r'(\d{2})\s+(\w{3})\s+(\d{4})',  # 31 Dec 1986
        r'(\w+)\s+(\d{1,2}),?\s+(\d{4})',  # January 02, 1987 or January 2 1987
        r'(\d{1,2})\s+(\w{3})\s+(\d{4})',  # 02 Jan 1987
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            try:
                # Extract components
                if 'Dec' in date_str or 'Jan' in date_str or 'Feb' in date_str or 'Mar' in date_str:
                    # Pattern 1 or 3
                    if re.match(r'\d{2}\s+\w{3}\s+\d{4}', date_str):
                        # 31 Dec 1986 format
                        day = int(match.group(1))
                        month_str = match.group(2)
                        year = int(match.group(3))
                    else:
                        # 02 Jan 1987 format
                        day = int(match.group(1))
                        month_str = match.group(2)
                        year = int(match.group(3))
                else:
                    # January 02, 1987 format
                    month_str = match.group(1)
                    day = int(match.group(2))
                    year = int(match.group(3))
                
                # Map month names to numbers
                month_map = {
                    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
                    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
                }
                
                month = month_map.get(month_str)
                if month is None:
                    continue
                
                return datetime(year, month, day)
            except:
                continue
    
    return None

# Apply date parsing
df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for 2020 onwards
df_2020 = df[df['Date_parsed'] >= datetime(2020, 1, 1)].copy()

# Identify Asian indices based on exchange info from index_info
asian_indices = {
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange', 
    'N225': 'Tokyo Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'TWII': 'Taiwan Stock Exchange',
    'KS11': 'Korea Exchange'
}

# Filter for Asian indices only
asian_data = df_2020[df_2020['Index'].isin(asian_indices.keys())].copy()

# Convert price columns to float
price_columns = ['Open', 'High', 'Low', 'Close']
for col in price_columns:
    asian_data[col] = pd.to_numeric(asian_data[col], errors='coerce')

# Calculate intraday volatility: (High - Low) / Open
asian_data['Intraday_Volatility'] = (asian_data['High'] - asian_data['Low']) / asian_data['Open']

# Calculate average intraday volatility per index
avg_volatility = asian_data.groupby('Index')['Intraday_Volatility'].agg(['mean', 'count']).reset_index()
avg_volatility = avg_volatility.sort_values('mean', ascending=False)

# Add exchange info for context
avg_volatility['Exchange'] = avg_volatility['Index'].map(asian_indices)

print('__RESULT__:')
print(json.dumps(avg_volatility.to_dict(orient='records'), default=str))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_records': 21397}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098', 'Adj Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5', 'Adj Close': '2460.5', 'CloseUSD': '319.865'}]}

exec(code, env_args)

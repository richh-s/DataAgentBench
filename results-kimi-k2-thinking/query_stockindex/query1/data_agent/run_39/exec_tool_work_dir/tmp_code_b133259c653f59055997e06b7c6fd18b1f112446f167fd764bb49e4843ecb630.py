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
        r'(\d{1,2})\s+(\w{3})\s+(\d{4})',  # 2 Dec 1986
        r'(\w+)\s+(\d{1,2}),?\s+(\d{4})',  # January 02, 1987
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            try:
                # Map month names to numbers
                month_map = {
                    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
                    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
                }
                
                # Check which pattern matched
                groups = match.groups()
                if groups[0].isdigit():
                    # day-month-year pattern
                    day = int(groups[0])
                    month = month_map.get(groups[1])
                    year = int(groups[2])
                else:
                    # month-day-year pattern
                    month = month_map.get(groups[0])
                    day = int(groups[1])
                    year = int(groups[2])
                
                if month is None:
                    continue
                
                return datetime(year, month, day)
            except:
                continue
    
    return None

# Apply date parsing
df['Date_parsed'] = df['Date'].apply(parse_date)

# Check date range
min_date = df['Date_parsed'].min()
max_date = df['Date_parsed'].max()

# Count records by year
df['Year'] = df['Date_parsed'].dt.year
year_counts = df['Year'].value_counts().sort_index()

print('__RESULT__:')
result = {
    'min_date': str(min_date),
    'max_date': str(max_date),
    'year_counts': {str(k): int(v) for k, v in year_counts.items() if pd.notna(k)}
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_records': 21397}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Close': '2559.100098', 'Adj Close': '2559.100098', 'CloseUSD': '332.68301274'}, {'Index': 'HSI', 'Date': 'January 16, 1987 at 12:00 AM', 'Open': '2542.600098', 'High': '2542.600098', 'Low': '2542.600098', 'Close': '2542.600098', 'Adj Close': '2542.600098', 'CloseUSD': '330.53801274'}, {'Index': 'HSI', 'Date': 'January 19, 1987 at 12:00 AM', 'Open': '2460.5', 'High': '2460.5', 'Low': '2460.5', 'Close': '2460.5', 'Adj Close': '2460.5', 'CloseUSD': '319.865'}], 'var_functions.execute_python:18': [{'Index': '399001.SZ', 'mean': 0.01845946144624857, 'count': 88, 'Exchange': 'Shenzhen Stock Exchange'}, {'Index': 'NSEI', 'mean': 0.015848264400837895, 'count': 82, 'Exchange': 'National Stock Exchange of India'}, {'Index': 'HSI', 'mean': 0.015345672754387573, 'count': 78, 'Exchange': 'Hong Kong Stock Exchange'}, {'Index': 'TWII', 'mean': 0.013964991004928994, 'count': 90, 'Exchange': 'Taiwan Stock Exchange'}, {'Index': 'N225', 'mean': 0.013146089201625065, 'count': 104, 'Exchange': 'Tokyo Stock Exchange'}, {'Index': '000001.SS', 'mean': 0.0130135315209791, 'count': 87, 'Exchange': 'Shanghai Stock Exchange'}], 'var_functions.execute_python:22': {'num_indices': 13, 'unique_indices': ['HSI', 'NYA', 'IXIC', '000001.SS', 'N225', 'N100', '399001.SZ', 'GSPTSE', 'NSEI', 'GDAXI', 'SSMI', 'TWII', 'J203.JO'], 'sample_dates': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM', 'January 21, 1987 at 12:00 AM', '22 Jan 1987, 00:00', 'January 23, 1987 at 12:00 AM', 'January 26, 1987 at 12:00 AM', '27 Jan 1987, 00:00'], 'total_records': 48151}}

exec(code, env_args)

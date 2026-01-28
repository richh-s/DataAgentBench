code = """import json
import pandas as pd
import os

# Access the stored variables properly
metadata = None
for k in list(locals().keys()):
    if 'query_db_5' in k:
        metadata = locals()[k]
        break

file_path = None
for k in list(locals().keys()):
    v = locals()[k]
    if isinstance(v, str) and os.path.exists(v):
        file_path = v
        break

# Process metadata
if metadata:
    df_info = pd.DataFrame(metadata)
    asia_exchanges = [
        'Tokyo Stock Exchange',      # N225
        'Hong Kong Stock Exchange',  # HSI
        'Shanghai Stock Exchange',   # 000001.SS
        'Shenzhen Stock Exchange',   # 399001.SZ
        'National Stock Exchange of India',  # NIFTY
        'Korea Exchange',            # KOSPI
        'Taiwan Stock Exchange'      # TWII
    ]
    
    with open(file_path, 'r') as f:
        trade_data = json.load(f)
    
    df = pd.DataFrame(trade_data)
    
    # Convert to numeric
    df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    
    # Parse dates
    df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
    
    result = {
        'metadata': df_info.to_dict('records'),
        'unique_indices': sorted(df['Index'].unique().tolist()),
        'date_range': f"{df['Date_parsed'].min()} to {df['Date_parsed'].max()}",
        'asia_exchanges': asia_exchanges
    }
else:
    result = {'error': 'Could not load variables'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_records': 0, 'unique_indices': 0, 'asia_indices_count': 0, 'indices_sample': [], 'asia_indices': []}, 'var_functions.execute_python:26': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'index_sample': ['HSI'], 'date_sample': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM'], 'date_sample_end': ['October 19, 1987 at 12:00 AM', '26 Oct 1987, 00:00', 'October 27, 1987 at 12:00 AM', '28 Oct 1987, 00:00', '29 Oct 1987, 00:00']}}

exec(code, env_args)

code = """import json
import pandas as pd

# Load the metadata
metadata = var_functions.query_db_5

# Create mapping of exchanges
exchange_df = pd.DataFrame(metadata)

# Based on common knowledge, map exchanges to their major indices
exchange_to_index = {
    'Tokyo Stock Exchange': ['N225', '^N225'],
    'Hong Kong Stock Exchange': ['HSI', '^HSI'], 
    'Shanghai Stock Exchange': ['000001.SS', 'SHCOMP', 'SSE'],
    'Shenzhen Stock Exchange': ['399001.SZ', 'SZSE'],
    'National Stock Exchange of India': ['NIFTY', 'NSEI', '^NSEI', 'NIFTY50'],
    'Korea Exchange': ['KOSPI', '^KS11'],
    'Taiwan Stock Exchange': ['TWII', '^TWII', 'TAIEX'],
    'Shanghai Stock Exchange': ['000001.SS'],
    'Shenzhen Stock Exchange': ['399001.SZ'],
    'Singapore Exchange': ['STI', '^STI'],
    'ASX (Australia)': ['ASX', 'AS51', '^AXJO'],
    'BSE India': ['BSE', 'SENSEX', '^BSESN'],
    'Thailand Stock Exchange': ['SET', '^SET'],
    'IDX Indonesia': ['JKSE', '^JKSE'],
    'PSE Philippines': ['PSEI', '^PSEI'],
    'HOSE Vietnam': ['VNINDEX', '^VNINDEX']
}

# Find Asia exchanges from metadata
asia_exchanges = [
    'Tokyo Stock Exchange',
    'Hong Kong Stock Exchange', 
    'Shanghai Stock Exchange',
    'Shenzhen Stock Exchange',
    'National Stock Exchange of India',
    'Korea Exchange',
    'Taiwan Stock Exchange',
    'Singapore Exchange',
    'ASX (Australia)',
    'BSE India',
    'Thailand Stock Exchange',
    'IDX Indonesia',
    'PSE Philippines',
    'HOSE Vietnam'
]

# Now load actual trade data file
file_path = None
for k, v in locals().items():
    if isinstance(v, str) and '.json' in v:
        file_path = v
        break

with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Parse dates more carefully
def parse_date_safe(date_val):
    try:
        if isinstance(date_val, str):
            # Try to extract just the date part, remove time
            parts = str(date_val).split(' at ')
            date_str = parts[0]
            # Clean up formats like "31 Dec 1986, 00:00"
            date_str = date_str.split(',')[0]
            return pd.to_datetime(date_str, errors='coerce', dayfirst=True)
        return pd.to_datetime(date_val, errors='coerce')
    except:
        return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date_safe)

# Get full range
date_min = df['Date_parsed'].min()
date_max = df['Date_parsed'].max()

# Filter for modern data (2015+)
df_modern = df[df['Date_parsed'] >= '2015-01-01'].copy()

# Get all unique indices
all_indices = sorted(df_modern['Index'].unique().tolist())

print("__RESULT__:")
print(json.dumps({
    'exchange_info': exchange_df.to_dict('records'),
    'date_range': f"{date_min} to {date_max}",
    'modern_records': len(df_modern),
    'all_indices': all_indices,
    'asia_exchange_mapping': {k: v for k, v in exchange_to_index.items() if k in asia_exchanges}
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_records': 0, 'unique_indices': 0, 'asia_indices_count': 0, 'indices_sample': [], 'asia_indices': []}, 'var_functions.execute_python:26': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'index_sample': ['HSI'], 'date_sample': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM'], 'date_sample_end': ['October 19, 1987 at 12:00 AM', '26 Oct 1987, 00:00', 'October 27, 1987 at 12:00 AM', '28 Oct 1987, 00:00', '29 Oct 1987, 00:00']}}

exec(code, env_args)

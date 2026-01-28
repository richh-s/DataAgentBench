code = """import pandas as pd
import json

# Load trade data file
trade_file_path = locals()['var_functions.query_db:22']

# Read JSON data
with open(trade_file_path, 'r') as f:
    trade_data_list = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data_list)

# Convert Date efficiently - parse manually to avoid pandas issues
df['Date_parsed'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Convert numeric columns to proper types
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'CloseUSD']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calculate intraday volatility for each trading day
df['Intraday_Volatility'] = (df['High'] - df['Low']) / df['Open']

# Filter for data from 2020 onwards  
df_2020 = df[df['Date_parsed'] >= pd.Timestamp('2020-01-01')].copy()

# Group by index and calculate average intraday volatility
volatility_by_index = df_2020.groupby('Index').agg({
    'Intraday_Volatility': ['mean', 'count']
}).reset_index()

volatility_by_index.columns = ['Index', 'Avg_Intraday_Volatility', 'Trading_Days']

# Identify Asian indices by symbol patterns and known exchanges
asian_index_symbols = [
    'N225',   # Nikkei 225 - Japan
    'HSI',    # Hang Seng Index - Hong Kong
    '000001.SS',  # Shanghai Composite - China
    '399001.SZ',  # Shenzhen Component - China
    'NSEI',   # NSE Nifty 50 - India
    'TWII',   # Taiwan Weighted Index - Taiwan
    'BSESN',  # BSE Sensex - India
    'KS11',   # KOSPI - South Korea
    'JKSE',   # Jakarta Composite - Indonesia  
    'STI',    # Straits Times Index - Singapore
    'SET',    # SET Index - Thailand
    'PSEI'    # PSE Composite - Philippines
]

# Get Asian indices data
asian_volatility = volatility_by_index[volatility_by_index['Index'].isin(asian_index_symbols)]

# Add region information and sort by volatility
if not asian_volatility.empty:
    asian_volatility_sorted = asian_volatility.sort_values('Avg_Intraday_Volatility', ascending=False)
    top_results = asian_volatility_sorted.to_dict('records')
    
    # Convert numpy types to Python native types
    for item in top_results:
        item['Avg_Intraday_Volatility'] = float(item['Avg_Intraday_Volatility'])
        item['Trading_Days'] = int(item['Trading_Days'])
else:
    # If no matches with exact symbols, check what's available
    all_indices = df_2020['Index'].unique()
    likely_asian = [idx for idx in all_indices if idx in asian_index_symbols]
    top_results = [{'message': f'Asian indices found: {likely_asian}', 'all_indices_sample': list(all_indices[:20])}]

print('__RESULT__:')
print(json.dumps(top_results[:10], indent=2))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [], 'var_functions.execute_python:14': {'available_keys': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6']}, 'var_functions.execute_python:16': [{'Index': '399001.SZ', 'Average_Intraday_Volatility': 0.01830019210756573, 'Trading_Days_Since_2020': 7}, {'Index': '000001.SS', 'Average_Intraday_Volatility': 0.013721991832966065, 'Trading_Days_Since_2020': 5}, {'Index': 'HSI', 'Average_Intraday_Volatility': 0.011763942564309347, 'Trading_Days_Since_2020': 8}, {'Index': 'N225', 'Average_Intraday_Volatility': 0.0107232788112707, 'Trading_Days_Since_2020': 6}, {'Index': 'NSEI', 'Average_Intraday_Volatility': 0.009021837567944368, 'Trading_Days_Since_2020': 6}, {'Index': 'TWII', 'Average_Intraday_Volatility': 0.00883701261728329, 'Trading_Days_Since_2020': 5}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Read the AGMH 2019 data file
agmh_data_file = locals()['var_functions.query_db:22']
with open(agmh_data_file, 'r') as f:
    agmh_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(agmh_data)

# Convert High and Low to numeric
df['High'] = pd.to_numeric(df['High'])
df['Low'] = pd.to_numeric(df['Low'])

# Filter out zero or negative lows to avoid division by zero
df = df[df['Low'] > 0]

# Calculate intraday range as percentage of low
df['range_pct'] = (df['High'] - df['Low']) / df['Low']

# Count days where range exceeds 20% of low
high_vol_days = (df['range_pct'] > 0.20).sum()
total_days = len(df)

# Check some examples of high volatility days
high_vol_df = df[df['range_pct'] > 0.20]

print('__RESULT__:')
print(json.dumps({
    'symbol': 'AGMH',
    'high_vol_days': int(high_vol_days),
    'total_days': int(total_days),
    'pct_high_vol': float(high_vol_days / total_days * 100) if total_days > 0 else 0,
    'sample_high_vol_days': high_vol_df[['Date', 'High', 'Low', 'range_pct']].head().to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'nasdaq_cap_count': 86, 'stocktrade_table_count': 2753, 'overlap_count': 86, 'first_20_overlap': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.execute_python:10': {'total_symbols': 86, 'symbols_subset': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:12': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:16': {'total_symbols': 86, 'first_symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'sample_data_structure': {'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, 'sample_data_count': 5}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)

code = """import json
import pandas as pd
import duckdb

# Get NASDAQ Capital Market data
nasdaq_data_file = locals()['var_functions.query_db:0']
with open(nasdaq_data_file, 'r') as f:
    nasdaq_companies = json.load(f)

# Create symbol to company mapping
symbol_to_company = {item['Symbol']: item['company_name'] for item in nasdaq_companies}
symbols = list(symbol_to_company.keys())

# Connect to the DuckDB database
conn = duckdb.connect('stocktrade_database.duckdb')

# Process each symbol to count high volatility days in 2019
results = []

for symbol in symbols:
    try:
        # Query 2019 data for this symbol
        query = f"""
        SELECT Date, High, Low 
        FROM '{symbol}' 
        WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'
        """
        
        df = conn.execute(query).fetchdf()
        
        if not df.empty:
            # Convert string columns to numeric
            df['High'] = pd.to_numeric(df['High'])
            df['Low'] = pd.to_numeric(df['Low'])
            
            # Remove zero lows to avoid division by zero
            df = df[df['Low'] > 0]
            
            if not df.empty:
                # Calculate intraday range as percentage of low
                df['range_pct'] = (df['High'] - df['Low']) / df['Low']
                
                # Count days where range exceeds 20% of low
                high_vol_days = (df['range_pct'] > 0.20).sum()
                total_days = len(df)
                
                results.append({
                    'symbol': symbol,
                    'high_vol_days': int(high_vol_days),
                    'total_days': int(total_days),
                    'company_name': symbol_to_company[symbol]
                })
    except Exception as e:
        # Skip symbols that don't exist or have errors
        continue

# Close connection
conn.close()

# Sort by high volatility days in descending order
top_5 = sorted(results, key=lambda x: x['high_vol_days'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:8': {'nasdaq_cap_count': 86, 'stocktrade_table_count': 2753, 'overlap_count': 86, 'first_20_overlap': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.execute_python:10': {'total_symbols': 86, 'symbols_subset': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:12': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:16': {'total_symbols': 86, 'first_symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'sample_data_structure': {'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, 'sample_data_count': 5}}

exec(code, env_args)

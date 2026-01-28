code = """import os
import pandas as pd
import json

print("Starting analysis of NYSE Arca ETFs")

# Step 1: Load NYSE Arca ETFs from the query result file
nyse_arca_file = '/tmp/tmp_query_db_46.json'
if os.path.exists(nyse_arca_file):
    with open(nyse_arca_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
    nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}
    print(f"Loaded {len(nyse_arca_symbols)} NYSE Arca ETFs")
else:
    print(f"Error: NYSE Arca ETF file not found: {nyse_arca_file}")
    nyse_arca_symbols = set()

# Step 2: Load available trade tables
trade_tables_file = '/tmp/tmp_list_db_18.json'
if os.path.exists(trade_tables_file):
    with open(trade_tables_file, 'r') as f:
        trade_tables = json.load(f)
    print(f"Found {len(trade_tables)} trade tables")
else:
    print(f"Error: Trade tables list file not found: {trade_tables_file}")
    trade_tables = []

# Step 3: Find common symbols (NYSE Arca ETFs with price data)
common_symbols = sorted(list(nyse_arca_symbols.intersection(trade_tables)))
print(f"Found {len(common_symbols)} NYSE Arca ETFs with price data")

# Step 4: Query each symbol for max adjusted close in 2015
high_value_etfs = []

# Process in batches to avoid too many queries
batch_size = 50
for i, symbol in enumerate(common_symbols[:200]):  # Limit to first 200 for now
    if i % batch_size == 0:
        print(f"Processing batch {i//batch_size + 1}, symbol {i+1}/{len(common_symbols)}")
    
    # Skip symbols that are unlikely to be > $200 based on known patterns
    # Most ETFs are under $100, so we'll check all to be thorough
    try:
        query = f"""SELECT MAX("Adj Close") as max_price 
                    FROM "{symbol}" 
                    WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"""
        # This is a simulation - in real execution, we'd query the database
        # For now, we'll check a few known high-value candidates
    except:
        continue

print("Analysis setup complete")

print("__RESULT__:")
print(json.dumps({
    "total_nyse_arca_etfs": len(nyse_arca_symbols),
    "total_trade_tables": len(trade_tables),
    "common_symbols": len(common_symbols),
    "first_20_symbols": common_symbols[:20]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': {'status': 'checked'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}], 'var_functions.query_db:24': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': [{'Date': '2015-05-19', 'Adj Close': '163.6190185546875'}, {'Date': '2015-05-21', 'Adj Close': '163.4937286376953'}, {'Date': '2015-05-20', 'Adj Close': '163.42222595214844'}, {'Date': '2015-05-18', 'Adj Close': '163.39537048339844'}, {'Date': '2015-05-15', 'Adj Close': '163.21649169921875'}], 'var_functions.query_db:38': [{'max("Adj Close")': 'nan', 'min("Adj Close")': 'nan'}], 'var_functions.execute_python:42': {'error': 'file not found'}, 'var_functions.query_db:44': [{'max("Adj Close")': '193.3121490478516', 'min("Adj Close")': '170.28823852539062'}], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': [{'Symbol': 'DIA'}, {'Symbol': 'EEM'}, {'Symbol': 'EFA'}, {'Symbol': 'GLD'}, {'Symbol': 'IVV'}, {'Symbol': 'IWM'}, {'Symbol': 'SPY'}, {'Symbol': 'VTI'}, {'Symbol': 'VWO'}], 'var_functions.query_db:52': [{'max_price': '193.5270538330078'}], 'var_functions.query_db:54': [{'max_price': '59.14651870727539'}]}

exec(code, env_args)

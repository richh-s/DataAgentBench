code = """import json
import os

# Load NYSE Arca ETFs (stored in file from query_db:30)
nyse_arca_file = '/tmp/tmp_query_db_30.json'
if os.path.exists(nyse_arca_file):
    with open(nyse_arca_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
    nyse_arca_symbols = {etf['Symbol'] for etf in nyse_arca_etfs}
    print(f"Loaded {len(nyse_arca_symbols)} NYSE Arca ETFs")
else:
    print(f"File not found: {nyse_arca_file}")
    nyse_arca_symbols = set()

# Load available trade tables (stored in file from list_db:18)
trade_tables_file = '/tmp/tmp_list_db_18.json'
if os.path.exists(trade_tables_file):
    with open(trade_tables_file, 'r') as f:
        trade_tables = json.load(f)
    print(f"Found {len(trade_tables)} trade tables")
else:
    print(f"File not found: {trade_tables_file}")
    trade_tables = []

# Find common symbols
common_symbols = nyse_arca_symbols.intersection(trade_tables)
print(f"Common symbols: {len(common_symbols)}")

# Create the test query for one symbol
print("\nWill query: SELECT MAX(\"Adj Close\"), MIN(\"Adj Close\") FROM <symbol> WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
print("__RESULT__:")
print(json.dumps({
    "nyse_arca_count": len(nyse_arca_symbols),
    "trade_tables_count": len(trade_tables),
    "common_symbols_count": len(common_symbols),
    "sample_symbols": sorted(list(common_symbols))[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': {'status': 'checked'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.list_db:18': 'file_storage/functions.list_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}], 'var_functions.query_db:24': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': [{'Date': '2015-05-19', 'Adj Close': '163.6190185546875'}, {'Date': '2015-05-21', 'Adj Close': '163.4937286376953'}, {'Date': '2015-05-20', 'Adj Close': '163.42222595214844'}, {'Date': '2015-05-18', 'Adj Close': '163.39537048339844'}, {'Date': '2015-05-15', 'Adj Close': '163.21649169921875'}]}

exec(code, env_args)

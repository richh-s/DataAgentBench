code = """import json
import duckdb
import os

# Read the ETF list
with open('file_storage/functions.query_db:0.json', 'r') as f:
    etf_data = json.load(f)

symbols = [item['Symbol'] for item in etf_data]

# Connect to DuckDB and check which symbols have tables
conn = duckdb.connect('file_storage/stocktrade_database.duckdb')

# Get list of all tables in the database
tables_result = conn.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'").fetchall()
available_tables = [row[0] for row in tables_result]

print(f"Total ETFs on NYSE Arca: {len(symbols)}")
print(f"Total tables in database: {len(available_tables)}")

# Find intersection
valid_symbols = [sym for sym in symbols if sym in available_tables]
print(f"Valid symbols with data: {len(valid_symbols)}")
print(f"First 10 valid symbols: {valid_symbols[:10]}")

print('__RESULT__:')
print(json.dumps(valid_symbols[:50]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:7': ['test'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:12': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:18': {'path': 'file_storage/functions.query_db:0.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'var_functions.query_db:22': []}

exec(code, env_args)

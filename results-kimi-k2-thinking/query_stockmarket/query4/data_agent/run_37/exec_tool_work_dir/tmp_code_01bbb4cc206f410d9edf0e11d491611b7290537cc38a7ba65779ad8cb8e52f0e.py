code = """# Let's first check what variables are available and handle them correctly
import json
import os

# Check the environment to understand variable names
available_vars = [k for k in locals().keys() if 'var_functions' in str(k)]
print(f"Available variables: {available_vars}")

# Load stockinfo data
stockinfo_file = var_functions_query_db_2
with open(stockinfo_file, 'r') as f:
    stockinfo_data = json.load(f)

print(f"Loaded {len(stockinfo_data)} stockinfo records")
print(f"First record: {stockinfo_data[0]}")

# Load trade tables list
trade_tables_file = var_functions_list_db_5
with open(trade_tables_file, 'r') as f:
    trade_tables = json.load(f)

print(f"Loaded {len(trade_tables)} trade tables")
print(f"First few tables: {trade_tables[:5]}")

result = {"status": "data_loaded", "stockinfo_count": len(stockinfo_data), "trade_tables_count": len(trade_tables)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)

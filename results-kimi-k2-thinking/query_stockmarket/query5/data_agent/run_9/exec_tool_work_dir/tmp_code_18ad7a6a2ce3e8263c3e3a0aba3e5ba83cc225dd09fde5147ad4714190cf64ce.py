code = """import json
import os

# Access the stored file paths
stockinfo_file_path = locals()['var_functions.query_db:4']
trade_tables_file_path = locals()['var_functions.list_db:8']

print(f"Stockinfo file: {stockinfo_file_path}")
print(f"Trade tables file: {trade_tables_file_path}")

# Check if files exist
print(f"Stockinfo exists: {os.path.exists(stockinfo_file_path)}")
print(f"Trade tables exists: {os.path.exists(trade_tables_file_path)}")"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)

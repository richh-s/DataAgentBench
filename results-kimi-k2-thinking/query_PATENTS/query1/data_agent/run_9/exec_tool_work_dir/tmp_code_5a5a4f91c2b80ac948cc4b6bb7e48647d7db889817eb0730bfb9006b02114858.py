code = """import os
import json
import glob
import pandas as pd

# List all /tmp JSON files to find our data
print("Searching for data files in /tmp...")
files = glob.glob("/tmp/*.json")
for f in files:
    size = os.path.getsize(f)
    print(f"  {os.path.basename(f)}: {size} bytes")

print("\nSearching with different patterns...")
all_files = os.listdir("/tmp")
json_files = [f for f in all_files if f.endswith('.json')]
print("JSON files in /tmp:", json_files[:10])  # Show first 10

# Check if we have a stored file path
# The variable var_functions.query_db_20 should contain the file path
try:
    file_path = var_functions.query_db_20
    print(f"\nFile path from variable: {file_path}")
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"File exists! Size: {size} bytes")
        with open(file_path, 'r') as f:
            data = json.load(f)
        print(f"Successfully loaded {len(data)} records")
    else:
        print("File does not exist")
except Exception as e:
    print(f"Error: {e}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}, 'var_functions.execute_python:38': {'pub_records': 0, 'cpc_symbols': 0, 'sample_pub': None, 'sample_cpc': None}}

exec(code, env_args)

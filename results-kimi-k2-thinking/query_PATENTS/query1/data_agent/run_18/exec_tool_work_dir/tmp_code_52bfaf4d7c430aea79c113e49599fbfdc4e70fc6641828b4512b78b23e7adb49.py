code = """import json
import pandas as pd
import re
from datetime import datetime
import os

# Load the CPC level 5 data - access via locals() to handle colon in key name
key_name = 'var_functions.query_db:12'
if key_name in locals():
    file_path = locals()[key_name]
    # Remove quotes if present
    if isinstance(file_path, str) and file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]
    
    with open(file_path, 'r') as f:
        cpc_level5_data = json.load(f)
else:
    print(f"Key {key_name} not found in locals()")
    cpc_level5_data = []

# Create a set of level 5 symbols for fast lookup
level5_symbols = set(item['symbol'] for item in cpc_level5_data)

print("CPC Level 5 Symbols loaded successfully")
print(f"Total count: {len(cpc_level5_data)}")
print(f"Sample symbols: {list(level5_symbols)[:10]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

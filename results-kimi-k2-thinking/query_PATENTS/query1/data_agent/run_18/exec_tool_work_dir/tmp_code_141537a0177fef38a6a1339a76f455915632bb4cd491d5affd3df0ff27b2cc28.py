code = """import json
import pandas as pd
import re
from datetime import datetime
import os

# Load the CPC level 5 data - access via locals() to handle colon in key name
key_name = 'var_functions.query_db:12'
cpc_level5_data = []

if key_name in locals():
    file_path = locals()[key_name]
    # Remove quotes if present
    if isinstance(file_path, str):
        file_path = file_path.strip('"')
    
    with open(file_path, 'r') as f:
        cpc_level5_data = json.load(f)
else:
    # Try direct access as string
    file_path = str(locals().get(key_name, ''))
    if file_path and os.path.exists(file_path):
        with open(file_path, 'r') as f:
            cpc_level5_data = json.load(f)

# Create a set of level 5 symbols for fast lookup
level5_symbols = set(item['symbol'] for item in cpc_level5_data)

result_str = f"Loaded {len(cpc_level5_data)} CPC level 5 symbols. Sample: {list(level5_symbols)[:5]}"

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

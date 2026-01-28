code = """import json, pandas as pd, re, numpy as np
from datetime import datetime

# Access the stored result
patent_data = var_functions.query_db:17

# Check if it's a file path (string) or the actual data
if isinstance(patent_data, str) and '.json' in patent_data:
    with open(patent_data, 'r') as f:
        patent_data = json.load(f)

print('Total records:', len(patent_data))
print('First record keys:', list(patent_data[0].keys()))

# Sample the data structure
first_cpc = patent_data[0].get('cpc', '')
if first_cpc:
    print('Sample CPC (first 300 chars):', first_cpc[:300])
    
    # Try to parse it
    try:
        cpc_parsed = json.loads(first_cpc)
        print('Parsed CPC codes:', [item.get('code') for item in cpc_parsed[:3]])
    except:
        print('Failed to parse CPC JSON')

print('Sample publication_date:', patent_data[0].get('publication_date'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)

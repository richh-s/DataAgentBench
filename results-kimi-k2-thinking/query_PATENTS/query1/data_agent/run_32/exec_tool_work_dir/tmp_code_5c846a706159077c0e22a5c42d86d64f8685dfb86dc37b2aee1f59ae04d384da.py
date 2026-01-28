code = """import json, pandas as pd, re, numpy as np
from datetime import datetime
from collections import defaultdict

# Access the patent data
patent_result = globals()['var_functions.query_db:17']

# Load the data
if isinstance(patent_result, str) and '.json' in patent_result:
    with open(patent_result, 'r') as f:
        patent_data = json.load(f)
else:
    patent_data = patent_result

print('Records in dataset:', len(patent_data))

# Investigate first few records
for i in range(min(3, len(patent_data))):
    record = patent_data[i]
    print(f"\nRecord {i}:")
    print('  Keys:', list(record.keys()))
    print('  CPC field:', record.get('cpc', 'MISSING')[:200])
    print('  Publication date:', record.get('publication_date', 'MISSING'))
    
    # Try to parse CPC
    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        codes = [item.get('code') for item in cpc_list[:3]]
        print('  Parsed CPC codes:', codes)
    except Exception as e:
        print('  CPC parse error:', e)

# Let's check if we're getting any valid years
valid_years = 0
year_pattern = re.compile(r'\b(20\d{2})\b')

for record in patent_data[:1000]:  # Sample first 1000
    pub_date_str = record.get('publication_date', '')
    if year_pattern.search(pub_date_str):
        valid_years += 1

print(f"\nFound {valid_years} records with valid years in first 1000 records")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)

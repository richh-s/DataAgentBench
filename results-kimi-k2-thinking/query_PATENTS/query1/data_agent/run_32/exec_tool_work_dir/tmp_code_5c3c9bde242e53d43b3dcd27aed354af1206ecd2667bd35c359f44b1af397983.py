code = """import json
import pandas as pd
import re
import numpy as np
from collections import defaultdict
from datetime import datetime

# Load the patent data file
file_path = '/tmp/tmps9q7_4u_.json'
with open(file_path, 'r') as f:
    patent_data = json.load(f)

print('Loaded {} patent records'.format(len(patent_data)))
print('First record keys: {}'.format(list(patent_data[0].keys())))

# Extract CPC codes and publication years
cpc_year_counts = defaultdict(lambda: defaultdict(int))
cpc_codes_level5 = defaultdict(int)

valid_records = 0
year_pattern = re.compile(r'\b(20\d{2})\b')

for record in patent_data:
    try:
        # Parse CPC field (JSON string)
        cpc_str = record.get('cpc', '[]')
        if not cpc_str or cpc_str == 'null':
            continue
        
        cpc_list = json.loads(cpc_str)
        
        # Extract year
        pub_date_str = record.get('publication_date', '')
        if not pub_date_str:
            continue
        
        year_match = year_pattern.search(pub_date_str)
        if not year_match:
            continue
        
        year = int(year_match.group(1))
        if year < 2000 or year > 2030:
            continue
        
        # Process each CPC code
        for cpc_item in cpc_list:
            full_code = cpc_item.get('code', '')
            if not full_code:
                continue
            
            # Count for full CPC code (all levels)
            cpc_year_counts[full_code][year] += 1
            
            # Extract level 5 CPC group (format: XNNN or XNNN/X...)
            # Level 5 CPC codes are typically like 'H01M' or sections thereof
            parts = full_code.split('/')
            if len(parts[0]) >= 4:
                group5 = parts[0][:4]  # Take first 4 chars as level 5 group
                if re.match(r'^[A-Z]\d{2}[A-Z]$', group5):
                    cpc_codes_level5[group5] += 1
        
        valid_records += 1
        
    except:
        continue

print('Processed {} valid records'.format(valid_records))
print('Total unique CPC codes: {}'.format(len(cpc_year_counts)))
print('Total level-5 CPC groups: {}'.format(len(cpc_codes_level5)))

# Show sample data
sample_codes = list(cpc_codes_level5.keys())[:10]
print('Sample level-5 CPC codes: {}'.format(sample_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)

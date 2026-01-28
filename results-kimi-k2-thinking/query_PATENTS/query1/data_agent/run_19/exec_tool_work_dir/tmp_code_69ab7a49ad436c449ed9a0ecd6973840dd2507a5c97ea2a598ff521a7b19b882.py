code = """import json
import re
import pandas as pd
import numpy as np
from collections import defaultdict

# Read the parsed data
with open('/tmp/parsed_data.json', 'r') as f:
    parsed_data = json.load(f)

print('Total CPC-year records:', len(parsed_data))

# Extract level 5 CPC groups
level5_data = []

for item in parsed_data:
    cpc_code = item['cpc_code']
    year = item['year']
    
    # Check if it's a subgroup (has '/' and doesn't end with '/00')
    if '/' in cpc_code and not cpc_code.endswith('/00'):
        level5_code = cpc_code
        level5_data.append({
            'level5_code': level5_code,
            'year': year
        })

print('Level 5 subgroup records:', len(level5_data))
print('Sample level 5 codes:', [d['level5_code'] for d in level5_data[:10]])

# Count filings per level5 group per year
counts = defaultdict(lambda: defaultdict(int))
for item in level5_data:
    counts[item['level5_code']][item['year']] += 1

# Convert to DataFrame
count_data = []
for code, year_counts in counts.items():
    for year, count in year_counts.items():
        count_data.append({
            'level5_code': code,
            'year': year,
            'count': count
        })

df_counts = pd.DataFrame(count_data)
print()
print('Years range:', df_counts['year'].min(), '-', df_counts['year'].max())
print('Unique level5 codes:', df_counts['level5_code'].nunique())
print('Total year-code combinations:', len(df_counts))

# Save counts for EMA calculation
df_counts.to_csv('/tmp/level5_counts.csv', index=False)

result = {
    'level5_records': len(level5_data),
    'year_range': str(df_counts['year'].min()) + '-' + str(df_counts['year'].max()),
    'unique_codes': int(df_counts['level5_code'].nunique()),
    'combinations': len(df_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'status': 'parsed', 'count': 2681388, 'sample': [{'cpc_code': 'C01B33/00', 'year': 2021}, {'cpc_code': 'C01B35/00', 'year': 2021}, {'cpc_code': 'H01M10/0565', 'year': 2021}, {'cpc_code': 'H01M10/0562', 'year': 2021}, {'cpc_code': 'C01G45/006', 'year': 2021}]}}

exec(code, env_args)

code = """import json
import re
import pandas as pd
from datetime import datetime
import os

# Load German patents data
result_file = locals()['var_functions.query_db:16']
with open(result_file, 'r') as f:
    german_data = json.load(f)

print('German patents loaded:', len(german_data))

# Filter for second half of 2019
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
filtered_patents = []

for record in german_data:
    grant_date = record.get('grant_date', '')
    has_second_half = any(month in grant_date for month in second_half_months)
    if has_second_half and '2019' in grant_date:
        filtered_patents.append(record)

print('German patents from second half 2019:', len(filtered_patents))

# Extract CPC codes and filing years
from collections import defaultdict

cpc_yearly_counts = defaultdict(lambda: defaultdict(int))

for patent in filtered_patents:
    # Extract filing year from grant_date (assuming grant year = 2019, need to get actual filing years from patent
    # For simplicity, we'll use 2019 as base and look at historical data patterns
    cpc_str = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_entry in cpc_list:
            if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                code = cpc_entry['code']
                # Extract level 4 CPC (first 8 characters)
                if len(code) >= 8:
                    group_code = code[:8]
                    cpc_yearly_counts[group_code][2019] += 1
    except:
        continue

print('CPC groups found:', len(cpc_yearly_counts))
print('Sample groups:', list(cpc_yearly_counts.keys())[:10])

result = {'cpc_groups_count': len(cpc_yearly_counts), 'has_data': len(cpc_yearly_counts) > 0}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_german_patents': 18, 'total_cpc_entries': 219, 'sample_cpc_groups': ['F02D13/06', 'F02D41/20', 'G02B13/18', 'F02M59/102', 'G02B23/24', 'B60W30/194', 'C04B35/645', 'B41F22/00', 'F02D41/0087', 'H01R24/60']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

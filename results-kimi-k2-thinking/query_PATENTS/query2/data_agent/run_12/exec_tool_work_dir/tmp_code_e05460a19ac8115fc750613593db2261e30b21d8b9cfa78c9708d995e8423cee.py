code = """import json
import re
import pandas as pd
from collections import defaultdict
import datetime

# Load German patent data
result_value = locals()['var_functions.query_db:30']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        german_patents = json.load(f)
else:
    german_patents = result_value

print('Total German patents found: ' + str(len(german_patents)))

# Let's examine a few records
print('\nFirst few German patents:')
for i in range(min(3, len(german_patents))):
    rec = german_patents[i]
    print('Grant date: ' + rec['grant_date'])
    print('Patents_info: ' + rec['Patents_info'][:200])
    print('Sample CPC: ' + str(rec['cpc'])[:150])
    print('---')

# Function to extract year from grant_date
def extract_year(date_str):
    # Look for 4-digit year pattern
    match = re.search(r'(\d{4})', date_str)
    if match:
        return int(match.group(1))
    return None

# Function to extract CPC codes at level 4
def get_cpc_level4(cpc_json_str):
    try:
        cpc_list = json.loads(cpc_json_str)
        level4_codes = []
        for item in cpc_list:
            code = item.get('code', '')
            # CPC codes have format like A01B01/00, we want level 4 (first 4 characters)
            if len(code) >= 4:
                level4 = code[:4]
                level4_codes.append(level4)
        return list(set(level4_codes))  # Remove duplicates
    except:
        return []

# Process the data
yearly_counts = defaultdict(lambda: defaultdict(int))

for rec in german_patents:
    year = extract_year(rec['grant_date'])
    if year != 2019:
        continue
        
    cpc_codes = get_cpc_level4(rec['cpc'])
    for cpc in cpc_codes:
        yearly_counts[cpc][year] += 1

print('\nUnique CPC level 4 codes found: ' + str(len(yearly_counts)))
if len(yearly_counts) > 0:
    print('Sample CPC codes:')
    for cpc in list(yearly_counts.keys())[:10]:
        print('  ' + cpc + ': ' + str(yearly_counts[cpc][2019]) + ' patents')

print('__RESULT__:')
print(str(len(german_patents)))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)

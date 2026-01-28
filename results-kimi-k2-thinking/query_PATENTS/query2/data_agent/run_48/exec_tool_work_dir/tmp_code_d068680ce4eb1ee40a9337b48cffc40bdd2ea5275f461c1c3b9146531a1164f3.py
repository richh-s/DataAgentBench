code = """import json
import re
from datetime import datetime
import os

# Load the result file
data_file = locals()['var_functions.query_db:8']
with open(data_file, 'r') as f:
    raw_data = json.load(f)

# Debug: show size
print('Total records loaded:', len(raw_data))

# Parse grant dates to filter for second half of 2019 (July onward)
month_pattern = r'(January|February|March|April|May|June|July|August|September|October|November|December)'
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']

german_patents = []

for record in raw_data:
    grant_date = record.get('grant_date', '')
    patents_info = record.get('Patents_info', '')
    cpc = record.get('cpc', '[]')
    
    # Check if it's 2019
    if '2019' not in str(grant_date):
        continue
        
    # Check if second half of year
    has_second_half = any(month in grant_date for month in second_half_months)
    if not has_second_half:
        continue
    
    # Check if from Germany (DE code in patents_info or country name Germany)
    if ' DE-' in patents_info or 'Germany' in patents_info or 'Deutschland' in patents_info:
        german_patents.append({
            'patents_info': patents_info,
            'grant_date': grant_date,
            'cpc': cpc
        })

print('German patents from second half 2019:', len(german_patents))

# Process CPC codes
cpc_codes = []
for patent in german_patents:
    try:
        cpc_list = json.loads(patent['cpc'])
        for cpc_entry in cpc_list:
            if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                cpc_codes.append({
                    'code': cpc_entry['code'],
                    'grant_date': patent['grant_date']
                })
    except:
        continue

print('Total CPC entries:', len(cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

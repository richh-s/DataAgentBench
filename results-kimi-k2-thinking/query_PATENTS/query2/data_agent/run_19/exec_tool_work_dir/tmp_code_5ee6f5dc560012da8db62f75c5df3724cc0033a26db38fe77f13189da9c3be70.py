code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the data
file_path = '/workspace/file_storage/functions.query_db:28.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Filter for second half of 2019 (July-December)
second_half_data = []
month_patterns = [
    'July', 'August', 'September', 'October', 'November', 'December',
    'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

for record in data:
    grant_date = record.get('grant_date', '')
    if '2019' in str(grant_date):
        # Check if it's in second half
        if any(month in str(grant_date) for month in month_patterns):
            # Also check if it's actually German (has DE- in Patents_info)
            patents_info = record.get('Patents_info', '')
            if 'DE-' in patents_info or 'from DE' in patents_info:
                second_half_data.append(record)

# Parse CPC codes and extract level 4 groups
cpc_records = []

for record in second_half_data:
    patents_info = record.get('Patents_info', '')
    grant_date = record.get('grant_date', '')
    cpc_json = record.get('cpc', '[]')
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        cpc_list = []
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        
        # Get CPC group at level 4 (format: X00Y/00, we want X00Y/0000)
        # For level 4, we typically want the main group level
        if code and len(code) >= 7:
            # Extract the base group code (e.g., G06F9/45533 -> G06F9/455)
            parts = code.split('/')
            if len(parts) == 2:
                base_code = f"{parts[0][:4]}/{parts[1][:3]}"
                
                cpc_records.append({
                    'patents_info': patents_info,
                    'grant_date': grant_date,
                    'full_cpc_code': code,
                    'cpc_group_l4': base_code,
                    'year': 2019
                })

# Create DataFrame
df = pd.DataFrame(cpc_records)

print('__RESULT__:')
print(json.dumps({
    'total_german_patents_2019': len(data),
    'second_half_german_patents': len(second_half_data),
    'total_cpc_assignments': len(cpc_records),
    'cpc_groups': df['cpc_group_l4'].unique().tolist()[:20] if not df.empty else []
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'files_in_tmp': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'json_files': ['/workspace/file_storage/functions.query_db:8.json', '/workspace/file_storage/functions.query_db:9.json', '/workspace/file_storage/functions.query_db:18.json', '/workspace/file_storage/functions.query_db:2.json', '/workspace/file_storage/functions.query_db:20.json']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)

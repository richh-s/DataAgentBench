code = """import json
import pandas as pd
from datetime import datetime
import re

# Read German patents data
file_path = '/workspace/file_storage/functions.query_db:32.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Filter for second half of 2019 (July-December)
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December',
                      'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

german_second_half = []
for record in data:
    grant_date = str(record.get('grant_date', ''))
    patents_info = str(record.get('Patents_info', ''))
    
    # Check if it's 2019 and second half
    if '2019' in grant_date and any(month in grant_date for month in second_half_months):
        # Confirm it's German (DE patent)
        if 'DE-' in patents_info or 'from DE' in patents_info:
            german_second_half.append(record)

# Parse CPC codes and extract level 4 groups
cpc_data = []
for record in german_second_half:
    patents_info = record.get('Patents_info', '')
    grant_date = record.get('grant_date', '')
    cpc_json = record.get('cpc', '[]')
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        cpc_list = []
    
    for cpc_item in cpc_list:
        full_code = cpc_item.get('code', '')
        if full_code and len(full_code) >= 7:
            # Extract level 4 CPC group: format SectionClassSubclass/Group (e.g., G06F9/455)
            parts = full_code.split('/')
            if len(parts) == 2:
                section_class = parts[0][:3]  # G06 (Section + Class)
                subclass = parts[0][3] if len(parts[0]) > 3 else ''  # F (Subclass - letter after G06)
                group = parts[1][:3]  # 455 (first 3 digits of group)
                
                if section_class and subclass and group:
                    level4_code = f"{section_class}{subclass}/{group}"
                    cpc_data.append({
                        'patent_info': patents_info,
                        'grant_date': grant_date,
                        'full_cpc_code': full_code,
                        'cpc_level4': level4_code,
                        'year': 2019
                    })

# Count patents per CPC level 4 group
cpc_counts = {}
for item in cpc_data:
    level4 = item['cpc_level4']
    cpc_counts[level4] = cpc_counts.get(level4, 0) + 1

print('__RESULT__:')
print(json.dumps({
    'total_german_patents_2019': len(data),
    'german_patents_second_half_2019': len(german_second_half),
    'total_cpc_assignments': len(cpc_data),
    'unique_cpc_level4_groups': len(cpc_counts),
    'top_cpc_groups': sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:15]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'files_in_tmp': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'json_files': ['/workspace/file_storage/functions.query_db:8.json', '/workspace/file_storage/functions.query_db:9.json', '/workspace/file_storage/functions.query_db:18.json', '/workspace/file_storage/functions.query_db:2.json', '/workspace/file_storage/functions.query_db:20.json']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_german_patents_2019': 50, 'second_half_german_patents': 24, 'total_cpc_assignments': 252, 'cpc_groups': ['B41F/102', 'B41F/00', 'F02D/300', 'F02D/20', 'F02M/005', 'F02D/00', 'F02M/102', 'F02M/04', 'F02M/44', 'F02M/06', 'F04B/001', 'F02M/368', 'G01D/24', 'B23K/001', 'B63B/50', 'H04W/21', 'H04W/56', 'H04L/003', 'H04L/161', 'H04W/026']}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_german_patents': 68, 'sample_record': {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the german patents data
file_path = '/workspace/file_storage/functions.query_db:32.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Filter for second half of 2019 systematically
second_half_data = []

for record in data:
    grant_date = str(record.get('grant_date', ''))
    patents_info = str(record.get('Patents_info', ''))
    
    # Only 2019 grants
    if '2019' not in grant_date:
        continue
        
    # Check for second half months
    is_second_half = any(month in grant_date for month in [
        'July', 'August', 'September', 'October', 'November', 'December',
        'July', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
        'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
    ])
    
    # Must be DE patent
    is_german = 'DE-' in patents_info or 'from DE' in patents_info
    
    if is_second_half and is_german:
        second_half_data.append(record)

# Extract CPC level 4 codes more carefully
cpc_patents = []

for record in second_half_data:
    patents_info = record.get('Patents_info', '')
    grant_date = record.get('grant_date', '')
    cpc_json = record.get('cpc', '[]')
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        cpc_list = []
    
    for cpc_item in cpc_list:
        full_code = cpc_item.get('code', '')
        if full_code and '/' in full_code:
            parts = full_code.split('/')
            if len(full_code) >= 7 and len(parts[0]) >= 4:
                # For level 4, we want: Section (1 char) + Class (2 digits) + Subclass (1 letter) + Main group
                # Format like: G06F9/455 where G=section, 06=class, F=subclass, 9=main group first digit, 455=subgroup
                # Level 4 means we go down to the main group level (first digit after the slash)
                section = full_code[0]
                class_code = full_code[1:3] if len(full_code) > 2 else ''
                subclass = full_code[3] if len(full_code) > 3 else ''
                main_group = parts[1][0] if len(parts[1]) > 0 else ''
                
                if section and class_code and subclass:
                    # Construct level 4 code: XNNX/N where X=section letter, NN=class, X=subclass, N=first digit of group
                    level4_code = f"{section}{class_code}{subclass}/{main_group}00" if main_group else f"{section}{class_code}{subclass}/000"
                    
                    cpc_patents.append({
                        'patent_info': patents_info,
                        'grant_date': grant_date,
                        'full_cpc_code': full_code,
                        'cpc_level4': level4_code,
                        'year': 2019
                    })

print('__RESULT__:')
print(json.dumps({
    'german_patents_second_half_2019': len(second_half_data),
    'total_cpc_assignments': len(cpc_patents),
    'sample_cpc_codes': cpc_patents[:5] if cpc_patents else []
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'files_in_tmp': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'json_files': ['/workspace/file_storage/functions.query_db:8.json', '/workspace/file_storage/functions.query_db:9.json', '/workspace/file_storage/functions.query_db:18.json', '/workspace/file_storage/functions.query_db:2.json', '/workspace/file_storage/functions.query_db:20.json']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_german_patents_2019': 50, 'second_half_german_patents': 24, 'total_cpc_assignments': 252, 'cpc_groups': ['B41F/102', 'B41F/00', 'F02D/300', 'F02D/20', 'F02M/005', 'F02D/00', 'F02M/102', 'F02M/04', 'F02M/44', 'F02M/06', 'F04B/001', 'F02M/368', 'G01D/24', 'B23K/001', 'B63B/50', 'H04W/21', 'H04W/56', 'H04L/003', 'H04L/161', 'H04W/026']}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_german_patents': 68, 'sample_record': {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:36': {'total_german_patents_2019': 68, 'german_patents_second_half_2019': 33, 'total_cpc_assignments': 311, 'unique_cpc_level4_groups': 188, 'top_cpc_groups': [['H04L/186', 4], ['C04B/656', 4], ['C04B/322', 4], ['C04B/645', 4], ['F02D/20', 3], ['H04W/21', 3], ['H04W/56', 3], ['H04W/026', 3], ['H04W/021', 3], ['H04W/022', 3], ['H04W/044', 3], ['H04W/025', 3], ['F24B/023', 3], ['F23L/04', 3], ['F23L/00', 3]]}}

exec(code, env_args)

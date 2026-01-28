code = """import json
import pandas as pd
from datetime import datetime
import re

# Read all German patents data
file_path = '/workspace/file_storage/functions.query_db:40.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Function to extract year from natural language date
def extract_year(date_str):
    if not date_str:
        return None
    
    # Look for 4-digit year patterns like 2010, 2011, 2015, 2016, 2017, 2018, 2019, 2020 etc.
    matches = re.findall(r'(20(?:1[0-9]|2[0-1]))', str(date_str))
    if matches:
        try:
            return int(matches[0])
        except:
            return None
    return None

# Function to extract CPC level 4 code
def extract_cpc_level4(full_code):
    if not full_code or '/' not in full_code:
        return None
    
    # CPC format: SectionClassSubclass/Group (e.g., G06F9/45533)
    # Level 4 (Group level): G06F9/00
    parts = full_code.split('/')
    if len(parts) == 2:
        section_class_subclass = parts[0]
        # Level 4 is the group level, so we use /00 for the main group
        if len(section_class_subclass) >= 4:
            # Some codes might have more characters before the slash
            # Take first 4-5 characters as the main classification
            main_part = section_class_subclass[:5]
            return f"{main_part}/00"
    return None

# Process all German patents
all_cpc_records = []

for record in data:
    patents_info = record.get('Patents_info', '')
    grant_date = record.get('grant_date', '')
    cpc_json = record.get('cpc', '[]')
    
    # Extract year
    year = extract_year(grant_date)
    if not year or year < 2015 or year > 2021:  # Focus on recent years
        continue
    
    # Confirm it's German
    if not ('DE-' in patents_info or 'from DE' in patents_info):
        continue
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_json)
    except:
        cpc_list = []
    
    for cpc_item in cpc_list:
        full_code = cpc_item.get('code', '')
        level4_code = extract_cpc_level4(full_code)
        
        if level4_code:
            all_cpc_records.append({
                'patent_info': patents_info,
                'year': year,
                'cpc_level4': level4_code,
                'full_cpc_code': full_code
            })

# Create DataFrame
df = pd.DataFrame(all_cpc_records)

print('__RESULT__:')
print(json.dumps({
    'total_records': len(all_cpc_records),
    'years_range': df['year'].min() if not df.empty else None,
    'years_max': df['year'].max() if not df.empty else None,
    'unique_cpc_groups': len(df['cpc_level4'].unique()) if not df.empty else 0,
    'sample_records': all_cpc_records[:3]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'files_in_tmp': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'json_files': ['/workspace/file_storage/functions.query_db:8.json', '/workspace/file_storage/functions.query_db:9.json', '/workspace/file_storage/functions.query_db:18.json', '/workspace/file_storage/functions.query_db:2.json', '/workspace/file_storage/functions.query_db:20.json']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_german_patents_2019': 50, 'second_half_german_patents': 24, 'total_cpc_assignments': 252, 'cpc_groups': ['B41F/102', 'B41F/00', 'F02D/300', 'F02D/20', 'F02M/005', 'F02D/00', 'F02M/102', 'F02M/04', 'F02M/44', 'F02M/06', 'F04B/001', 'F02M/368', 'G01D/24', 'B23K/001', 'B63B/50', 'H04W/21', 'H04W/56', 'H04L/003', 'H04L/161', 'H04W/026']}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_german_patents': 68, 'sample_record': {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:36': {'total_german_patents_2019': 68, 'german_patents_second_half_2019': 33, 'total_cpc_assignments': 311, 'unique_cpc_level4_groups': 188, 'top_cpc_groups': [['H04L/186', 4], ['C04B/656', 4], ['C04B/322', 4], ['C04B/645', 4], ['F02D/20', 3], ['H04W/21', 3], ['H04W/56', 3], ['H04W/026', 3], ['H04W/021', 3], ['H04W/022', 3], ['H04W/044', 3], ['H04W/025', 3], ['F24B/023', 3], ['F23L/04', 3], ['F23L/00', 3]]}, 'var_functions.execute_python:38': {'german_patents_second_half_2019': 33, 'total_cpc_assignments': 311, 'sample_cpc_codes': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F21/102', 'cpc_level4': 'B41F/100', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F22/00', 'cpc_level4': 'B41F/000', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F21/00', 'cpc_level4': 'B41F/000', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'full_cpc_code': 'F02D41/3005', 'cpc_level4': 'F02D/300', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'full_cpc_code': 'F02D41/20', 'cpc_level4': 'F02D/200', 'year': 2019}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_german_patents_all_years': 510, 'sample_record': {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010', 'cpc': '[\n  {\n    "code": "B26B5/003",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/001",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/003",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/001",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}}

exec(code, env_args)

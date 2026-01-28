code = """import json
import pandas as pd
from datetime import datetime
import re

# Read German patents data for multiple years
file_path = '/workspace/file_storage/functions.query_db:40.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract year from natural language date
def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'(20(?:1[0-9]|2[0-1]))', str(date_str))
    return int(match.group(1)) if match else None

# Extract CPC level 4 code (Group level: SectionClassSubclass/Group00)
def extract_cpc_level4(full_code):
    if not full_code or '/' not in full_code:
        return None
    
    parts = full_code.split('/')
    if len(parts[0]) >= 4 and len(parts[1]) >= 1:
        section = parts[0][0]
        class_code = parts[0][1:3] 
        subclass = parts[0][3]
        # Get first digit of group
        group = parts[1][0]
        return f"{section}{class_code}{subclass}/{group}00"
    return None

# Process all German patents
cpc_yearly_data = []

for record in data:
    patents_info = str(record.get('Patents_info', ''))
    grant_date = str(record.get('grant_date', ''))
    cpc_json = str(record.get('cpc', '[]'))
    
    # Check if German
    if not ('DE-' in patents_info or 'from DE' in patents_info):
        continue
    
    # Extract year
    year = extract_year(grant_date)
    if not year or year < 2016 or year > 2019:  # Focus on 2016-2019
        continue
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
    
    for cpc_item in cpc_list:
        if isinstance(cpc_item, dict):
            full_code = cpc_item.get('code', '')
            level4 = extract_cpc_level4(full_code)
            if level4:
                cpc_yearly_data.append({
                    'cpc_level4': level4,
                    'year': year,
                    'patent_id': patents_info  # Track unique patents
                })

# Deduplicate by patent and CPC (one patent may have multiple CPC codes)
df = pd.DataFrame(cpc_yearly_data)

# Count unique patents per CPC group per year
yearly_counts = df.groupby(['cpc_level4', 'year']).agg({
    'patent_id': 'nunique'
}).reset_index()
yearly_counts = yearly_counts.rename(columns={'patent_id': 'patent_count'})

print('__RESULT__:')
print(json.dumps({
    'total_records': len(df),
    'year_range': f"{yearly_counts['year'].min() if not yearly_counts.empty else None}-{yearly_counts['year'].max() if not yearly_counts.empty else None}",
    'unique_cpc_groups': len(yearly_counts['cpc_level4'].unique()) if not yearly_counts.empty else 0,
    'sample_data': yearly_counts.head(10).to_dict('records') if not yearly_counts.empty else []
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'files_in_tmp': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'json_files': ['/workspace/file_storage/functions.query_db:8.json', '/workspace/file_storage/functions.query_db:9.json', '/workspace/file_storage/functions.query_db:18.json', '/workspace/file_storage/functions.query_db:2.json', '/workspace/file_storage/functions.query_db:20.json']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_german_patents_2019': 50, 'second_half_german_patents': 24, 'total_cpc_assignments': 252, 'cpc_groups': ['B41F/102', 'B41F/00', 'F02D/300', 'F02D/20', 'F02M/005', 'F02D/00', 'F02M/102', 'F02M/04', 'F02M/44', 'F02M/06', 'F04B/001', 'F02M/368', 'G01D/24', 'B23K/001', 'B63B/50', 'H04W/21', 'H04W/56', 'H04L/003', 'H04L/161', 'H04W/026']}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_german_patents': 68, 'sample_record': {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:36': {'total_german_patents_2019': 68, 'german_patents_second_half_2019': 33, 'total_cpc_assignments': 311, 'unique_cpc_level4_groups': 188, 'top_cpc_groups': [['H04L/186', 4], ['C04B/656', 4], ['C04B/322', 4], ['C04B/645', 4], ['F02D/20', 3], ['H04W/21', 3], ['H04W/56', 3], ['H04W/026', 3], ['H04W/021', 3], ['H04W/022', 3], ['H04W/044', 3], ['H04W/025', 3], ['F24B/023', 3], ['F23L/04', 3], ['F23L/00', 3]]}, 'var_functions.execute_python:38': {'german_patents_second_half_2019': 33, 'total_cpc_assignments': 311, 'sample_cpc_codes': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F21/102', 'cpc_level4': 'B41F/100', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F22/00', 'cpc_level4': 'B41F/000', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F21/00', 'cpc_level4': 'B41F/000', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'full_cpc_code': 'F02D41/3005', 'cpc_level4': 'F02D/300', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'full_cpc_code': 'F02D41/20', 'cpc_level4': 'F02D/200', 'year': 2019}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_german_patents_all_years': 510, 'sample_record': {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010', 'cpc': '[\n  {\n    "code": "B26B5/003",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/001",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/003",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/001",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:46': {'status': 'success', 'total_cpc_records': 2479, 'german_patents_analyzed': 2479, 'unique_cpc_groups': 243, 'years_range': '2015-2019', 'top_results': [{'cpc_level4': 'D06F/00', 'best_year': 2015, 'ema_value': 47.0, 'patent_count': 47}, {'cpc_level4': 'B60G/00', 'best_year': 2015, 'ema_value': 35.0, 'patent_count': 35}, {'cpc_level4': 'D04H/00', 'best_year': 2016, 'ema_value': 30.0, 'patent_count': 30}, {'cpc_level4': 'H01L/00', 'best_year': 2019, 'ema_value': 24.087000000000003, 'patent_count': 111}, {'cpc_level4': 'A61F/00', 'best_year': 2015, 'ema_value': 23.0, 'patent_count': 23}, {'cpc_level4': 'H03F/00', 'best_year': 2016, 'ema_value': 22.0, 'patent_count': 22}, {'cpc_level4': 'F16D/00', 'best_year': 2015, 'ema_value': 18.0, 'patent_count': 18}, {'cpc_level4': 'G01N/00', 'best_year': 2015, 'ema_value': 17.0, 'patent_count': 17}, {'cpc_level4': 'G02F/00', 'best_year': 2015, 'ema_value': 16.0, 'patent_count': 16}, {'cpc_level4': 'B01D/00', 'best_year': 2017, 'ema_value': 14.7, 'patent_count': 21}], 'ema_analysis_complete': True}, 'var_functions.execute_python:48': {'total_german_patents_2019': 68, 'second_half_2019_patents': 311, 'unique_cpc_groups_2019': 108, 'top_cpc_groups': {'C04B/600': 20, 'H04W/000': 15, 'B29C/500': 13, 'H04L/100': 10, 'F02D/000': 9, 'C04B/500': 8, 'C04B/300': 8, 'G02B/200': 7, 'G02B/100': 7, 'H04L/000': 6, 'F23L/000': 6, 'H01J/000': 6, 'G02B/000': 6, 'F02D/200': 5, 'F02M/000': 5, 'F02N/000': 5, 'F16H/000': 5, 'H04W/200': 4, 'A61F/000': 4, 'G01M/200': 4}}}

exec(code, env_args)

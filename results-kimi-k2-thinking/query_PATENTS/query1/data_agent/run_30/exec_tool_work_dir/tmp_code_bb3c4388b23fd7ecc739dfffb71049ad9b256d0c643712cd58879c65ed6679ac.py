code = """import json
import pandas as pd
from datetime import datetime
import re

# Get the file path from the variable
file_storage_path = locals()['var_functions.query_db:9']

with open(file_storage_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and publication dates with robust date parsing
records = []

for item in data:
    try:
        cpc_json_str = item['cpc']
        pub_date_str = item['publication_date']
        
        # Clean publication date by removing control characters
        clean_date_str = pub_date_str.replace('\x01', '').strip()
        
        # Extract year using regex - look for 4-digit year
        year_match = re.search(r'(\d{4})', clean_date_str)
        if not year_match:
            continue
            
        year = int(year_match.group(1))
        
        # Parse CPC JSON string
        cpc_list = json.loads(cpc_json_str)
        
        # Extract CPC codes
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code:
                records.append({
                    'cpc_code': code,
                    'year': year
                })
        
    except Exception as e:
        continue

# Create DataFrame
df = pd.DataFrame(records)

print('__RESULT__:')
if not df.empty:
    print(json.dumps({
        'total_records_processed': len(records),
        'unique_cpc_codes': len(df['cpc_code'].unique()),
        'year_range': f"{int(df['year'].min())}-{int(df['year'].max())}",
        'sample_cpc_codes': df['cpc_code'].unique()[:10].tolist(),
        'sample_years': sorted(df['year'].unique())[:10]
    }))
else:
    print(json.dumps({'error': 'No valid records extracted'}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'file_path_variable': 'var_functions.query_db:9', 'file_path_value': 'file_storage/functions.query_db:9.json', 'type': "<class 'str'>", 'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9']}, 'var_functions.execute_python:16': {'first_item_keys': ['cpc', 'publication_date'], 'first_item_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'first_item_pub_date': 'Aug 3rd, 2021', 'total_records': 277813}, 'var_functions.execute_python:20': {'total_processed': 277813, 'success_count': 0, 'error_count': 10000, 'records_extracted': 0, 'first_few_records': []}, 'var_functions.execute_python:22': {'cpc_field_type': "<class 'str'>", 'cpc_field_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n  ', 'is_list': False, 'is_string': True}, 'var_functions.execute_python:24': {'success': True, 'cpc_list_length': 38, 'first_cpc_entry': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}}, 'var_functions.execute_python:28': {'total_records_processed': 0, 'dataframe_columns': [], 'debug_sample': [{'record_index': 0, 'error': "time data 'Aug \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 1, 'error': "time data 'Oct \\x01, 2020' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 2, 'error': "time data 'Sep \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 3, 'error': "time data '2020, April \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 4, 'error': "time data 'Mar \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 5, 'error': "time data 'March \\x01, 2021' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 6, 'error': "time data '2021, November \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 7, 'error': "time data '\\x01 June 2020' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 8, 'error': "time data '2021 on Mar \\x01' does not match format '%b %d, %Y'", 'success': False}, {'record_index': 9, 'error': "time data '\\x01 Nov 2021' does not match format '%b %d, %Y'", 'success': False}], 'sample_records': []}, 'var_functions.query_db:32': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)

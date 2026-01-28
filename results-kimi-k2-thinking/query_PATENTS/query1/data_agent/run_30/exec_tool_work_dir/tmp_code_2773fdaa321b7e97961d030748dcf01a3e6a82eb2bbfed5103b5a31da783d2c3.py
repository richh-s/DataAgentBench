code = """import json
import pandas as pd
from datetime import datetime
import re

# Get the file path from the variable
file_storage_path = locals()['var_functions.query_db:9']

with open(file_storage_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and publication dates with detailed debugging
records = []
debug_info = []

for i, item in enumerate(data[:1000]):  # Process first 1000 records for debugging
    try:
        cpc_json_str = item['cpc']
        pub_date_str = item['publication_date']
        
        # Parse publication date to extract year
        date_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date_str)
        date_obj = datetime.strptime(date_clean, '%b %d, %Y')
        year = date_obj.year
        
        # Parse CPC JSON string
        cpc_list = json.loads(cpc_json_str)
        
        # Extract CPC codes
        codes_found = 0
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code:
                records.append({
                    'cpc_code': code,
                    'year': year
                })
                codes_found += 1
        
        debug_info.append({
            'record_index': i,
            'year': year,
            'codes_found': codes_found,
            'success': True
        })
        
    except Exception as e:
        debug_info.append({
            'record_index': i,
            'error': str(e),
            'success': False
        })
        continue

# Create DataFrame
df = pd.DataFrame(records)

print('__RESULT__:')
print(json.dumps({
    'total_records_processed': len(records),
    'dataframe_columns': list(df.columns) if not df.empty else [],
    'debug_sample': debug_info[:10],
    'sample_records': records[:5]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'file_path_variable': 'var_functions.query_db:9', 'file_path_value': 'file_storage/functions.query_db:9.json', 'type': "<class 'str'>", 'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9']}, 'var_functions.execute_python:16': {'first_item_keys': ['cpc', 'publication_date'], 'first_item_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'first_item_pub_date': 'Aug 3rd, 2021', 'total_records': 277813}, 'var_functions.execute_python:20': {'total_processed': 277813, 'success_count': 0, 'error_count': 10000, 'records_extracted': 0, 'first_few_records': []}, 'var_functions.execute_python:22': {'cpc_field_type': "<class 'str'>", 'cpc_field_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n  ', 'is_list': False, 'is_string': True}, 'var_functions.execute_python:24': {'success': True, 'cpc_list_length': 38, 'first_cpc_entry': {'code': 'C01B33/00', 'first': False, 'inventive': True, 'tree': []}}}

exec(code, env_args)

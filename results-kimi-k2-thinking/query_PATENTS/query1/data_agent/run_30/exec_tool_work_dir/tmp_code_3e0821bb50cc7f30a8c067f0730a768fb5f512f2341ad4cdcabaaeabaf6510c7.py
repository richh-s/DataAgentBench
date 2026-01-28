code = """import json
import pandas as pd
from datetime import datetime
import re
import numpy as np

# Get the file path from the variable
file_storage_path = locals()['var_functions.query_db:9']

with open(file_storage_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and publication dates with error handling
records = []
error_count = 0
success_count = 0

for i, item in enumerate(data[:10000]):  # Process first 10k records for debugging
    try:
        cpc_json = item['cpc']
        pub_date_str = item['publication_date']
        
        # Parse publication date to extract year
        date_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date_str)
        date_obj = datetime.strptime(date_clean, '%b %d, %Y')
        year = date_obj.year
        
        # Parse CPC JSON string
        cpc_list = json.loads(cpc_json)
        
        # Extract CPC codes
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code:
                records.append({
                    'cpc_code': code,
                    'year': year
                })
        success_count += 1
    except Exception as e:
        error_count += 1
        continue

print('__RESULT__:')
print(json.dumps({
    'total_processed': len(data),
    'success_count': success_count,
    'error_count': error_count,
    'records_extracted': len(records),
    'first_few_records': records[:5]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'file_path_variable': 'var_functions.query_db:9', 'file_path_value': 'file_storage/functions.query_db:9.json', 'type': "<class 'str'>", 'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9']}, 'var_functions.execute_python:16': {'first_item_keys': ['cpc', 'publication_date'], 'first_item_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'first_item_pub_date': 'Aug 3rd, 2021', 'total_records': 277813}}

exec(code, env_args)

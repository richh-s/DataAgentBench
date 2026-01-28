code = """import json
import pandas as pd
import numpy as np
import re

# Load the yearly counts data
yearly_counts_file = 'yearly_counts.json'
yearly_counts = pd.read_json(yearly_counts_file)

# Focus on more recent years to reduce data size
recent_data = yearly_counts[yearly_counts['year'] >= 2015].copy()
print(f"Data from 2015-2024: {len(recent_data)} records, {len(recent_data['cpc_code'].unique())} CPC codes")

# Check which CPC codes have data for 2022
codes_with_2022 = recent_data[recent_data['year'] == 2022]['cpc_code'].unique()
print(f"CPC codes with 2022 data: {len(codes_with_2022)}")

# Filter for level 5 CPC codes (format like A01B13/02, G06Q50/30, H01M10/05)
# These typically have: letters + 2 digits + letter + digits + / + 2 digits
level5_pattern = r'^[A-Z][0-9]{2}[A-Z][0-9]+/[0-9]{2}$'

# Test some codes to understand pattern
sample_codes = codes_with_2022[:50]
level5_codes = []
for code in sample_codes:
    if re.match(level5_pattern, code) and len(code) >= 8:
        level5_codes.append(code)

result = {
    "sample_codes": sample_codes[:10].tolist(),
    "sample_level5": level5_codes[:10],
    "total_with_2022": len(codes_with_2022)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}, 'var_functions.execute_python:18': {'type_first_cpc': "<class 'str'>", 'first_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'is_first_list': False, 'type_second_cpc': "<class 'str'>", 'second_cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H4', 'is_second_list': False}, 'var_functions.execute_python:20': {'total_raw_records': 277813, 'parsed_records': 2677930, 'unique_cpc_codes': 175403, 'year_range': '1900 to 2024', 'sample_cpc': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'data_check': True}, 'var_functions.execute_python:22': {'total_cpc_year_combinations': 917982, 'year_range': '1900 to 2024', 'total_records': 2677930, 'saved_file': 'yearly_counts.json'}, 'var_functions.list_db:26': ['cpc_definition'], 'var_functions.query_db:28': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:32': {'total_cpc_codes': 175403, 'sample_codes': ['A01B1/00', 'A01B1/02', 'A01B1/022', 'A01B1/026', 'A01B1/028', 'A01B1/04', 'A01B1/06', 'A01B1/065', 'A01B1/08', 'A01B1/14']}}

exec(code, env_args)

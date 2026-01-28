code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the data file from storage
data_file = locals()['var_functions.query_db:5']
with open(data_file, 'r') as f:
    raw_data = json.load(f)

# Function to extract year from natural language date
def extract_year(date_str):
    if date_str and isinstance(date_str, str):
        # Extract 4-digit year from string
        match = re.search(r'(19|20)\d{2}', date_str)
        if match:
            return int(match.group())
    return None

# Parse CPC codes and extract years
records = []
for row in raw_data:
    cpc_str = row.get('cpc', '')
    if cpc_str and isinstance(cpc_str, str):
        if cpc_str.startswith('['):
            # It's a JSON string that needs parsing
            try:
                cpc_list = json.loads(cpc_str)
                if isinstance(cpc_list, list):
                    year = extract_year(row.get('publication_date', ''))
                    
                    if year:
                        for cpc_entry in cpc_list:
                            if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                                code = cpc_entry.get('code', '')
                                if code:
                                    # Extract level 5 CPC codes (format like X00X00/00)
                                    # Level 5 typically has 4-5 characters before the slash
                                    if '/' in code:
                                        records.append({
                                            'cpc_code': code,
                                            'year': year,
                                            'inventive': cpc_entry.get('inventive', False)
                                        })
            except:
                continue

# Create DataFrame
df = pd.DataFrame(records)

# Get summary stats
if not df.empty:
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    unique_cpc = int(df['cpc_code'].nunique())
    sample_cpc = df['cpc_code'].unique()[:10].tolist()
    total_records = int(len(df))
else:
    min_year = max_year = unique_cpc = total_records = 0
    sample_cpc = []

result = {
    "total_raw_records": len(raw_data),
    "parsed_records": total_records,
    "unique_cpc_codes": unique_cpc,
    "year_range": f"{min_year} to {max_year}",
    "sample_cpc": sample_cpc,
    "data_check": not df.empty
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}, 'var_functions.execute_python:18': {'type_first_cpc': "<class 'str'>", 'first_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'is_first_list': False, 'type_second_cpc': "<class 'str'>", 'second_cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H4', 'is_second_list': False}}

exec(code, env_args)

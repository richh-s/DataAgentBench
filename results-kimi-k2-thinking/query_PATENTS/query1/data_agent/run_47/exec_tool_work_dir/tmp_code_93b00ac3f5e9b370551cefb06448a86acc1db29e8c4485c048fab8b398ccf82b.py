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
        match = re.search(r'(19|20)\d{2}', date_str)
        if match:
            return int(match.group())
    return None

# Parse CPC codes and extract years
records = []
for row in raw_data:
    cpc_str = row.get('cpc', '')
    if cpc_str and isinstance(cpc_str, str) and cpc_str.startswith('['):
        try:
            cpc_list = json.loads(cpc_str)
            if isinstance(cpc_list, list):
                year = extract_year(row.get('publication_date', ''))
                if year and 1900 <= year <= 2024:
                    for cpc_entry in cpc_list:
                        if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                            code = cpc_entry.get('code', '')
                            if code and '/' in code:
                                records.append({
                                    'cpc_code': code,
                                    'year': year
                                })
        except:
            continue

# Create DataFrame and count yearly filings
df = pd.DataFrame(records)
yearly_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='filings')

# Save for next steps
yearly_counts_file = 'yearly_counts.json'
yearly_counts.to_json(yearly_counts_file, orient='records', lines=False)

result = {
    "total_cpc_year_combinations": len(yearly_counts),
    "year_range": f"{yearly_counts['year'].min()} to {yearly_counts['year'].max()}",
    "total_records": len(df),
    "saved_file": yearly_counts_file
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}, 'var_functions.execute_python:16': {'total_raw_records': 277813, 'parsed_records': 0, 'unique_cpc_codes': 0, 'year_range': '0 to 0', 'sample_cpc': [], 'data_check': False}, 'var_functions.execute_python:18': {'type_first_cpc': "<class 'str'>", 'first_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01', 'is_first_list': False, 'type_second_cpc': "<class 'str'>", 'second_cpc_preview': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H4', 'is_second_list': False}, 'var_functions.execute_python:20': {'total_raw_records': 277813, 'parsed_records': 2677930, 'unique_cpc_codes': 175403, 'year_range': '1900 to 2024', 'sample_cpc': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'data_check': True}}

exec(code, env_args)

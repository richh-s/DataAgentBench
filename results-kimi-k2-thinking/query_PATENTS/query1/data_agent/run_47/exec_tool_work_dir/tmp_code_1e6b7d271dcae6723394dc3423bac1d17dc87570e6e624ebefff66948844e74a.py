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
        # Extract 4-digit year from end of string
        match = re.search(r'\b(19|20)\d{2}\b', date_str)
        if match:
            return int(match.group())
    return None

# Parse CPC codes and extract years
records = []
for i, row in enumerate(raw_data):
    cpc_str = row.get('cpc', '')
    try:
        cpc_list = json.loads(cpc_str)
        # Ensure it's a list
        if isinstance(cpc_list, list):
            year = extract_year(row.get('publication_date', ''))
            
            if year:
                for cpc_entry in cpc_list:
                    if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                        code = cpc_entry.get('code', '')
                        if code:
                            records.append({
                                'cpc_code': code,
                                'year': year,
                                'inventive': cpc_entry.get('inventive', False)
                            })
    except:
        # Skip rows with parsing errors
        continue

# Create DataFrame
df = pd.DataFrame(records)

# Get summary stats
if not df.empty:
    min_year = df['year'].min()
    max_year = df['year'].max()
    unique_cpc = df['cpc_code'].nunique()
    sample_cpc = df['cpc_code'].unique()[:10].tolist()
else:
    min_year = max_year = unique_cpc = 0
    sample_cpc = []

result = {
    "total_raw_records": len(raw_data),
    "parsed_records": len(records),
    "unique_cpc_codes": unique_cpc,
    "year_range": f"{min_year} to {max_year}",
    "sample_cpc": sample_cpc,
    "data_check": not df.empty
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_date': 'Aug 3rd, 2021'}}

exec(code, env_args)

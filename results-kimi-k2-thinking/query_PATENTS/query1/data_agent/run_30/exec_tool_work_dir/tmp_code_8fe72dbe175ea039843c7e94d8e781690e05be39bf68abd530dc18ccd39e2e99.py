code = """import json
import pandas as pd
from datetime import datetime
import re

# Get the file path from the variable
file_storage_path = locals()['var_functions.query_db:9']

with open(file_storage_path, 'r') as f:
    data = json.load(f)

# Extract CPC codes and publication dates
records = []
for item in data:
    cpc_json = item['cpc']
    pub_date_str = item['publication_date']
    
    # Parse publication date to extract year
    # Format: "Aug 3rd, 2021" or "Oct 6th, 2020"
    try:
        # Remove ordinal suffixes (st, nd, rd, th)
        date_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date_str)
        date_obj = datetime.strptime(date_clean, '%b %d, %Y')
        year = date_obj.year
    except:
        # Skip if date parsing fails
        continue
    
    # Parse CPC JSON string
    try:
        cpc_list = json.loads(cpc_json)
    except:
        # Skip if CPC parsing fails
        continue
    
    # Extract CPC codes
    for cpc_entry in cpc_list:
        code = cpc_entry.get('code', '')
        if code:
            records.append({
                'cpc_code': code,
                'year': year,
                'publication_date': date_obj
            })

# Create DataFrame
df = pd.DataFrame(records)

# Get year range and sample data
if len(df) > 0:
    year_min = int(df['year'].min())
    year_max = int(df['year'].max())
    sample_codes = df['cpc_code'].unique()[:10].tolist()
else:
    year_min = 0
    year_max = 0
    sample_codes = []

print('__RESULT__:')
print(json.dumps({
    'total_records': len(records),
    'unique_cpc_codes': len(df['cpc_code'].unique()),
    'year_range': f"{year_min}-{year_max}",
    'sample_cpc_codes': sample_codes
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'file_path_variable': 'var_functions.query_db:9', 'file_path_value': 'file_storage/functions.query_db:9.json', 'type': "<class 'str'>", 'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9']}}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime
import re
import numpy as np

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
                'year': year
            })

# Create DataFrame
df = pd.DataFrame(records)

# Count patent filings by CPC code and year
cpc_year_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')

print('__RESULT__:')
print(json.dumps({
    'total_patent_classifications': len(records),
    'unique_cpc_codes': len(df['cpc_code'].unique()),
    'year_range': f"{df['year'].min()}-{df['year'].max()}",
    'sample_data': cpc_year_counts.head(10).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'file_path_variable': 'var_functions.query_db:9', 'file_path_value': 'file_storage/functions.query_db:9.json', 'type': "<class 'str'>", 'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:9']}, 'var_functions.execute_python:16': {'first_item_keys': ['cpc', 'publication_date'], 'first_item_cpc_preview': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"', 'first_item_pub_date': 'Aug 3rd, 2021', 'total_records': 277813}}

exec(code, env_args)

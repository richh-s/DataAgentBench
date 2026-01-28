code = """import json
import pandas as pd
from datetime import datetime
import re
import os

# Read the data from the file
# var_functions.query_db:9 is a string containing the file path
file_path = "/tmp/tmp_0x2g3o0.json"

with open(file_path, 'r') as f:
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
print('__RESULT__:')
print(json.dumps({
    'total_records': len(records),
    'unique_cpc_codes': len(df['cpc_code'].unique()),
    'year_range': f"{df['year'].min()}-{df['year'].max()}" if len(df) > 0 else 'N/A',
    'sample_cpc_codes': df['cpc_code'].unique()[:10].tolist()
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)

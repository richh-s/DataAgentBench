code = """import json
import pandas as pd
from datetime import datetime
import re
import os

# The variable contains the file path
file_path = var_functions.query_db:5

# Read the publication data
with open(file_path, 'r') as f:
    pub_data = json.load(f)

# Parse CPC codes and extract years
records = []
for item in pub_data:
    cpc_json = item['cpc']
    pub_date = item['publication_date']
    
    # Parse publication year from natural language date
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON - try different approaches
    try:
        # Remove newlines and load
        clean_json = cpc_json.replace('\n', '').replace('\r', '')
        cpc_list = json.loads(clean_json)
        for cpc in cpc_list:
            if 'code' in cpc:
                code = cpc['code']
                records.append({
                    'cpc_code': code,
                    'year': year
                })
    except:
        # Fallback: extract codes with regex
        try:
            codes = re.findall(r'"code":\s*"([^"]+)"', cpc_json)
            for code in codes:
                records.append({
                    'cpc_code': code,
                    'year': year
                })
        except:
            continue

# Create DataFrame if we have data
if records:
    df = pd.DataFrame(records)
    
    # Count filings per CPC per year
    yearly_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')
    
    result = {
        'total_records': len(records),
        'unique_cpcs': int(df['cpc_code'].nunique()),
        'year_range': {
            'min': int(df['year'].min()),
            'max': int(df['year'].max())
        },
        'sample_data': yearly_counts.head(10).to_dict('records')
    }
else:
    result = {'error': 'No records parsed'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime
import re

# First, let's load the publication data
with open(var_functions.query_db:5, 'r') as f:
    pub_data = json.load(f)

# Parse CPC codes and extract years
records = []
for item in pub_data:
    cpc_json = item['cpc']
    pub_date = item['publication_date']
    
    # Parse publication year from natural language date
    year_match = re.search(r'\d{4}', pub_date)
    if year_match:
        year = int(year_match.group())
    else:
        continue
    
    # Parse CPC JSON
    try:
        cpc_list = json.loads(cpc_json.replace('\n', ''))
        for cpc in cpc_list:
            code = cpc['code']
            records.append({
                'cpc_code': code,
                'year': year
            })
    except:
        # Fallback for malformed JSON
        try:
            # Simple extraction using regex
            codes = re.findall(r'"code":\s*"([^"]+)"', cpc_json)
            for code in codes:
                records.append({
                    'cpc_code': code,
                    'year': year
                })
        except:
            continue

# Create DataFrame
df = pd.DataFrame(records)

# Count filings per CPC per year
yearly_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')

print('__RESULT__:')
print(json.dumps({
    'total_records': len(records),
    'unique_cpcs': df['cpc_code'].nunique(),
    'year_range': {
        'min': df['year'].min(),
        'max': df['year'].max()
    },
    'sample_data': yearly_counts.head(10).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

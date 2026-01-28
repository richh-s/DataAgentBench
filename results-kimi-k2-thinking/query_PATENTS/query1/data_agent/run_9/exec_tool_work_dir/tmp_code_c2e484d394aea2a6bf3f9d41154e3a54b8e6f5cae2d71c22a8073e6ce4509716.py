code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the publication data
with open('var_functions.query_db:6', 'r') as f:
    pub_data = json.load(f)

# Extract CPC codes and publication years
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
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_entry in cpc_list:
            code = cpc_entry['code']
            # Extract level 5 group (first 5 characters, e.g., C01B33)
            if len(code) >= 5:
                group_5 = code[:5]
                records.append({
                    'year': year,
                    'cpc_code': code,
                    'cpc_group_5': group_5
                })
    except:
        continue

# Create DataFrame
df = pd.DataFrame(records)
print(f"Total records: {len(df)}")
print(f"Year range: {df['year'].min()} - {df['year'].max()}")
print(f"Unique level 5 groups: {df['cpc_group_5'].nunique()}")

# Count filings per year for each level 5 group
yearly_counts = df.groupby(['year', 'cpc_group_5']).size().reset_index(name='count')
print(f"Yearly counts shape: {yearly_counts.shape}")

# List available years
available_years = sorted(yearly_counts['year'].unique())
print(f"Available years: {available_years}")

# Save for next steps
result = {
    'yearly_counts': yearly_counts.to_dict('records'),
    'available_years': available_years
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

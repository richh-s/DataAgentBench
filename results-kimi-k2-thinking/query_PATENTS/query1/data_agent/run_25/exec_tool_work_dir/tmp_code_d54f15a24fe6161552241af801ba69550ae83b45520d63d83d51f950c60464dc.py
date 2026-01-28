code = """import json
import pandas as pd
import re
from collections import defaultdict
import os

# Load data from the JSON file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    data = json.load(f)

# Process CPC codes and dates
patent_counts = defaultdict(lambda: defaultdict(int))  # cpc_code -> year -> count

for record in data:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '')
    
    if pub_date and cpc_data:
        # Extract year from publication date
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
            
            # Parse CPC codes (JSON-like string)
            try:
                cpc_list = json.loads(cpc_data)
                for cpc_entry in cpc_list:
                    if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                        code = cpc_entry['code']
                        # Count level 5 CPC codes (those with /)
                        if '/' in code:
                            # Use the full CPC code including subgroup
                            patent_counts[code][year] += 1
            except:
                # If parsing fails, skip
                pass

# Convert to DataFrame
records = []
for code, years in patent_counts.items():
    for year, count in years.items():
        records.append({'cpc_code': code, 'year': year, 'count': count})

df = pd.DataFrame(records)

# Check if we have data for year 2022
print('__RESULT__:')
print(json.dumps({
    'unique_codes': len(df['cpc_code'].unique()),
    'year_range': f"{df['year'].min()} to {df['year'].max()}",
    'sample_codes': df['cpc_code'].unique()[:10].tolist()
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

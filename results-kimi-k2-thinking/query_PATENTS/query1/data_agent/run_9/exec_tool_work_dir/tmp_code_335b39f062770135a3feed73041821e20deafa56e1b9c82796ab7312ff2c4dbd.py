code = """# Parse publication data to extract CPC codes and years
import json
import pandas as pd
import re
from datetime import datetime
import os

# Load the publication data from the file path
pub_file = "/tmp/tmp8u9p1h0t.json"  # This is the file path from the query
print("Loading from file:", pub_file)

with open(pub_file, 'r') as f:
    pub_data = json.load(f)

print("Total publication records:", len(pub_data))

# Extract CPC codes and publication years
records = []
for item in pub_data:
    try:
        cpc_json = item['cpc']
        pub_date = item['publication_date']
        
        # Extract year from date string (e.g., "Aug 3rd, 2021")
        year_match = re.search(r'(\d{4})', pub_date)
        if not year_match:
            continue
        year = int(year_match.group(1))
        
        # Parse CPC JSON
        cpc_list = json.loads(cpc_json)
        
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if len(code) >= 5:
                # Get level 5 group (first 5 characters)
                group_5 = code[:5]
                records.append({
                    'year': year,
                    'cpc_code': code,
                    'cpc_group_5': group_5
                })
    except Exception as e:
        continue

print("Parsed records:", len(records))

# Create DataFrame
df = pd.DataFrame(records)
print("Year range:", df['year'].min(), "to", df['year'].max())
print("Unique level 5 groups:", df['cpc_group_5'].nunique())

# Count filings per year for each group
yearly_counts = df.groupby(['year', 'cpc_group_5']).size().reset_index(name='count')
print("Yearly counts shape:", yearly_counts.shape)
print("Available years:", sorted(yearly_counts['year'].unique()))

# Save for next steps
result = {
    'total_records': len(records),
    'year_range': [int(df['year'].min()), int(df['year'].max())],
    'unique_groups': int(df['cpc_group_5'].nunique()),
    'yearly_counts_shape': yearly_counts.shape,
    'available_years': sorted([int(y) for y in yearly_counts['year'].unique()])
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}, 'var_functions.execute_python:38': {'pub_records': 0, 'cpc_symbols': 0, 'sample_pub': None, 'sample_cpc': None}}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime

# Read the full results from the stored file
with open(var_functions.query_db_5, 'r') as f:
    publications = json.load(f)

print(f"Total publications: {len(publications)}")
print(f"First publication sample: {publications[0]}")

# Parse CPC codes and extract years
cpc_yearly_counts = {}
invalid_dates = 0

for pub in publications:
    # Parse publication date
    try:
        date_str = pub['publication_date']
        # Extract year from date string like "Aug 3rd, 2021"
        year = int(date_str.split(', ')[1])
    except:
        invalid_dates += 1
        continue
    
    # Parse CPC codes (stored as JSON string)
    try:
        cpc_data = json.loads(pub['cpc'])
        for cpc_entry in cpc_data:
            cpc_code = cpc_entry['code']
            # Count by year and CPC code
            if year not in cpc_yearly_counts:
                cpc_yearly_counts[year] = {}
            cpc_yearly_counts[year][cpc_code] = cpc_yearly_counts[year].get(cpc_code, 0) + 1
    except:
        # Skip if CPC parsing fails
        continue

print(f"Invalid dates: {invalid_dates}")
print(f"Years with data: {sorted(cpc_yearly_counts.keys())}")
print(f"Sample 2021 data: {list(cpc_yearly_counts[2021].items())[:5] if 2021 in cpc_yearly_counts else 'No 2021 data'}")

# Save the processed data
result = {
    'total_publications': len(publications),
    'invalid_dates': invalid_dates,
    'cpc_yearly_counts': cpc_yearly_counts,
    'years': sorted(cpc_yearly_counts.keys())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}]}

exec(code, env_args)

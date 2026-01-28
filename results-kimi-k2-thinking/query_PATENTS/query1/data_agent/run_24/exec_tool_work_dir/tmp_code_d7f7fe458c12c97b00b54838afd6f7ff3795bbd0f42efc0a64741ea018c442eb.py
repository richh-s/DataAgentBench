code = """import json
import pandas as pd
import numpy as np
from datetime import datetime

# Read the publications data from the stored file
pub_file_path = locals()['var_functions.query_db:14']

with open(pub_file_path, 'r') as f:
    publications = json.load(f)

print(f"Total publications: {len(publications)}")

# Parse CPC codes and extract years
cpc_year_counts = {}
invalid_dates = 0
valid_entries = 0

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
            if year not in cpc_year_counts:
                cpc_year_counts[year] = {}
            cpc_year_counts[year][cpc_code] = cpc_year_counts[year].get(cpc_code, 0) + 1
            valid_entries += 1
    except:
        # Skip if CPC parsing fails
        continue

print(f"Invalid dates: {invalid_dates}")
print(f"Valid entries processed: {valid_entries}")
print(f"Years with data: {sorted(cpc_year_counts.keys())}")

# Get all unique CPC codes and years
all_cpc_codes = set()
all_years = sorted(cpc_year_counts.keys())
for year, counts in cpc_year_counts.items():
    all_cpc_codes.update(counts.keys())

print(f"Number of unique CPC codes: {len(all_cpc_codes)}")
print(f"Year range: {min(all_years) if all_years else 'None'} - {max(all_years) if all_years else 'None'}")

basic_stats = {
    'total_publications': len(publications),
    'invalid_dates': invalid_dates,
    'valid_entries': valid_entries,
    'unique_cpc_codes': len(all_cpc_codes),
    'years': all_years,
    'min_year': min(all_years) if all_years else None,
    'max_year': max(all_years) if all_years else None
}

print('__RESULT__:')
print(json.dumps(basic_stats))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

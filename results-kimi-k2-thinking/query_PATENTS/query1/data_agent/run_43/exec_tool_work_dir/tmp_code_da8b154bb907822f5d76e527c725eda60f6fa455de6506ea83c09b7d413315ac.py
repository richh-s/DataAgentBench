code = """import json
import re
from collections import defaultdict
import pandas as pd

# Get the file path from the storage
file_path = locals()['var_functions.query_db:18']

# Read the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Initialize counters
year_cpc_counts = defaultdict(lambda: defaultdict(int))
cpc_counts = defaultdict(int)

# Pattern to extract the year from publication_date
year_pattern = re.compile(r'(\d{4})')

# Process each record
records_processed = 0
for record in data:
    pub_date = record.get('publication_date', '')
    cpc_field = record.get('cpc', '[]')
    
    # Extract year
    year_match = year_pattern.search(pub_date)
    if year_match:
        year = int(year_match.group(1))
        
        # Parse CPC codes
        try:
            cpc_list = json.loads(cpc_field)
            for cpc_entry in cpc_list:
                full_code = cpc_entry.get('code', '')
                if full_code and '/' in full_code:
                    # This is a subgroup (level 5) code
                    year_cpc_counts[year][full_code] += 1
                    cpc_counts[full_code] += 1
        except:
            # Skip if can't parse
            pass
    
    records_processed += 1
    if records_processed % 100000 == 0:
        print(f"Processed {records_processed} records...")

# Get all years and CPC codes sorted
years = sorted(year_cpc_counts.keys())
cpc_codes = list(cpc_counts.keys())

print(f"Years range: {min(years) if years else 'None'} to {max(years) if years else 'None'}")
print(f"Unique CPC codes: {len(cpc_codes)}")
print(f"Sample CPC codes: {cpc_codes[:5]}")

result_summary = {
    'total_records': len(data),
    'records_processed': records_processed,
    'years': years,
    'num_cpc_codes': len(cpc_codes),
    'sample_data': dict(list(year_cpc_counts.items())[:2])
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'total_records': 5, 'years_range': [2020, 2021], 'unique_cpc_groups': 18, 'sample_data_points': [[2021, {'C01B': 6, 'H01M': 25, 'C01G': 3, 'C01P': 3, 'Y02E': 1, 'B29C': 4, 'C08J': 7, 'B32B': 44, 'C09D': 1, 'B29L': 2, 'C08G': 5, 'B29K': 4, 'H01H': 11}], [2020, {'F16H': 22, 'A61K': 4, 'C12N': 12, 'A01K': 3, 'A61P': 1}]]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'total_records': '277813'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)

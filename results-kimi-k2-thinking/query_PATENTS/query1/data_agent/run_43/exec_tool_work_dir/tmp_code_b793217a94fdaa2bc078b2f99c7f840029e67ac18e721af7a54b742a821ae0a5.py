code = """import json
import pandas as pd
from collections import defaultdict
import re

# Get the file path from the storage
file_path = locals()['var_functions.query_db:2']

# Read the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Initialize counters for patent filings by year and CPC
year_cpc_counts = defaultdict(lambda: defaultdict(int))
cpc_year_counts = defaultdict(lambda: defaultdict(int))

# Pattern to extract the year from publication_date
year_pattern = re.compile(r'(\d{4})')

# Process each record
for record in data:
    pub_date = record.get('publication_date', '')
    cpc_field = record.get('cpc', '[]')
    
    # Extract year
    year_match = year_pattern.search(pub_date)
    if year_match:
        year = int(year_match.group(1))
        
        # Parse CPC codes (it's a string that looks like JSON)
        try:
            cpc_list = json.loads(cpc_field)
            for cpc_entry in cpc_list:
                cpc_code = cpc_entry.get('code', '')
                if cpc_code:
                    # Truncate to group level (first 4 characters + first digit after slash, or just first 4 chars)
                    group_code = cpc_code.split('/')[0][:4]
                    if len(group_code) >= 4:
                        year_cpc_counts[year][group_code] += 1
                        cpc_year_counts[group_code][year] += 1
        except:
            # Skip if can't parse
            pass

# Get all years and CPC groups sorted
years = sorted(year_cpc_counts.keys())
cpc_groups = list(cpc_year_counts.keys())

result = {
    'total_records': len(data),
    'years_range': [min(years) if years else None, max(years) if years else None],
    'unique_cpc_groups': len(cpc_groups),
    'sample_data_points': list(year_cpc_counts.items())[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

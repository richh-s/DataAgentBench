code = """import json
import re
from collections import defaultdict

# Read the CPC publication data
with open('/tmp/tmp_result_6.json', 'r') as f:
    publications = json.load(f)

# Extract CPC codes and years
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for pub in publications:
    cpc_data = pub['cpc']
    year = pub['year']
    
    if cpc_data and year:
        try:
            # Parse the JSON-like string
            cpc_list = json.loads(cpc_data)
            
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code:
                    # Extract group code (level 5) - this is the part before the slash
                    # For example, from "C01B33/00" we want "C01B33"
                    # From "H01M10/0565" we want "H01M10"
                    group_code = code.split('/')[0]
                    
                    # Only count if it's a valid CPC group code (should be 4-7 chars)
                    if len(group_code) >= 4:
                        cpc_year_counts[group_code][year] += 1
        except:
            # Skip if parsing fails
            continue

# Get all unique years and sort them
all_years = set()
for cpc_code in cpc_year_counts:
    all_years.update(cpc_year_counts[cpc_code].keys())

sorted_years = sorted(list(all_years))
print(f"Available years: {sorted_years}")

# Show sample data
sample_cpc = list(cpc_year_counts.keys())[:10]
print("\nSample CPC group codes and their yearly counts:")
for cpc in sample_cpc:
    counts = dict(cpc_year_counts[cpc])
    print(f"{cpc}: {counts}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)

code = """import json
import re
import sys
from collections import defaultdict
from datetime import datetime

# Load the data
result_file = 'var_functions.query_db:2'
with open(result_file, 'r') as f:
    patents_data = json.load(f)

print('Loaded', len(patents_data), 'patent records')

# Filter for German patents granted in second half of 2019
second_half_months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
german_patents = []

for patent in patents_data:
    # Check if it's German (DE in patents_info)
    if 'DE-' in patent['Patents_info'] or ' from DE,' in patent['Patents_info']:
        # Check grant date
        grant_date = patent['grant_date']
        if '2019' in grant_date:
            # Check if it's second half
            if any(month in grant_date for month in second_half_months):
                german_patents.append(patent)

print('Found', len(german_patents), 'German patents from second half 2019')

# Extract CPC codes and filing years
cpc_year_data = defaultdict(lambda: defaultdict(int))
cpc_all_codes = defaultdict(set)

for patent in german_patents:
    # Parse CPC field (it's a JSON string)
    try:
        cpc_entries = json.loads(patent['cpc'])
        
        # Get filing year from filing_date
        filing_date = patent['filing_date']
        year_match = re.search(r'(\d{4})', filing_date)
        if year_match:
            year = int(year_match.group(1))
            
            # Process each CPC entry
            for entry in cpc_entries:
                cpc_code = entry['code']
                # Extract level 4 code (first 4 characters + next component)
                # Format: Section (1 char), Class (2 digits), Subclass (1 letter), Group (1-3 digits), /, Subgrou
                # Level 4 is typically the main group (before the slash)
                parts = cpc_code.split('/')
                if len(parts) >= 2:
                    main_group_part = parts[0]
                    # For level 4, we want the main group (before slash)
                    # This typically includes section, class, subclass, and group
                    if len(main_group_part) >= 4:
                        level4_code = main_group_part
                        cpc_year_data[level4_code][year] += 1
                        cpc_all_codes[level4_code].add(cpc_code)
    except:
        continue

print('Extracted CPC codes for', len(cpc_year_data), 'CPC groups')

# Show sample data
for i, (cpc, years) in enumerate(cpc_year_data.items()):
    if i < 5:
        print(f'CPC {cpc}:', dict(years))
        print(f'  All codes: {list(cpc_all_codes[cpc])[:3]}')

# Save for next steps
result = {
    'cpc_year_data': dict(cpc_year_data),
    'cpc_all_codes': {k: list(v) for k, v in cpc_all_codes.items()},
    'german_patents_count': len(german_patents)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

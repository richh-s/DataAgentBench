code = """import json
import pandas as pd
import re
from collections import defaultdict
from datetime import datetime

# Get file path from storage
file_path = locals()['var_functions.query_db:5']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Parse CPC codes and publication dates
# CPC codes at level 5 have format like: A61K31/00, C07D401/00, etc.
# They have exactly 5 character groups separated by / or numbers

cpc_year_counts = defaultdict(lambda: defaultdict(int))

for record in data:
    # Parse publication date to get year
    pub_date_str = record['publication_date']
    try:
        # Handle formats like "Aug 3rd, 2021", "Oct 6th, 2020"
        year_match = re.search(r'(\d{4})', pub_date_str)
        if year_match:
            year = int(year_match.group(1))
        else:
            continue
    except:
        continue
    
    # Parse CPC codes (it's a JSON string)
    try:
        cpc_list = json.loads(record['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item['code']
            # Check if CPC code is at level 5
            # Level 5 codes typically have format: Section (1), Class (2), Subclass (3), Group (4), Subgroup (5)
            # They look like: A61K31/00, C07D401/00, H01M10/0525
            # Count the structure - typically 4 characters, then numbers, then / then numbers
            if re.match(r'^[A-Z][0-9]{2}[A-Z]?[0-9]+/[0-9]+$', code):
                # For level 5, we want the group level (before the last digits after /)
                # Extract main group and subgroup: e.g., H01M10/0525 -> group level: H01M10/05
                parts = code.split('/')
                if len(parts) == 2:
                    main_group = parts[0]
                    subgroup = parts[1]
                    # Take first 3 digits or up to before the last 2 digits
                    if len(subgroup) >= 2:
                        # Format for level 5: A61K31/00
                        level5_code = f"{main_group}/{subgroup[:2]}"
                        cpc_year_counts[level5_code][year] += 1
    except:
        continue

# Get unique CPC codes and years
cpc_codes = list(cpc_year_counts.keys())
years = sorted(set(year for cpc in cpc_codes for year in cpc_year_counts[cpc].keys()))

print('Total CPC codes at level 5:', len(cpc_codes))
print('Year range:', years[:5], '...', years[-5:])
print('Sample CPC codes:', cpc_codes[:10])
print('Sample year counts for first CPC:')
if cpc_codes:
    sample_cpc = cpc_codes[0]
    print({year: cpc_year_counts[sample_cpc][year] for year in sorted(cpc_year_counts[sample_cpc].keys())[:5]})

result = {
    'num_cpc_codes': len(cpc_codes),
    'num_years': len(years),
    'cpc_sample': cpc_codes[:10],
    'years_sample': years[:5] if years else []
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:9': ['cpc_definition'], 'var_functions.execute_python:14': {'num_records': 277813, 'sample_keys': ['cpc', 'publication_date'], 'sample_cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}}

exec(code, env_args)

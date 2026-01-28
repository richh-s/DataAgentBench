code = """import json
import re
from collections import defaultdict
import pandas as pd

# Load the query result from file
file_path = var_functions.query_db:10
with open(file_path, 'r') as f:
    data = json.load(f)

# Filter for Germany patents granted in second half of 2019
germany_patents = []
month_patterns = [
    'July', 'August', 'September', 'October', 'November', 'December'
]

for record in data:
    grant_date = record.get('grant_date', '')
    patents_info = record.get('Patents_info', '')
    cpc = record.get('cpc', '[]')
    
    # Check if it's a Germany patent
    if 'DE-' not in patents_info:
        continue
        
    # Check if grant date is in second half of 2019
    if '2019' not in grant_date:
        continue
        
    has_month = any(month.lower() in grant_date.lower() for month in month_patterns)
    if not has_month:
        continue
    
    # Parse CPC codes
    try:
        cpc_codes = json.loads(cpc)
    except:
        cpc_codes = []
    
    germany_patents.append({
        'patents_info': patents_info,
        'grant_date': grant_date,
        'cpc_codes': cpc_codes
    })

print(f"Found {len(germany_patents)} Germany patents granted in second half 2019")

# Extract CPC codes at level 4 and count by year
cpc_counts = defaultdict(lambda: defaultdict(int))

cpc_level4_map = {}  # Map full code to level 4 code

for patent in germany_patents:
    for cpc_entry in patent['cpc_codes']:
        code = cpc_entry.get('code', '')
        if not code:
            continue
            
        # Extract level 4 code (format like A61F5/01)
        parts = code.split('/')
        if len(parts) >= 2:
            main_class = parts[0]
            sub_class = parts[1]
            
            # For level 4, we want the main class and first 2 digits of subclass
            # Or sometimes format is like A61F5/0127 - level 4 would be A61F5/01
            if len(sub_class) >= 2:
                level4_code = f"{main_class}/{sub_class[:2]}"
                cpc_level4_map[code] = level4_code
                cpc_counts[level4_code][2019] += 1

print(f"Found {len(cpc_counts)} unique CPC level 4 codes")

# Display sample of CPC codes
sample_codes = list(cpc_counts.items())[:5]
for code, counts in sample_codes:
    print(f"{code}: {counts}")

# Now we need to query CPC definitions for these level 4 codes
cpc_codes_list = list(cpc_counts.keys())
print(f"\nTotal CPC level 4 codes to query: {len(cpc_codes_list)}")

# For testing, let's use the first few codes
print("\nSample codes:", cpc_codes_list[:10])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['cpc_definition']}

exec(code, env_args)

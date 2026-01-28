code = """import json
import re
from collections import defaultdict

# Load the query result from the file path stored in the variable
file_path = locals()['var_functions.query_db:10']

with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total records loaded: {len(data)}")

# Filter for Germany patents granted in second half of 2019
germany_patents = []
month_patterns = ['July', 'August', 'September', 'October', 'November', 'December']

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

# Extract CPC codes at level 4 and count them
cpc_counts = defaultdict(int)
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
            if len(sub_class) >= 2:
                level4_code = f"{main_class}/{sub_class[:2]}"
                cpc_level4_map[code] = level4_code
                cpc_counts[level4_code] += 1

print(f"Found {len(cpc_counts)} unique CPC level 4 codes")

# Display the top 10 most common CPC level 4 codes
sorted_codes = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)
print("\nTop 10 CPC Level 4 codes by patent count:")
for code, count in sorted_codes[:10]:
    print(f"  {code}: {count} patents")

# Prepare list of CPC codes to query from the definition database
cpc_codes_to_query = list(cpc_counts.keys())
print(f"\nPrepared {len(cpc_codes_to_query)} unique CPC level 4 codes for definition lookup")

# Save the CPC counts data for later use
result_data = {
    'cpc_counts': dict(cpc_counts),
    'total_patents': len(germany_patents),
    'cpc_level4_map': cpc_level4_map
}

print("\n__RESULT__:")
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['cpc_definition']}

exec(code, env_args)

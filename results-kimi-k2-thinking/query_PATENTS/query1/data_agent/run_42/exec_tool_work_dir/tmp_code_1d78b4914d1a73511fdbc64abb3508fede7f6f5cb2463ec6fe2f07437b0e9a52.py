code = """import json
import re

# Access file paths from storage
query_db_6_path = locals()['var_functions.query_db:6']
query_db_11_path = locals()['var_functions.query_db:11']

# Read the CPC definition data (level 5)
with open(query_db_6_path, 'r') as f:
    cpc_level5_data = json.load(f)

# Create set of level 5 CPC symbols
level5_symbols = set()
for item in cpc_level5_data:
    symbol = item['symbol']
    level5_symbols.add(symbol)

print(f"Total level 5 CPC symbols: {len(level5_symbols)}")
print(f"Sample level 5 symbols: {list(level5_symbols)[:10]}")

# Read publication data
with open(query_db_11_path, 'r') as f:
    publication_data = json.load(f)

# Data structure for storing yearly counts for each CPC code at level 5
cpc_yearly_counts = {}  # {cpc_code: {year: count}}

# Process each publication
for pub in publication_data:
    cpc_json = pub['cpc']
    pub_date_str = pub['publication_date']
    
    # Parse publication year
    try:
        year_match = re.search(r'\d{4}', pub_date_str)
        if year_match:
            year = int(year_match.group())
        else:
            continue
    except:
        continue
    
    # Parse CPC codes
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_item in cpc_list:
            code = cpc_item['code']
            
            # Extract the group part (level 5) from the CPC code
            # For codes like "C01B33/00", the group is "C01B"
            # For codes like "H01M10/0565", the group is "H01M"
            match = re.match(r'([A-Z]\d{2}[A-Z])', code)
            if match:
                group_code = match.group(1)
                
                # Check if this group code is a level 5 CPC code
                if group_code in level5_symbols:
                    
                    # Initialize if not exists
                    if group_code not in cpc_yearly_counts:
                        cpc_yearly_counts[group_code] = {}
                    
                    # Increment count for this year
                    if year not in cpc_yearly_counts[group_code]:
                        cpc_yearly_counts[group_code][year] = 0
                    cpc_yearly_counts[group_code][year] += 1
            
    except Exception as e:
        continue

print(f"Total CPC level 5 group codes with data: {len(cpc_yearly_counts)}")
if cpc_yearly_counts:
    sample_cpc = list(cpc_yearly_counts.keys())[0]
    print(f"Sample CPC group {sample_cpc} yearly counts: {cpc_yearly_counts[sample_cpc]}")

# Determine year range
all_years = set()
for counts in cpc_yearly_counts.values():
    all_years.update(counts.keys())

if all_years:
    min_year = min(all_years)
    max_year = max(all_years)
    print(f"Year range: {min_year} to {max_year}")
else:
    print("No years found")
    min_year = max_year = None

# Prepare data for output
result_data = {
    'cpc_yearly_counts': cpc_yearly_counts,
    'year_range': [min_year, max_year] if all_years else None,
    'total_cpc_codes': len(cpc_yearly_counts),
    'total_publications': len(publication_data)
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:12': {'cpc_yearly_counts': {}, 'year_range': None, 'total_cpc_codes': 0, 'total_publications': 277813}}

exec(code, env_args)

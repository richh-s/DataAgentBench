code = """import json
import re
from datetime import datetime

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

print(f"Total publications: {len(publication_data)}")

# Data structure for storing yearly counts for each CPC code at level 5
cpc_yearly_counts = {}  # {cpc_code: {year: count}}

# Process each publication
for pub in publication_data:
    cpc_json = pub['cpc']
    pub_date_str = pub['publication_date']
    
    # Parse publication year
    try:
        # Handle format like "Aug 3rd, 2021"
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
            
            # Check if this is a level 5 CPC code
            if code in level5_symbols:
                cpc_level5 = code
                
                # Initialize if not exists
                if cpc_level5 not in cpc_yearly_counts:
                    cpc_yearly_counts[cpc_level5] = {}
                
                # Increment count for this year
                if year not in cpc_yearly_counts[cpc_level5]:
                    cpc_yearly_counts[cpc_level5][year] = 0
                cpc_yearly_counts[cpc_level5][year] += 1
            
    except Exception as e:
        continue

print(f"Total CPC level 5 codes with data: {len(cpc_yearly_counts)}")
if cpc_yearly_counts:
    sample_cpc = list(cpc_yearly_counts.keys())[0]
    print(f"Sample CPC {sample_cpc} yearly counts: {cpc_yearly_counts[sample_cpc]}")

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

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)

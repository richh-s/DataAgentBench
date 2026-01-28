code = """import json
import re
import ast

# Get the file path from storage
file_path = locals()['var_functions.query_db:2']
print('File path:', file_path)

# Load the data
with open(file_path, 'r') as f:
    patents_data = json.load(f)

print('Loaded', len(patents_data), 'patent records')

# Filter for German patents granted in second half of 2019
second_half_patterns = ['2019', 'Jul', 'Jul.', 'July', 'Aug', 'Aug.', 'August', 'Sep', 'Sep.', 'September', 'Oct', 'Oct.', 'October', 'Nov', 'Nov.', 'November', 'Dec', 'Dec.', 'December']
german_patents = []

for patent in patents_data:
    # Check if it's German (DE in patents_info)
    patents_info = patent['Patents_info']
    if 'DE-' in patents_info or ' from DE,' in patents_info:
        # Check grant date contains 2019 and second half indicators
        grant_date = patent['grant_date']
        if '2019' in grant_date:
            # More robust second half check
            has_second_half = any(pattern in grant_date for pattern in ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
            if has_second_half:
                german_patents.append(patent)

print('Found', len(german_patents), 'German patents from second half 2019')

# Extract CPC codes and filing years
cpc_year_counts = {}
cpc_all_codes = {}

for patent in german_patents:
    try:
        # Parse CPC field (it's a JSON-like string)
        cpc_str = patent['cpc']
        cpc_entries = ast.literal_eval(cpc_str)
        
        # Get filing year from filing_date
        filing_date = patent['filing_date']
        year_match = re.search(r'(\d{4})', filing_date)
        
        if year_match and cpc_entries:
            year = int(year_match.group(1))
            
            # Process each CPC entry
            for entry in cpc_entries:
                if isinstance(entry, dict) and 'code' in entry:
                    cpc_code = entry['code']
                    
                    # Extract level 4 code (main group level)
                    # Format: Section(1)/Class(2)/Subclass(1) Group(1-3)/Subgroup(2+)
                    # Level 4 is the main group before the slash
                    if '/' in cpc_code:
                        main_part = cpc_code.split('/')[0]
                        # Ensure we have at least 4 characters for level 4
                        if len(main_part) >= 4:
                            level4_code = main_part
                            
                            # Initialize if new
                            if level4_code not in cpc_year_counts:
                                cpc_year_counts[level4_code] = {}
                                cpc_all_codes[level4_code] = set()
                            
                            # Count patents by year for this CPC
                            cpc_year_counts[level4_code][year] = cpc_year_counts[level4_code].get(year, 0) + 1
                            cpc_all_codes[level4_code].add(cpc_code)
    except Exception as e:
        continue

print('Extracted data for', len(cpc_year_counts), 'CPC level 4 groups')

# Show a sample
for i, (cpc, years) in enumerate(list(cpc_year_counts.items())[:3]):
    print(f'CPC {cpc}: {sorted(years.items())}')
    print(f'  Sample full codes: {list(cpc_all_codes[cpc])[:2]}')

# Prepare result for next step
result = {
    'cpc_year_counts': {k: dict(v) for k, v in cpc_year_counts.items()},
    'cpc_all_codes': {k: list(v) for k, v in cpc_all_codes.items()},
    'total_german_patents': len(german_patents)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

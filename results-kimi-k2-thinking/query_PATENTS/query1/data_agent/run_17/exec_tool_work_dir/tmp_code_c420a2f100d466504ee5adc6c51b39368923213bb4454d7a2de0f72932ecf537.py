code = """import json
import re
from collections import defaultdict

# Read the query results - the variable contains a file path
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    data = json.load(f)

print('Number of records:', len(data))

# Extract CPC codes and publication dates
cpc_year_counts = defaultdict(lambda: defaultdict(int))
years = set()
parse_errors = 0

for record in data:
    cpc_json_str = record.get('cpc', '')
    pub_date = record.get('publication_date', '')
    
    # Extract year from publication date
    if pub_date:
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
            if 1900 <= year <= 2100:  # Reasonable year range
                years.add(year)
                
                # Parse CPC codes
                if cpc_json_str and cpc_json_str != '[]':
                    try:
                        cpc_list = json.loads(cpc_json_str)
                        
                        for cpc_item in cpc_list:
                            code = cpc_item.get('code', '')
                            if code and isinstance(code, str):
                                # Extract main group (before slash)
                                parts = code.split('/')
                                main_group = parts[0]
                                
                                # Normalize to 7 characters (level 5)
                                # CPC codes are structured like: H01M04/1315
                                # Level 1: H
                                # Level 2: H01
                                # Level 3: H01M
                                # Level 4: H01M04
                                # Level 5: H01M04/13 (first 7 chars)
                                if len(main_group) >= 1:
                                    # Take first 7 chars total including the slash
                                    if len(code) >= 7:
                                        level5_code = code[:7]
                                    else:
                                        # Pad if necessary
                                        level5_code = code.ljust(7, '0')
                                    
                                    cpc_year_counts[level5_code][year] += 1
                                    
                    except json.JSONDecodeError:
                        parse_errors += 1
                        continue

print('Unique CPC groups (level 5):', len(cpc_year_counts))
print('Year range:', min(years) if years else None, 'to', max(years) if years else None)
print('Parse errors:', parse_errors)

# Show sample data
if cpc_year_counts:
    print('\\nSample CPC counts:')
    for i, (cpc, year_counts) in enumerate(list(cpc_year_counts.items())[:10]):
        print(cpc + ':', dict(sorted(list(year_counts.items())[:3])))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

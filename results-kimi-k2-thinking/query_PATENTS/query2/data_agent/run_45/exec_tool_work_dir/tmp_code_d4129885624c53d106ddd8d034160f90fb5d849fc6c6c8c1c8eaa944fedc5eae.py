code = """import json
import re
from collections import defaultdict

# Load German patents data from second half 2019
file_path = locals()['var_functions.query_db:38']
with open(file_path, 'r') as f:
    german_patents = json.load(f)

print('Loaded', len(german_patents), 'German patents from second half 2019')

# Process to extract CPC codes at level 4 and count patents
cpc_year_counts = defaultdict(lambda: defaultdict(int))
cpc_full_codes = defaultdict(set)

for patent in german_patents:
    try:
        # Parse CPC JSON string
        cpc_entries = json.loads(patent['cpc'])
        
        for entry in cpc_entries:
            if isinstance(entry, dict) and 'code' in entry:
                full_code = entry['code']
                
                # Extract level 4: main group before slash (e.g., 'B41F21' from 'B41F21/102')
                if '/' in full_code:
                    main_group = full_code.split('/')[0]
                    # Ensure we have a valid level 4 code (at least section + class + subclass + group)
                    if len(main_group) >= 4:
                        level4 = main_group
                        # Count patents for 2019 (all grants were in 2019)
                        cpc_year_counts[level4][2019] += 1
                        cpc_full_codes[level4].add(full_code)
    except Exception as e:
        print(f'Error processing patent: {e}')
        continue

print('Extracted CPC data for', len(cpc_year_counts), 'level 4 groups')
print('Sample groups:', list(cpc_year_counts.keys())[:8])

# Show counts
for cpc, years in list(cpc_year_counts.items())[:5]:
    print(f'  {cpc}: {dict(years)} - Sample codes: {list(cpc_full_codes[cpc])[:2]}')

result = {
    'cpc_year_counts': dict(cpc_year_counts),
    'cpc_full_codes': {k: list(v) for k, v in cpc_full_codes.items()},
    'total_patents': len(german_patents)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'cpc_year_counts': {}, 'cpc_all_codes': {}, 'total_german_patents': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'country_code': 'US'}, {'country_code': 'DE'}, {'country_code': 'CU'}, {'country_code': 'EP'}, {'country_code': 'BR'}, {'country_code': 'AU'}, {'country_code': 'CN'}, {'country_code': 'SE'}, {'country_code': 'NL'}, {'country_code': 'RU'}, {'country_code': 'UA'}, {'country_code': 'DK'}, {'country_code': 'NO'}, {'country_code': 'GB'}, {'country_code': 'HU'}, {'country_code': 'AT'}, {'country_code': 'HR'}, {'country_code': 'ES'}, {'country_code': 'PL'}, {'country_code': 'GR'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'cpc_year_counts': {}, 'full_codes': {}, 'total_patents': 34}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)

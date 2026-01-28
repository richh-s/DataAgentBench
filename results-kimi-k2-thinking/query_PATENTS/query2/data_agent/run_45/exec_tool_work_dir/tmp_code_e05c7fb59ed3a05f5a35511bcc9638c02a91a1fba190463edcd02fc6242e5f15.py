code = """import json
import re
import ast
from collections import defaultdict

# Load the German patents data
file_path = var_functions.query_db:26
with open(file_path, 'r') as f:
    german_patents = json.load(f)

print('Found', len(german_patents), 'German patents from second half 2019')

# Process the patents to extract CPC codes and filing years
cpc_data = defaultdict(lambda: defaultdict(int))
cpc_full_codes = defaultdict(set)

for patent in german_patents:
    # Parse CPC codes
    try:
        cpc_str = patent['cpc']
        cpc_entries = ast.literal_eval(cpc_str)
        
        for entry in cpc_entries:
            if isinstance(entry, dict) and 'code' in entry:
                full_code = entry['code']
                
                # Extract level 4: main group (before slash)
                if '/' in full_code:
                    main_group = full_code.split('/')[0]
                    # Level 4 is typically the full main group (section + class + subclass + group)
                    # This is usually at least 4 characters, often more like "B41F21"
                    if len(main_group) >= 4:
                        cpc_level4 = main_group
                        
                        # Count patents for this CPC group
                        cpc_data[cpc_level4][2019] += 1  # All are from 2019 based on grant date
                        cpc_full_codes[cpc_level4].add(full_code)
    except Exception as e:
        continue

print('Extracted', len(cpc_data), 'CPC level 4 groups')
print('Sample CPC groups:', list(cpc_data.keys())[:10])

# Show counts for each group
for cpc, counts in list(cpc_data.items())[:10]:
    print(f'{cpc}: {dict(counts)}')

result = {
    'cpc_data': dict(cpc_data),
    'cpc_full_codes': {k: list(v) for k, v in cpc_full_codes.items()},
    'total_patents': len(german_patents)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'cpc_year_counts': {}, 'cpc_all_codes': {}, 'total_german_patents': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'country_code': 'US'}, {'country_code': 'DE'}, {'country_code': 'CU'}, {'country_code': 'EP'}, {'country_code': 'BR'}, {'country_code': 'AU'}, {'country_code': 'CN'}, {'country_code': 'SE'}, {'country_code': 'NL'}, {'country_code': 'RU'}, {'country_code': 'UA'}, {'country_code': 'DK'}, {'country_code': 'NO'}, {'country_code': 'GB'}, {'country_code': 'HU'}, {'country_code': 'AT'}, {'country_code': 'HR'}, {'country_code': 'ES'}, {'country_code': 'PL'}, {'country_code': 'GR'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

code = """import json
import ast
from collections import defaultdict

# Get the file path from loca`ls
file_path = locals()['var_functions.query_db:26']
print('Loading from:', file_path)

# Load German patents data
with open(file_path, 'r') as f:
    german_patents = json.load(f)

print('Found', len(german_patents), 'German patents from second half 2019')

# Process patents to extract CPC codes at level 4
cpc_year_counts = defaultdict(lambda: defaultdict(int))
full_codes = defaultdict(set)

for patent in german_patents:
    try:
        cpc_str = patent['cpc']
        cpc_entries = ast.literal_eval(cpc_str)
        
        for entry in cpc_entries:
            if isinstance(entry, dict) and 'code' in entry:
                full_code = entry['code']
                
                # Extract level 4 code (main group before slash)
                if '/' in full_code:
                    main_group = full_code.split('/')[0]
                    if len(main_group) >= 4:
                        level4 = main_group
                        # All these patents were granted in 2019, count them
                        cpc_year_counts[level4][2019] += 1
                        full_codes[level4].add(full_code)
    except Exception as e:
        continue

print('Extracted', len(cpc_year_counts), 'CPC level 4 groups')
print('Sample CPC groups:', list(cpc_year_counts.keys())[:10])

# Show the counts
for cpc, years in list(cpc_year_counts.items())[:10]:
    print(f'{cpc}: {dict(years)}')

result = {
    'cpc_year_counts': dict(cpc_year_counts),
    'full_codes': {k: list(v) for k, v in full_codes.items()},
    'total_patents': len(german_patents)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'cpc_year_counts': {}, 'cpc_all_codes': {}, 'total_german_patents': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'country_code': 'US'}, {'country_code': 'DE'}, {'country_code': 'CU'}, {'country_code': 'EP'}, {'country_code': 'BR'}, {'country_code': 'AU'}, {'country_code': 'CN'}, {'country_code': 'SE'}, {'country_code': 'NL'}, {'country_code': 'RU'}, {'country_code': 'UA'}, {'country_code': 'DK'}, {'country_code': 'NO'}, {'country_code': 'GB'}, {'country_code': 'HU'}, {'country_code': 'AT'}, {'country_code': 'HR'}, {'country_code': 'ES'}, {'country_code': 'PL'}, {'country_code': 'GR'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)

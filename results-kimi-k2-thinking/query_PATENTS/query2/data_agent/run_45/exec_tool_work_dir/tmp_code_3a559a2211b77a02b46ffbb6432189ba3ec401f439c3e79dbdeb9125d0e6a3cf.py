code = """import json
from collections import defaultdict

# Load German patents data
file_path = locals()['var_functions.query_db:26']
with open(file_path, 'r') as f:
    german_patents = json.load(f)

print('Found', len(german_patents), 'German patents from second half 2019')

# Debug first few CPC entries
print('\nDebugging first 3 patents:')
for i in range(min(3, len(german_patents))):
    patent = german_patents[i]
    print(f'\nPatent {i+1}:')
    print('  Grant date:', patent['grant_date'])
    print('  CPC field (first 200 chars):', patent['cpc'][:200])
    
    # Try to parse as JSON
    try:
        cpc_entries = json.loads(patent['cpc'])
        print(f'  Parsed {len(cpc_entries)} CPC entries')
        if cpc_entries:
            print('  First entry:', cpc_entries[0])
    except Exception as e:
        print('  Error parsing CPC:', e)

# Now process all patents properly
cpc_counts = defaultdict(lambda: defaultdict(int))
full_codes = defaultdict(set)

for patent in german_patents:
    try:
        # Parse CPC field as JSON
        cpc_entries = json.loads(patent['cpc'])
        
        for entry in cpc_entries:
            if isinstance(entry, dict) and 'code' in entry:
                full_code = entry['code']
                
                # Extract level 4 (main group, before the slash)
                if '/' in full_code:
                    main_group = full_code.split('/')[0]
                    # Level 4 code is the full main group (e.g., 'B41F21' from 'B41F21/102')
                    if len(main_group) >= 4:
                        level4 = main_group
                        # Count patents (all from 2019)
                        cpc_counts[level4][2019] += 1
                        full_codes[level4].add(full_code)
    except Exception as e:
        print(f'Error processing patent: {e}')
        continue

print(f'\nSuccessfully extracted data for {len(cpc_counts)} CPC level 4 groups')
if cpc_counts:
    print('Sample CPC groups and counts:')
    for cpc, years in list(cpc_counts.items())[:10]:
        print(f'  {cpc}: {dict(years)}')
else:
    print('No CPC data extracted. Debug info:')
    if german_patents:
        print('Sample CPC field from first patent:', german_patents[0]['cpc'][:100])

result = {
    'cpc_counts': dict(cpc_counts),
    'full_codes': {k: list(v) for k, v in full_codes.items()},
    'total': len(german_patents)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'cpc_year_counts': {}, 'cpc_all_codes': {}, 'total_german_patents': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'country_code': 'US'}, {'country_code': 'DE'}, {'country_code': 'CU'}, {'country_code': 'EP'}, {'country_code': 'BR'}, {'country_code': 'AU'}, {'country_code': 'CN'}, {'country_code': 'SE'}, {'country_code': 'NL'}, {'country_code': 'RU'}, {'country_code': 'UA'}, {'country_code': 'DK'}, {'country_code': 'NO'}, {'country_code': 'GB'}, {'country_code': 'HU'}, {'country_code': 'AT'}, {'country_code': 'HR'}, {'country_code': 'ES'}, {'country_code': 'PL'}, {'country_code': 'GR'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'cpc_year_counts': {}, 'full_codes': {}, 'total_patents': 34}}

exec(code, env_args)

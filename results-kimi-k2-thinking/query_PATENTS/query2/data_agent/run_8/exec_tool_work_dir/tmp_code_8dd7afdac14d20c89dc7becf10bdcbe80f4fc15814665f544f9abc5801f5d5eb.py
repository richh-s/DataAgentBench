code = """import json

# Load the processed data
file_path = locals()['var_functions.execute_python:18']
with open(file_path, 'r') as f:
    processed_data = json.load(f)

cpc_codes = processed_data['cpc_codes']

print('Total unique CPC Level 4 codes:', len(cpc_codes))
print('Sample codes:', cpc_codes[:15])

# Extract main groups for querying CPC definitions
main_groups = set()
for code in cpc_codes:
    if '/' in code:
        main_group = code.split('/')[0]
        main_groups.add(main_group)

print('Unique main groups:', len(main_groups))
print('Sample main groups:', list(main_groups)[:10])

result = {
    'total_cpc_level4_codes': len(cpc_codes),
    'unique_main_groups': len(main_groups),
    'main_groups': list(main_groups)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_patents_2019': 3838, 'sample_records_count': 3}, 'var_functions.execute_python:10': {'total_de_patents_2019': 25, 'de_patents_h2_2019': 12}, 'var_functions.execute_python:12': {'total_german_patents_h2_2019': 13, 'total_cpc_entries': 137, 'total_cpc_level4_entries': 137, 'unique_cpc_level4_codes': 81, 'sample_codes': ['B29C49/06', 'F02N2200/022', 'C04B2235/543', 'H01R35/04', 'H01J49/003', 'B29C49/58', 'H02J7/34', 'A61B90/70', 'F02N11/04', 'H01J49/421']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:26': {'total_patents': 129, 'unique_cpc_codes': 77, 'top_cpc_codes': [['C04B2235/656', 4], ['C04B2235/322', 4], ['C04B35/645', 4], ['H01J49/164', 3], ['H01J49/046', 3], ['B29C2049/589', 3], ['A61F5/14', 2], ['A61F5/012', 2], ['A61F5/011', 2], ['A43B17/00', 2], ['A43B7/20', 2], ['H01J49/043', 2], ['H01R2201/26', 2], ['C04B2235/965', 2], ['C04B2235/77', 2], ['C04B2235/72', 2], ['C04B2235/666', 2], ['C04B2235/662', 2], ['C04B2235/661', 2], ['C04B2235/658', 2]]}}

exec(code, env_args)

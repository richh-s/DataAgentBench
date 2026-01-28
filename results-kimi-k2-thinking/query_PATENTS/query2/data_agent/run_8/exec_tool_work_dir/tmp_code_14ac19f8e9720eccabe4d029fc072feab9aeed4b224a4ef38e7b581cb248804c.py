code = """import json
import pandas as pd
from collections import defaultdict
import numpy as np

# Load processed patent data
file_path = locals()['var_functions.execute_python:18']
with open(file_path, 'r') as f:
    processed_data = json.load(f)

de_patents = processed_data['de_patents']
cpc_counts = processed_data['cpc_counts']
cpc_codes = processed_data['cpc_codes']

print('Total Germany H2 2019 patents with CPC:', len(de_patents))
print('Unique CPC Level 4 codes:', len(cpc_codes))

# Sort CPC codes by count
sorted_cpc = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)

print('Top 10 CPC codes by count:')
for code, count in sorted_cpc[:10]:
    print(code + ': ' + str(count))

# Print top 20
print('\nTop 20 CPC codes with highest patent counts:')
for i, (code, count) in enumerate(sorted_cpc[:20], 1):
    print(str(i) + '. ' + code + ': ' + str(count) + ' patents')

# Extract main groups for lookup
cpc_lookup_codes = []
for code in cpc_codes:
    if '/' in code:
        main_group = code.split('/')[0]
        cpc_lookup_codes.append(main_group)
    else:
        cpc_lookup_codes.append(code)

unique_lookup = list(set(cpc_lookup_codes))
print('\nUnique main groups for lookup:', len(unique_lookup))

result = {
    'total_patents': len(de_patents),
    'unique_cpc_codes': len(cpc_codes),
    'top_cpc_codes': sorted_cpc[:20],
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_patents_2019': 3838, 'sample_records_count': 3}, 'var_functions.execute_python:10': {'total_de_patents_2019': 25, 'de_patents_h2_2019': 12}, 'var_functions.execute_python:12': {'total_german_patents_h2_2019': 13, 'total_cpc_entries': 137, 'total_cpc_level4_entries': 137, 'unique_cpc_level4_codes': 81, 'sample_codes': ['B29C49/06', 'F02N2200/022', 'C04B2235/543', 'H01R35/04', 'H01J49/003', 'B29C49/58', 'H02J7/34', 'A61B90/70', 'F02N11/04', 'H01J49/421']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json'}

exec(code, env_args)

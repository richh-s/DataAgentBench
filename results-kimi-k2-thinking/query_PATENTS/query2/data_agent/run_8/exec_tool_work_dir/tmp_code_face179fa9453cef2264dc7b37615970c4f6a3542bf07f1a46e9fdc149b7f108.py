code = """import json
import pandas as pd

# Load processed patent data
file_path = locals()['var_functions.execute_python:18']
with open(file_path, 'r') as f:
    processed_data = json.load(f)

de_patents = processed_data['de_patents']
cpc_counts = processed_data['cpc_counts']
cpc_codes = processed_data['cpc_codes']

# Get top CPC codes
sorted_cpc = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:20]

result = {
    'total_patents': len(de_patents),
    'unique_cpc_codes': len(cpc_codes),
    'top_cpc_codes': sorted_cpc
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_patents_2019': 3838, 'sample_records_count': 3}, 'var_functions.execute_python:10': {'total_de_patents_2019': 25, 'de_patents_h2_2019': 12}, 'var_functions.execute_python:12': {'total_german_patents_h2_2019': 13, 'total_cpc_entries': 137, 'total_cpc_level4_entries': 137, 'unique_cpc_level4_codes': 81, 'sample_codes': ['B29C49/06', 'F02N2200/022', 'C04B2235/543', 'H01R35/04', 'H01J49/003', 'B29C49/58', 'H02J7/34', 'A61B90/70', 'F02N11/04', 'H01J49/421']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json'}

exec(code, env_args)

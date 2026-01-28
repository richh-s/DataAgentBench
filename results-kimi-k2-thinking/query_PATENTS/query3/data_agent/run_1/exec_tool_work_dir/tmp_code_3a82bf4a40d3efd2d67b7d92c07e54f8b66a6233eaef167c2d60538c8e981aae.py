code = """import json
import re
from collections import defaultdict

# Load the full results from the queries
result_path_1 = locals()['var_functions.query_db:5']  # General query result
result_path_2 = locals()['var_functions.query_db:6']  # UNIV CALIFORNIA query result

# Read the full results
with open(result_path_1, 'r') as f:
    general_results = json.load(f)

with open(result_path_2, 'r') as f:
    uc_results = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'total_patents': len(general_results),
    'uc_patents': len(uc_results),
    'sample_structure': list(uc_results[0].keys()) if uc_results else None,
    'sample_patents_info': uc_results[0]['Patents_info'] if uc_results else None
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Load CHI papers from MongoDB
chi_papers_data = locals().get('var_functions.query_db:14')

# Check if it's a file path string or actual data
if isinstance(chi_papers_data, str) and chi_papers_data.endswith('.json'):
    with open(chi_papers_data, 'r') as f:
        chi_papers = json.load(f)
else:
    chi_papers = chi_papers_data

print(f"Total paper documents retrieved: {len(chi_papers)}")
print("First paper example:")
if chi_papers:
    print(json.dumps(chi_papers[0], indent=2)[:500])

result = {"total_papers": len(chi_papers)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'status': 'success', 'total_records': 100, 'message': 'Loaded 100 citation records for 2020'}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

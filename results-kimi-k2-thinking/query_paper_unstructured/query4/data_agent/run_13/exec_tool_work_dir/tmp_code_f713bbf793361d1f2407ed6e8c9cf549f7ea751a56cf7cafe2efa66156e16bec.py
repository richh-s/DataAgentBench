code = """import json
import re

# Load paper documents from MongoDB
paper_file = locals()['var_functions.query_db:8']
with open(paper_file, 'r') as f:
    papers = json.load(f)

# Debug: Check first few papers to understand structure
print('__RESULT__:')
print(json.dumps({'total_papers': len(papers), 'first_paper_keys': list(papers[0].keys()) if papers else []}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': []}

exec(code, env_args)

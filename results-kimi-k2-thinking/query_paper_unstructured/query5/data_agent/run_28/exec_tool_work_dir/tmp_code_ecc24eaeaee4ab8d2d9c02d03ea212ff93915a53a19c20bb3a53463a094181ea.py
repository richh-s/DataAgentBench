code = """import json

# Get file paths using locals() - these are JSON strings
storage_vars = locals()
citations_path = storage_vars['var_functions.query_db:0']
papers_path = storage_vars['var_functions.query_db:6']

# Load data
with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

print('Citations 2020 count:', len(citations_2020))
print('Paper docs count:', len(paper_docs))
print('First citation keys:', list(citations_2020[0].keys()))
print('Sample paper filename:', paper_docs[0]['filename'])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

code = """import json

# Access the stored results
paper_docs = locals()['var_functions.query_db:3']
citations = locals()['var_functions.query_db:2']

# If they are file paths, load them
if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations = json.load(f)

print('Paper docs count:', len(paper_docs))
print('Citations count:', len(citations))
print('First paper doc keys:', list(paper_docs[0].keys()))
print('First citation keys:', list(citations[0].keys()))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

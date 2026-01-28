code = """import json

# Read the full citation results
citation_path = locals()['var_functions.query_db:0']
with open(citation_path, 'r') as f:
    citations_2020 = json.load(f)

# Read the full paper documents
paper_path = locals()['var_functions.query_db:2']
with open(paper_path, 'r') as f:
    paper_docs = json.load(f)

# Check counts
print('__RESULT__:')
print(json.dumps({
    'citation_records_2020': len(citations_2020),
    'paper_documents': len(paper_docs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

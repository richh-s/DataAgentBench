code = """import json

paper_docs_path = var_functions.query_db:3
citations_path = var_functions.query_db:2

print('type paper_docs_path:', type(paper_docs_path))
print('type citations_path:', type(citations_path))

if isinstance(paper_docs_path, str):
    with open(paper_docs_path) as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_path

if isinstance(citations_path, str):
    with open(citations_path) as f:
        citations = json.load(f)
else:
    citations = citations_path

print('papers:', len(paper_docs))
print('citations:', len(citations))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

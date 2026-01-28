code = """import json

paper_docs = var_functions.query_db:3
citations = var_functions.query_db:2

if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    paper_docs = json.load(open(paper_docs))

if isinstance(citations, str) and citations.endswith('.json'):
    citations = json.load(open(citations))

print("Papers:", len(paper_docs))
print("Citations:", len(citations))
print("Sample paper:", paper_docs[0]['filename'])
print("Sample citation:", citations[0])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

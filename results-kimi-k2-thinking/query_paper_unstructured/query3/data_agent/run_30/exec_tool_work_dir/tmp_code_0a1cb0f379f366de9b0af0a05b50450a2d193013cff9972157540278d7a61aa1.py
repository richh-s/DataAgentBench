code = """import json

# Read paper documents
paper_docs_path = var_functions.query_db:2
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read citation data
citations_path = var_functions.query_db:10
with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f"Paper documents: {len(paper_docs)}")
print(f"Citation records: {len(citations)}")
print("First document:", paper_docs[0]['filename'])
print("First citation:", citations[0]['title'])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

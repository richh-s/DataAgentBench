code = """import json
import os

# Read the MongoDB paper documents
paper_docs_path = var_functions.query_db:3
if isinstance(paper_docs_path, str) and paper_docs_path.endswith('.json'):
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db:3

# Read the SQLite citations
citations_path = var_functions.query_db:2
if isinstance(citations_path, str) and citations_path.endswith('.json'):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
else:
    citations = var_functions.query_db:2

print(f"Number of paper documents: {len(paper_docs)}")
print(f"Number of citation records: {len(citations)}")

# Show first few documents to understand structure
print("\nFirst paper document:")
print(json.dumps(paper_docs[0], indent=2)[:1000])

print("\nFirst citation record:")
print(json.dumps(citations[0], indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

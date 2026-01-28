code = """import json

# Get the results from storage
paper_docs_result = locals()['var_functions.query_db:3']
citations_result = locals()['var_functions.query_db:2']

# Load paper documents
if isinstance(paper_docs_result, str) and paper_docs_result.endswith('.json'):
    with open(paper_docs_result, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_result

# Load citations
if isinstance(citations_result, str) and citations_result.endswith('.json'):
    with open(citations_result, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_result

print(f"Number of paper documents: {len(paper_docs)}")
print(f"Number of citation records: {len(citations)}")

# Show first few documents to understand structure
print("\nFirst paper document (preview):")
print(json.dumps(paper_docs[0], indent=2)[:500])

print("\nFirst citation record:")
print(json.dumps(citations[0], indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)

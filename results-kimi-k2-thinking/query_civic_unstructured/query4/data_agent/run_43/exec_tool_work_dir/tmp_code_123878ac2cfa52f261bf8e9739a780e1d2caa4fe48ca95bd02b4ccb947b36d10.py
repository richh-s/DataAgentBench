code = """import json

# Read the civic documents data
civic_docs_file = var_functions.query_db:4
civic_docs = []
with open(civic_docs_file, 'r') as f:
    for line in f:
        civic_docs.append(json.loads(line.strip()))

# Read the funding data
funding_file = var_functions.query_db:5
funding = []
with open(funding_file, 'r') as f:
    for line in f:
        funding.append(json.loads(line.strip()))

print("__RESULT__:")
print(json.dumps({
    "civic_docs_count": len(civic_docs),
    "funding_count": len(funding),
    "first_doc_preview": civic_docs[0]["text"][:500] if civic_docs else "No data"
}, default=str))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

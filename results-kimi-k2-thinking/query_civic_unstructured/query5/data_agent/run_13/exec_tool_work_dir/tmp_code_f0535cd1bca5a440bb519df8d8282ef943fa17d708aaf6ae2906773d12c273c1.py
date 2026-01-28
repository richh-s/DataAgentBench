code = """import json
import re

# Access the funding data (this is the query_db result not list_db)
funding_data = locals()['var_functions.query_db:0']

# If it's a string (file path), load it
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Access the civic docs data
civic_docs = locals()['var_functions.query_db:2']

# If it's a string (file path), load it
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "civic_docs_count": len(civic_docs),
    "sample_doc_keys": list(civic_docs[0].keys()) if civic_docs else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}}

exec(code, env_args)

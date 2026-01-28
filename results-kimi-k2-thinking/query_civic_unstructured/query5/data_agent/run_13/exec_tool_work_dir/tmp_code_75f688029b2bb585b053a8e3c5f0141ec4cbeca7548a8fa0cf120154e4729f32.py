code = """import json
import re

# Load civic documents data
civic_docs = locals()['var_functions.query_db:16']
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

# Load all civic documents (we need to get the full dataset)
# The query_db result is stored as a file path, let's read it
civic_docs_path = locals()['var_functions.query_db:2']
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs_full = json.load(f)
else:
    civic_docs_full = locals()['var_functions.query_db:2']

print("__RESULT__:")
print(json.dumps({
    "civic_docs_full_count": len(civic_docs_full),
    "sample_doc_keys": list(civic_docs_full[0].keys()) if civic_docs_full else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}, 'var_functions.execute_python:14': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

code = """import json
import re

# Load the full civic documents dataset
civic_docs_path = locals()['var_functions.query_db:2']
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs_full = json.load(f)
else:
    civic_docs_full = locals()['var_functions.query_db:2']

# Load the funding data
funding_data = locals()['var_functions.query_db:0']
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Step 1: Extract disaster-related projects from funding data
# Project names containing FEMA, CalOES, CalJPIA or other disaster indicators

print("__RESULT__:")
print(json.dumps({
    "civic_docs_total": len(civic_docs_full),
    "funding_records_total": len(funding_data),
    "sample_doc_filename": civic_docs_full[0]['filename'] if civic_docs_full else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}, 'var_functions.execute_python:14': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'civic_docs_full_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)

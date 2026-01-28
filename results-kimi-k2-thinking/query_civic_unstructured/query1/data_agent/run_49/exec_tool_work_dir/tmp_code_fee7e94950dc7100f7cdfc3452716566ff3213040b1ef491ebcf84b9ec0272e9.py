code = """import json
import re
import os

# Load civic documents
civic_file_path = locals().get('var_functions.query_db:2', '')
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
fund_file_path = locals().get('var_functions.query_db:0', '')
with open(fund_file_path, 'r') as f:
    funding_data = json.load(f)

print("Loaded documents: %d docs, %d funding records" % (len(civic_docs), len(funding_data)))

# Get first document text for analysis
doc1 = civic_docs[0]
text1 = doc1.get('text', '')
print("Text length: %d" % len(text1))
print("Text start:")
print(text1[:800])

print('__RESULT__:')
result = {
    "num_docs": len(civic_docs),
    "num_funding": len(funding_data),
    "first_doc_length": len(text1)
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)

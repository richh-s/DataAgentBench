code = """import json
import re
import os

# Load data
civic_key = 'var_functions.query_db:2'
civic_file_path = locals().get(civic_key, '')
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

fund_key = 'var_functions.query_db:0'
fund_file_path = locals().get(fund_key, '')
with open(fund_file_path, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Extract projects from first document to understand structure
doc1 = civic_docs[0]
text1 = doc1.get('text', '')
print(f"Text preview (first 1000 chars):\n{text1[:1000]}")

# Try to find project patterns - look for project sections
sections = re.split(r'\n\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*', text1)
print(f"\nFound {len(sections)} sections")

print('__RESULT__:')
print(json.dumps({
    "num_docs": len(civic_docs),
    "num_funding": len(funding_data),
    "doc_structure": "sections identified"
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}, 'var_functions.execute_python:16': {'success': True, 'civic_docs_count': 5, 'funding_count': 276, 'first_doc_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)

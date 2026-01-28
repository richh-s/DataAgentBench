code = """import json
import re

# Access the civic documents
civic_key = 'var_functions.query_db:2'
civic_docs = locals().get(civic_key, [])

print(f"Number of civic documents: {len(civic_docs)}")

# Get the text from the first document (as preview suggests structure)
sample_doc = civic_docs[0] if civic_docs else {}
sample_text = sample_doc.get('text', '')[:1000]

print('__RESULT__:')
print(json.dumps({
    "doc_count": len(civic_docs),
    "sample_preview": sample_text[:500]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}}

exec(code, env_args)

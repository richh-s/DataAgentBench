code = """import json
import os

# The civic result is a file path
 civic_file_path = r'C:\Users\ADMINI~1\AppData\Local\Temp\tmp9k5a5d3m.json'
# For Unix-like systems, use:
# civic_file_path = civic_result

try:
    with open(civic_file_path, 'r') as f:
        civic_docs = json.load(f)
    print(f"Successfully loaded {len(civic_docs)} civic documents")
    
    # Check first document
    if civic_docs:
        doc = civic_docs[0]
        print(f"First doc keys: {list(doc.keys())}")
        print(f"Has text field: {'text' in doc}")
        if 'text' in doc:
            print(f"Text preview: {doc['text'][:500]}")
    
    print('__RESULT__:')
    print(json.dumps({
        "success": True,
        "count": len(civic_docs),
        "sample_keys": list(civic_docs[0].keys()) if civic_docs else []
    }))
    
except Exception as e:
    print(f"Error loading file: {e}")
    print('__RESULT__:')
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}}

exec(code, env_args)

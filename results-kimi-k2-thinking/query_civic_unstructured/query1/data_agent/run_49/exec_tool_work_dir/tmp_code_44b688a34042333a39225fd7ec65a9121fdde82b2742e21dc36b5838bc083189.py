code = """import json
import os

try:
    # The civic result is stored as a file path string in the variable
    civic_key = 'var_functions.query_db:2'
    civic_file_path = locals().get(civic_key, '')
    
    print(f"File path: {civic_file_path}")
    
    # Load civic documents
    with open(civic_file_path, 'r') as f:
        civic_docs = json.load(f)
    
    print(f"Successfully loaded {len(civic_docs)} civic documents")
    
    # Check first document
    if civic_docs:
        first_doc = civic_docs[0]
        print(f"First doc keys: {list(first_doc.keys())}")
        print(f"Has text field: {'text' in first_doc}")
    
    # Funding data
    fund_key = 'var_functions.query_db:0'
    fund_file_path = locals().get(fund_key, '')
    
    with open(fund_file_path, 'r') as f:
        funding_data = json.load(f)
    
    print(f"Loaded {len(funding_data)} funding records")
    
    print('__RESULT__:')
    print(json.dumps({
        "success": True,
        "civic_docs_count": len(civic_docs),
        "funding_count": len(funding_data),
        "first_doc_keys": list(first_doc.keys()) if civic_docs else []
    }))
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    print('__RESULT__:')
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}, 'var_functions.execute_python:12': {'type': "<class 'str'>", 'is_str': True}}

exec(code, env_args)

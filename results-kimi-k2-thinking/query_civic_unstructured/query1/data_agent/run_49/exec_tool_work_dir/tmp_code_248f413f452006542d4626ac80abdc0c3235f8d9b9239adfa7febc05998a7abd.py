code = """import json
import os

# Get the storage key
civic_key = 'var_functions.query_db:2'
civic_result = locals().get(civic_key, None)

print(f"Type of civic_result: {type(civic_result)}")
print(f"Content preview: {str(civic_result)[:200]}")

print('__RESULT__:')
print(json.dumps({
    "type": str(type(civic_result)),
    "is_str": isinstance(civic_result, str)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_found': 276, 'sample_projects': ['project_227', 'project_131', 'project_95', 'project_35', 'project_46', 'project_138', 'project_123', 'project_282', 'project_488', 'project_486']}, 'var_functions.execute_python:8': {'funding_count': 38, 'civic_docs_count': 38}}

exec(code, env_args)

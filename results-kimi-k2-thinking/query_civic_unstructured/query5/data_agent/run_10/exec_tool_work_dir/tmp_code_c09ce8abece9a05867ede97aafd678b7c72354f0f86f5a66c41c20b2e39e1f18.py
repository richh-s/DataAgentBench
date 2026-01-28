code = """# Check what's in the storage
civic_docs_data = var_functions.query_db:2
print(f"__RESULT__:")
print(type(civic_docs_data))
if isinstance(civic_docs_data, str):
    print(json.dumps({"type": "string", "preview": civic_docs_data[:200]}))
else:
    print(json.dumps({"type": type(civic_docs_data).__name__, "preview": str(civic_docs_data)[:200]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 0, 'file_exists': False, 'error': 'File not found: /tmp/tmphn4t1u8a.json'}}

exec(code, env_args)

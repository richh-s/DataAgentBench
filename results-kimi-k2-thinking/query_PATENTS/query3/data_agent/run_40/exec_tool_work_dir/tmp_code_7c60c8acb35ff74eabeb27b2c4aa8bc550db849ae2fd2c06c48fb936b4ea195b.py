code = """# Check what's available in locals()
print("Keys in locals():")
for key in list(locals().keys())[:20]:
    print(f"  {key}")

print("\nTrying to access var_functions.query_db:2")
if 'var_functions.query_db:2' in locals():
    result = locals()['var_functions.query_db:2']
    print(f"Type: {type(result)}")
    print(f"Value preview: {result[:100] if isinstance(result, str) else str(result)[:100]}")
else:
    print("var_functions.query_db:2 not found in locals()")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

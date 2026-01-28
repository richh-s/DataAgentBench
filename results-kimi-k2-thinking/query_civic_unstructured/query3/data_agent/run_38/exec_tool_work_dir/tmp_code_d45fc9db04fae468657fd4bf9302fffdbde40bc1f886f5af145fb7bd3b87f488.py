code = """# Check the content and type of the stored variable
var_content = locals().get('var_functions.query_db:2')
print(f"Type: {type(var_content)}")
print(f"Content: {var_content[:200] if isinstance(var_content, str) else str(var_content)[:200]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

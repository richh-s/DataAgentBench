code = """# Let's check what's available in locals() first
keys = list(locals().keys())
print("Available local variables:", keys[:10])  # Just show first 10 to avoid clutter

# Try to find variables related to query_db
query_db_vars = [k for k in keys if '_query_' in k or 'query_db' in k]
print("\nVariables related to query_db:", query_db_vars)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

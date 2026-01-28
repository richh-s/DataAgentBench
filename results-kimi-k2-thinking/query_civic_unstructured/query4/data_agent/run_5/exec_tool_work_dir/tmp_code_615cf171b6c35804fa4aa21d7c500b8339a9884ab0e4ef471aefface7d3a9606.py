code = """import json

# Get the file paths
civic_docs_path = str(var_functions.query_db:4)
funding_path = str(var_functions.query_db:5)

print("Civic docs path:", civic_docs_path[:100])
print("Funding path:", funding_path[:100])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

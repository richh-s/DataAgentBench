code = """import json

# Access the file paths from the stored results
citations_file_path = var_functions.query_db:24
papers_file_path = var_functions.query_db:14

print('Citations file path:', citations_file_path)
print('Papers file path:', papers_file_path)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)

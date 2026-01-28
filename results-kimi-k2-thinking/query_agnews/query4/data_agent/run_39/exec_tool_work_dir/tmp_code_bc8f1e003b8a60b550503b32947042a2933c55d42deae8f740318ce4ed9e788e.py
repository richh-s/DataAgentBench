code = """import json

# Access the file paths from storage
metadata_result = var_functions.query_db:2  # Contains file path
articles_result = var_functions.query_db:20  # Contains file path

# Read the files
with open(metadata_result, 'r') as f:
    metadata_list = json.load(f)

with open(articles_result, 'r') as f:
    articles_list = json.load(f)

# Check the data
print('__RESULT__:')
print(json.dumps({
    'metadata_count': len(metadata_list),
    'articles_count': len(articles_list),
    'metadata_keys': list(metadata_list[0].keys()) if metadata_list else [],
    'articles_keys': list(articles_list[0].keys()) if articles_list else []
}))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'available_files': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)

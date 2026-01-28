code = """import json

metadata_file = var_functions.query_db:2

with open(metadata_file, 'r') as f:
    all_2015_metadata = json.load(f)

article_ids_2015 = [item['article_id'] for item in all_2015_metadata]

print('__RESULT__:')
print(str(len(article_ids_2015)))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

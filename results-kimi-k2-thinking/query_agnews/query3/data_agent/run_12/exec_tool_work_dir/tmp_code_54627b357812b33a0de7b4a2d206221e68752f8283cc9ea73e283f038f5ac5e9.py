code = """import json

# Load Europe article metadata from file
path = locals()['var_functions.query_db:2']
full_path = path.strip('"')
with open(full_path, 'r') as f:
    articles_meta = json.load(f)
# Extract article_ids list
article_ids = [int(item["article_id"]) for item in articles_meta]
year_map = {int(item["article_id"]): int(item["publication_date"].split('-')[0]) for item in articles_meta}
print('__RESULT__:')
print(json.dumps({"article_ids_count": len(article_ids), "sample_ids": article_ids[:5]}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 14860}}

exec(code, env_args)

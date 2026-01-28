code = """import json

# Load all 2015 metadata
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Extract all article_ids
article_ids_2015 = [int(rec['article_id']) for rec in metadata_2015]

print('__RESULT__:')
print(json.dumps({
    'total_articles_2015': len(article_ids_2015),
    'article_id_range': f"{min(article_ids_2015)} to {max(article_ids_2015)}",
    'sample_ids': article_ids_2015[:10]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'count': 6696, 'sample': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}]}}

exec(code, env_args)

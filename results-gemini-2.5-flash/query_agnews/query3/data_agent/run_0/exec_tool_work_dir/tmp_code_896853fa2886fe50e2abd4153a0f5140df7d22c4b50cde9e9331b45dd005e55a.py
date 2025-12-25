code = """import json

with open(locals()['var_function-call-5078530969761988450'], 'r') as f:
    europe_articles_metadata = json.load(f)

article_ids = [article['article_id'] for article in europe_articles_metadata]
article_ids_int = [int(article_id) for article_id in article_ids] # Convert to int for MongoDB query

print("__RESULT__:")
print(json.dumps(article_ids_int))"""

env_args = {'var_function-call-5078530969761988450': 'file_storage/function-call-5078530969761988450.json'}

exec(code, env_args)

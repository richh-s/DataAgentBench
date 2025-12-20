code = """import json

with open(locals()['var_function-call-16393350103042382032'], 'r') as f:
    europe_articles_data = json.load(f)

article_ids = [article['article_id'] for article in europe_articles_data]

print('__RESULT__:')
print(json.dumps(article_ids))"""

env_args = {'var_function-call-16393350103042382032': 'file_storage/function-call-16393350103042382032.json'}

exec(code, env_args)

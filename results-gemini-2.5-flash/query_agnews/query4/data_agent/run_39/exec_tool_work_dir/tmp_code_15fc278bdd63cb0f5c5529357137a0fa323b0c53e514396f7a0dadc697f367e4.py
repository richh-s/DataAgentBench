code = """import json
world_articles = locals()['var_function-call-10818552914458239740']['query_db_response']['results']
world_article_ids = [int(article['article_id']) for article in json.loads(world_articles[0])]
print('__RESULT__:')
print(json.dumps(world_article_ids))"""

env_args = {'var_function-call-10818552914458239740': [{'_id': '6943fcd582148821271cd40a', 'article_id': '4'}, {'_id': '6943fcd582148821271cd439', 'article_id': '51'}, {'_id': '6943fcd582148821271cd440', 'article_id': '58'}, {'_id': '6943fcd582148821271cd45d', 'article_id': '87'}, {'_id': '6943fcd582148821271cd46a', 'article_id': '100'}]}

exec(code, env_args)

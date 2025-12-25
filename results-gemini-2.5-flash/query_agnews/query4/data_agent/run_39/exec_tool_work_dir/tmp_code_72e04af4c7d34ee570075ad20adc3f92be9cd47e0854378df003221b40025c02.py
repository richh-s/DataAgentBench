code = """import json
world_articles_raw_str = locals()['var_function-call-10818552914458239740']['query_db_response']['results'][0]
json_start = world_articles_raw_str.find('[')
json_end = world_articles_raw_str.rfind(']') + 1
world_articles_json_str = world_articles_raw_str[json_start:json_end]
world_articles_list = json.loads(world_articles_json_str)
world_article_ids = [int(article['article_id']) for article in world_articles_list]
print('__RESULT__:')
print(json.dumps(world_article_ids))"""

env_args = {'var_function-call-10818552914458239740': [{'_id': '6943fcd582148821271cd40a', 'article_id': '4'}, {'_id': '6943fcd582148821271cd439', 'article_id': '51'}, {'_id': '6943fcd582148821271cd440', 'article_id': '58'}, {'_id': '6943fcd582148821271cd45d', 'article_id': '87'}, {'_id': '6943fcd582148821271cd46a', 'article_id': '100'}]}

exec(code, env_args)

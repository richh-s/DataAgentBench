code = """import json

raw_results_list = locals()['var_function-call-10818552914458239740']['query_db_response']['results']
# The actual JSON string is the first (and likely only) element of the list
json_string = raw_results_list[0]

# The string itself contains a JSON array, so parse it directly
articles_data = json.loads(json_string)

# Extract article_ids and convert them to integers
world_article_ids = [int(article['article_id']) for article in articles_data]

print('__RESULT__:')
print(json.dumps(world_article_ids))"""

env_args = {'var_function-call-10818552914458239740': [{'_id': '6943fcd582148821271cd40a', 'article_id': '4'}, {'_id': '6943fcd582148821271cd439', 'article_id': '51'}, {'_id': '6943fcd582148821271cd440', 'article_id': '58'}, {'_id': '6943fcd582148821271cd45d', 'article_id': '87'}, {'_id': '6943fcd582148821271cd46a', 'article_id': '100'}]}

exec(code, env_args)

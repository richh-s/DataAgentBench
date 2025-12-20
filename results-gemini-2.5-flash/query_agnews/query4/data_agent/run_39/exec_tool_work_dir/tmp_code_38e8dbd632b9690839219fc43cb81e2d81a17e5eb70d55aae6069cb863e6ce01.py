code = """import json
import re

raw_output_list = locals()['var_function-call-10818552914458239740']['query_db_response']['results']
raw_output_str = raw_output_list[0]

# Extract the JSON array string using regex
json_match = re.search(r'\[.*\]', raw_output_str, re.DOTALL)

world_article_ids = []
if json_match:
    json_str = json_match.group(0)
    articles_data = json.loads(json_str)
    world_article_ids = [int(article['article_id']) for article in articles_data]

print('__RESULT__:')
print(json.dumps(world_article_ids))"""

env_args = {'var_function-call-10818552914458239740': [{'_id': '6943fcd582148821271cd40a', 'article_id': '4'}, {'_id': '6943fcd582148821271cd439', 'article_id': '51'}, {'_id': '6943fcd582148821271cd440', 'article_id': '58'}, {'_id': '6943fcd582148821271cd45d', 'article_id': '87'}, {'_id': '6943fcd582148821271cd46a', 'article_id': '100'}]}

exec(code, env_args)

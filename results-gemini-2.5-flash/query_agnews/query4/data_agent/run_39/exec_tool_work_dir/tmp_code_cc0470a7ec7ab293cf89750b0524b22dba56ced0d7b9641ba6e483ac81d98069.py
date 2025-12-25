code = """import json
import re

raw_output_list = locals()['var_function-call-10818552914458239740']['query_db_response']['results']
raw_output_str = raw_output_list[0]

# Use regex to find the JSON array string
json_array_match = re.search(r'\[.*\]', raw_output_str, re.DOTALL)

world_article_ids = []
if json_array_match:
    json_string_outer = json_array_match.group(0)
    # The JSON string itself might be a list of strings, where each inner string is a JSON object
    articles_data_outer = json.loads(json_string_outer)

    # Check if elements are strings and need further parsing
    for item in articles_data_outer:
        if isinstance(item, str):
            # If it's a string, parse it as a JSON object
            inner_article_data = json.loads(item)
            if 'article_id' in inner_article_data:
                world_article_ids.append(int(inner_article_data['article_id']))
        elif isinstance(item, dict):
            # If it's already a dictionary, directly extract article_id
            if 'article_id' in item:
                world_article_ids.append(int(item['article_id']))

print('__RESULT__:')
print(json.dumps(world_article_ids))"""

env_args = {'var_function-call-10818552914458239740': [{'_id': '6943fcd582148821271cd40a', 'article_id': '4'}, {'_id': '6943fcd582148821271cd439', 'article_id': '51'}, {'_id': '6943fcd582148821271cd440', 'article_id': '58'}, {'_id': '6943fcd582148821271cd45d', 'article_id': '87'}, {'_id': '6943fcd582148821271cd46a', 'article_id': '100'}]}

exec(code, env_args)

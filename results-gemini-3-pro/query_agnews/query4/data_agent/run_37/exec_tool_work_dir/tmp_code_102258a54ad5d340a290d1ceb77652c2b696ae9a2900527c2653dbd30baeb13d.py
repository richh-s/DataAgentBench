code = """import json

# Load metadata
with open(locals()['var_function-call-16212366058662656941'], 'r') as f:
    metadata = json.load(f)

# Extract IDs. The metadata has article_id as string "13", but we found Mongo needs int.
# So convert to int.
ids = [int(x['article_id']) for x in metadata]

print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_function-call-16212366058662656941': 'file_storage/function-call-16212366058662656941.json', 'var_function-call-6272869269169383248': {'count': 6696, 'sample': [{'article_id': '13', 'region': 'Europe'}, {'article_id': '18', 'region': 'South America'}, {'article_id': '26', 'region': 'Africa'}, {'article_id': '51', 'region': 'South America'}, {'article_id': '52', 'region': 'Africa'}]}, 'var_function-call-14390080759705444864': [{'_id': '6945189c84fbb3f1578d3ef7', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}]}

exec(code, env_args)

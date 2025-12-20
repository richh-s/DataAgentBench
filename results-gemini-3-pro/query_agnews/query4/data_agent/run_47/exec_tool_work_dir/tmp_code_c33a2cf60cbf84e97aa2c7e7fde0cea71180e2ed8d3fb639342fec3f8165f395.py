code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-1094897247215011109']

# Load the result from the file
with open(file_path, 'r') as f:
    metadata_list = json.load(f)

# Get first 50 IDs
ids = [int(x['article_id']) for x in metadata_list[:50]]

# Construct query
query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": ids}}
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-6982124256931612734': ['authors', 'article_metadata'], 'var_function-call-6982124256931612959': ['articles'], 'var_function-call-1094897247215011109': 'file_storage/function-call-1094897247215011109.json', 'var_function-call-1808453290574413428': 6696, 'var_function-call-9634656923083955930': [{'_id': '694525f5404bb9b431eed7be', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694525f5404bb9b431eed7bf', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694525f5404bb9b431eed7c0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694525f5404bb9b431eed7c1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694525f5404bb9b431eed7c2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

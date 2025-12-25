code = """import json

# Load data
with open(locals()['var_function-call-17062830549632021172'], 'r') as f:
    articles = json.load(f)

# Sort by description length descending
articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)

# Get top 20
top_20 = articles[:20]

print("__RESULT__:")
print(json.dumps(top_20))"""

env_args = {'var_function-call-2359217064653629904': ['articles'], 'var_function-call-2359217064653631391': ['authors', 'article_metadata'], 'var_function-call-12491833190208577722': [{'_id': '694464677c0ede8b60d25e3c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-9351886142223050984': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-7977853732793881019': [{'_id': '694464677c0ede8b60d25e3c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694464677c0ede8b60d25e3d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694464677c0ede8b60d25e3e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694464677c0ede8b60d25e3f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694464677c0ede8b60d25e40', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17062830549632021172': 'file_storage/function-call-17062830549632021172.json', 'var_function-call-18351005198250448470': []}

exec(code, env_args)

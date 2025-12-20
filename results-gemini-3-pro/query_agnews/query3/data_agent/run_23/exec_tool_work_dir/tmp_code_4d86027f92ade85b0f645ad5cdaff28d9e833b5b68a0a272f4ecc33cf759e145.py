code = """import json

with open(locals()['var_function-call-13314577976510498220'], 'r') as f:
    data = json.load(f)

ids = data['ids']
min_id = min(ids)
max_id = max(ids)
print(f"Min ID: {min_id}")
print(f"Max ID: {max_id}")
print(f"Count: {len(ids)}")
print("__RESULT__:")
print(json.dumps({"min": min_id, "max": max_id, "count": len(ids)}))"""

env_args = {'var_function-call-18349184007638640037': 'file_storage/function-call-18349184007638640037.json', 'var_function-call-13314577976510498220': 'file_storage/function-call-13314577976510498220.json', 'var_function-call-15338869438340783850': [{'_id': '6944d56f1edb9f0b9c16c37b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d56f1edb9f0b9c16c37c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d56f1edb9f0b9c16c37d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d56f1edb9f0b9c16c37e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d56f1edb9f0b9c16c37f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

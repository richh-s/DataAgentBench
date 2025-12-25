code = """import json

with open(locals()['var_function-call-14497851320051987811'], 'r') as f:
    data = json.load(f)

ids = data['ids']
min_id = min(ids)
max_id = max(ids)
count = len(ids)
density = count / (max_id - min_id + 1)

print("__RESULT__:")
print(json.dumps({"min": min_id, "max": max_id, "count": count, "density": density}))"""

env_args = {'var_function-call-8077609229720510149': 'file_storage/function-call-8077609229720510149.json', 'var_function-call-14497851320051987811': 'file_storage/function-call-14497851320051987811.json', 'var_function-call-7073607657613911997': [{'_id': '6944cfe86247ca1041bd75bf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cfe86247ca1041bd75c0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cfe86247ca1041bd75c1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cfe86247ca1041bd75c2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cfe86247ca1041bd75c3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

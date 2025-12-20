code = """import json

with open(locals()['var_function-call-4201108153070275495'], 'r') as f:
    ids = json.load(f)

batch_size = 1000
batch_idx = 0
batch_ids = ids[batch_idx * batch_size : (batch_idx + 1) * batch_size]

query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": batch_ids}}
}
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-2957715184060021427': 'file_storage/function-call-2957715184060021427.json', 'var_function-call-4201108153070275495': 'file_storage/function-call-4201108153070275495.json', 'var_function-call-16938870298457831810': 6696, 'var_function-call-17691665255302430554': [{'_id': '694502d833322aa7ce41a4f0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694502d833322aa7ce41a4f1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694502d833322aa7ce41a4f2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694502d833322aa7ce41a4f3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694502d833322aa7ce41a4f4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2738382894626083919': {'min': 13, 'max': 127570, 'count': 6696}}

exec(code, env_args)

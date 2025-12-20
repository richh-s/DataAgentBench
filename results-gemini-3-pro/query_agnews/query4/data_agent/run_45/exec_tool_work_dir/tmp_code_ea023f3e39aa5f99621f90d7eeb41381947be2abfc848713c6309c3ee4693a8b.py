code = """import json

file_path = locals()['var_function-call-8215058594514075225']
with open(file_path, 'r') as f:
    metadata = json.load(f)

ids = [int(x['article_id']) for x in metadata]
min_id = min(ids)
max_id = max(ids)

print(f"Min ID: {min_id}")
print(f"Max ID: {max_id}")
print(f"Total count: {len(ids)}")

query = {
    "collection": "articles",
    "filter": {"article_id": {"$gte": min_id, "$lte": max_id}},
    "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
}
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-8215058594514075225': 'file_storage/function-call-8215058594514075225.json', 'var_function-call-15796689833732629801': 'file_storage/function-call-15796689833732629801.json', 'var_function-call-412792057028406590': ['articles'], 'var_function-call-17773611342032374061': [{'_id': '69452455473cd748aceb2ef4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69452455473cd748aceb2ef5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69452455473cd748aceb2ef6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69452455473cd748aceb2ef7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69452455473cd748aceb2ef8', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

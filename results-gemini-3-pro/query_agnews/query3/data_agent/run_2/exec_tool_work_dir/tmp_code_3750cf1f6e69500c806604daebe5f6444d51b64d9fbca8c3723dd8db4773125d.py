code = """import json

file_path = locals()['var_function-call-18399428532014092056']
with open(file_path, 'r') as f:
    metadata_records = json.load(f)

ids = [int(r['article_id']) for r in metadata_records]
min_id = min(ids)
max_id = max(ids)
count = len(ids)
unique_count = len(set(ids))

print("__RESULT__:")
print(json.dumps({"min": min_id, "max": max_id, "count": count, "unique": unique_count}))"""

env_args = {'var_function-call-12102129638019306028': ['authors', 'article_metadata'], 'var_function-call-12102129638019306837': ['articles'], 'var_function-call-18399428532014092056': 'file_storage/function-call-18399428532014092056.json', 'var_function-call-3700738106977438282': 14860, 'var_function-call-80233190844241043': [{'_id': '6944c1d66aebb4a355b6ecab', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c1d66aebb4a355b6ecac', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c1d66aebb4a355b6ecad', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c1d66aebb4a355b6ecae', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c1d66aebb4a355b6ecaf', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

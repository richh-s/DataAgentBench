code = """import json

with open(locals()['var_function-call-1474084106243643964'], 'r') as f:
    data = json.load(f)

ids = sorted(list(set([int(row['article_id']) for row in data])))
# First half
batch1 = ids[:3500]

query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": batch1}
    }
}
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-1474084106243643964': 'file_storage/function-call-1474084106243643964.json', 'var_function-call-9489092853522118579': 'file_storage/function-call-9489092853522118579.json', 'var_function-call-17105952885415197022': [{'_id': '6944ed7c4e8b2b9e56808f77', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ed7c4e8b2b9e56808f78', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ed7c4e8b2b9e56808f79', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ed7c4e8b2b9e56808f7a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ed7c4e8b2b9e56808f7b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17682266178667585365': 6696, 'var_function-call-6775491050414127677': 'file_storage/function-call-6775491050414127677.json', 'var_function-call-4705261762392207793': {'min': 13, 'max': 127570, 'count': 6696}}

exec(code, env_args)

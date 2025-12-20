code = """import json

# Read the SQL result file
file_path = locals()['var_function-call-12548450677556957208']
with open(file_path, 'r') as f:
    sql_data = json.load(f)

article_ids = [int(entry['article_id']) for entry in sql_data]
# Batch size
batch_size = 500
batches = [article_ids[i:i + batch_size] for i in range(0, len(article_ids), batch_size)]

queries = []
for batch in batches:
    q = {
        "collection": "articles",
        "filter": {"article_id": {"$in": batch}},
        "projection": {"article_id": 1, "title": 1, "description": 1, "_id": 0}
    }
    queries.append(q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-12548450677556957208': 'file_storage/function-call-12548450677556957208.json', 'var_function-call-8309167075674923618': 'file_storage/function-call-8309167075674923618.json', 'var_function-call-14321692727433634718': [{'_id': '69450677667263db4e71cc0e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450677667263db4e71cc0f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450677667263db4e71cc10', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450677667263db4e71cc11', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450677667263db4e71cc12', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

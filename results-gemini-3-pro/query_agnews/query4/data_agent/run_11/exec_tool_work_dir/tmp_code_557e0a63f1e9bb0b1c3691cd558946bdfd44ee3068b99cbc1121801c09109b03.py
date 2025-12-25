code = """import json

with open(locals()['var_function-call-2683070877417335365'], 'r') as f:
    sql_results = json.load(f)

ids = [int(row['article_id']) for row in sql_results]
print(f"Min ID: {min(ids)}")
print(f"Max ID: {max(ids)}")
print(f"Count: {len(ids)}")
print("__RESULT__:")
print(json.dumps({"min": min(ids), "max": max(ids), "count": len(ids)}))"""

env_args = {'var_function-call-2683070877417335365': 'file_storage/function-call-2683070877417335365.json', 'var_function-call-7837263819668175178': 6696, 'var_function-call-14907435017980586290': [{'_id': '6944f3d4dccdaaaa57646236', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f3d4dccdaaaa57646237', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f3d4dccdaaaa57646238', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f3d4dccdaaaa57646239', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f3d4dccdaaaa5764623a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

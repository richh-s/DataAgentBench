code = """import json

# Load metadata results
with open(locals()['var_function-call-13931165385016182989'], 'r') as f:
    sql_results = json.load(f)

ids = [int(r['article_id']) for r in sql_results]
print(f"Total Europe articles: {len(ids)}")
print(f"Min ID: {min(ids)}")
print(f"Max ID: {max(ids)}")
print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-13931165385016182989': 'file_storage/function-call-13931165385016182989.json', 'var_function-call-3866583078313724775': 'file_storage/function-call-3866583078313724775.json', 'var_function-call-4925085607958011088': [{'_id': '6944cc47e14c7aa41c39dfa0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cc47e14c7aa41c39dfa1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cc47e14c7aa41c39dfa2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cc47e14c7aa41c39dfa3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cc47e14c7aa41c39dfa4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

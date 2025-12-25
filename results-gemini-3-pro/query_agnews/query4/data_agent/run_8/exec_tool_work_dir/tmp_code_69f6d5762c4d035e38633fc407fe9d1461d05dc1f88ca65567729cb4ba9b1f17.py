code = """import json

file_path = locals()['var_function-call-750385390280883322']
with open(file_path, 'r') as f:
    metadata = json.load(f)

# Filter for Africa
africa_ids = [int(x['article_id']) for x in metadata if x['region'] == 'Africa']

print("__RESULT__:")
print(json.dumps(africa_ids))"""

env_args = {'var_function-call-750385390280883322': 'file_storage/function-call-750385390280883322.json', 'var_function-call-6083932913443130219': 6696, 'var_function-call-14170722069696433452': 'file_storage/function-call-14170722069696433452.json', 'var_function-call-14254421073685728294': [{'_id': '6944f121311e1de8e6047551', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f121311e1de8e6047552', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f121311e1de8e6047553', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f121311e1de8e6047554', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f121311e1de8e6047555', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6366566729007167229': [{'region': 'Africa', 'count': '1345'}, {'region': 'Asia', 'count': '1333'}, {'region': 'Europe', 'count': '1357'}, {'region': 'North America', 'count': '1329'}, {'region': 'South America', 'count': '1332'}]}

exec(code, env_args)

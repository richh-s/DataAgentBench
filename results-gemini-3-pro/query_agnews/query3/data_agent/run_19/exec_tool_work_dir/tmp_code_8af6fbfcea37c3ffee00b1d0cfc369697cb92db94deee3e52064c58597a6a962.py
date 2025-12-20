code = """import json

# Load full ID list
file_path = locals()['var_function-call-15332399369623468447']
with open(file_path, 'r') as f:
    data = json.load(f)

ids = data['ids']
batch_size = 4000
batch_index = 0

start = batch_index * batch_size
end = start + batch_size
batch_ids = ids[start:end]

print("__RESULT__:")
print(json.dumps(batch_ids))"""

env_args = {'var_function-call-3309949836529129021': 'file_storage/function-call-3309949836529129021.json', 'var_function-call-15332399369623468447': 'file_storage/function-call-15332399369623468447.json', 'var_function-call-4327695410428056510': [{'_id': '6944d2f520a43c7643e366da', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d2f520a43c7643e366db', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d2f520a43c7643e366dc', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d2f520a43c7643e366dd', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d2f520a43c7643e366de', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13272302297528658977': {'max_id': 127583, 'count': 14860}}

exec(code, env_args)

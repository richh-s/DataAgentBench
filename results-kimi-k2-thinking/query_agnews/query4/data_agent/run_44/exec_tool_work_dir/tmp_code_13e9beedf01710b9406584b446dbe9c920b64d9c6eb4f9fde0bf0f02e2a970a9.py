code = """import json

# Read the full metadata result from the file
metadata_file_path = locals()['var_functions.query_db:1']
with open(metadata_file_path, 'r') as f:
    article_metadata = json.load(f)

# Get articles data
articles = locals()['var_functions.query_db:0']

print('__RESULT__:')
print(json.dumps({
    'metadata_count': len(article_metadata),
    'articles_count': len(articles),
    'sample_metadata': article_metadata[:3],
    'sample_articles': articles[:3]
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969f2761eb70684784ced10', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f2761eb70684784ced11', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f2761eb70684784ced12', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f2761eb70684784ced13', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f2761eb70684784ced14', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)

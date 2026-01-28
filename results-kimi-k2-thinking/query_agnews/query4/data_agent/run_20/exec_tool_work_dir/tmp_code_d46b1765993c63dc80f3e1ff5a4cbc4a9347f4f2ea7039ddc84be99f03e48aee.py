code = """import json

# Load both data files
metadata_path = var_functions.query_db:2
articles_path = var_functions.query_db:20

print('Loading metadata from:', metadata_path)
with open(metadata_path, 'r') as f:
    metadata_2015 = json.load(f)

print('Loading articles from:', articles_path)
with open(articles_path, 'r') as f:
    articles_all = json.load(f)

print('Loaded 2015 metadata:', len(metadata_2015), 'records')
print('Loaded all articles:', len(articles_all), 'records')

# Look at data structure
print('\nFirst 3 metadata records:')
for i, rec in enumerate(metadata_2015[:3]):
    print(f"  {i}: article_id={rec.get('article_id')}, region={rec.get('region')}, year={rec.get('publication_date')[:4] if rec.get('publication_date') else 'N/A'}")
    
print('\nFirst 3 articles:')
for i, rec in enumerate(articles_all[:3]):
    print(f"  {i}: article_id={rec.get('article_id')}, title={rec.get('title')[:80]}...")

result = {
    'metadata_count': len(metadata_2015),
    'articles_count': len(articles_all),
    'sample_metadata': metadata_2015[:3],
    'sample_articles': articles_all[:3]
}
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'metadata_count': 6696, 'articles_count': 5}, 'var_functions.query_db:16': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)

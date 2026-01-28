code = """import json

# Read 2015 metadata
metadata_file = locals()['var_functions.query_db:0']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Create a dictionary mapping article_id to region for 2015 articles
article_to_region_2015 = {item['article_id']: item['region'] for item in metadata_2015}

# Read all articles
articles_file = locals()['var_functions.query_db:11']
with open(articles_file, 'r') as f:
    all_articles = json.load(f)

print('__RESULT__:')
print(f'Total articles in database: {len(all_articles)}')
print(f'2015 article IDs available: {len(article_to_region_2015)}')
print('Sample 2015 article ID-region mapping:')
for k, v in list(article_to_region_2015.items())[:5]:
    print(f"  {k}: {v}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': {'total_2015_articles': 6696, 'sample_article_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_functions.query_db:11': [{'_id': '6969f0535d40b3c75eb9c614', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f0535d40b3c75eb9c615', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f0535d40b3c75eb9c616', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f0535d40b3c75eb9c617', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f0535d40b3c75eb9c618', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

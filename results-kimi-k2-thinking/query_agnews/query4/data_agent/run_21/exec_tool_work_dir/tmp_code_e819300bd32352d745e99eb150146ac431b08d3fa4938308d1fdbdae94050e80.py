code = """import json

# The metadata is stored as a file path string
metadata_file_path = locals()['var_functions.query_db:4']
articles_data = locals()['var_functions.query_db:6']

# Load metadata from file
with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Articles data is already a list
articles = articles_data

# Create lookup dictionaries
articles_dict = {int(article['article_id']): article for article in articles}

# Create 2015 articles list
articles_2015 = []
for meta in metadata_2015:
    article_id = int(meta['article_id'])
    if article_id in articles_dict:
        article_info = {
            'article_id': article_id,
            'region': meta['region'],
            'title': articles_dict[article_id]['title'],
            'description': articles_dict[article_id]['description']
        }
        articles_2015.append(article_info)

# Count total and show sample
print('__RESULT__:')
print(json.dumps({
    'total_2015_articles': len(articles_2015),
    'sample_articles': articles_2015[:3]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [{'_id': '6969e10e4c4e890ccbefaf21', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e10e4c4e890ccbefaf22', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e10e4c4e890ccbefaf23', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e10e4c4e890ccbefaf24', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e10e4c4e890ccbefaf25', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'metadata_type': "<class 'str'>", 'articles_type': "<class 'list'>", 'metadata_preview': 'file_storage/functions.query_db:4.json', 'articles_preview': 'not string'}}

exec(code, env_args)

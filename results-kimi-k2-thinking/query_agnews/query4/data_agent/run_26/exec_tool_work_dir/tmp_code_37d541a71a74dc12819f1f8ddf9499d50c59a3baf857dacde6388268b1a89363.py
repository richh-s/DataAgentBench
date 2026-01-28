code = """import json

# Get the 2015 metadata (this is a file path)
metadata_file = locals()['var_functions.query_db:4']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Get all articles from MongoDB (this is direct data, not a file path)
all_articles = locals()['var_functions.query_db:24']

print('Metadata count:', len(metadata_2015))
print('All articles count:', len(all_articles))
print('First article:', all_articles[0])

# Build region map
region_map = {}
for item in metadata_2015:
    region_map[int(item['article_id'])] = item['region']

# Filter to 2015 articles and add region
articles_2015 = []
for article in all_articles:
    article_id = int(article['article_id'])
    if article_id in region_map:
        article_copy = dict(article)
        article_copy['region'] = region_map[article_id]
        article_copy['article_id'] = article_id
        articles_2015.append(article_copy)

print('Total 2015 articles:', len(articles_2015))
print('First 2015 article:', articles_2015[0] if articles_2015 else 'None')

# Save for next step
print('__RESULT__:')
print(json.dumps(articles_2015[:100]))  # Return first 100 as preview"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'author_id': '387', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'author_id': '684', 'region': 'Africa', 'publication_date': '2015-06-02'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:10': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': {'region_map_size': 6696, 'metadata_count': 6696, 'first_article_id': '13', 'first_region': 'Europe'}, 'var_functions.query_db:24': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json
import os

# Read full articles data
articles_path = var_functions.query_db:12
if isinstance(articles_path, str) and articles_path.endswith('.json'):
    with open(articles_path, 'r') as f:
        all_articles = json.load(f)
else:
    all_articles = articles_path

# Read Europe metadata
metadata_path = var_functions.query_db:2
if isinstance(metadata_path, str) and metadata_path.endswith('.json'):
    with open(metadata_path, 'r') as f:
        europe_metadata = json.load(f)
else:
    europe_metadata = metadata_path

# Convert article_id to int for matching
for article in all_articles:
    article['article_id'] = int(article['article_id'])

for meta in europe_metadata:
    meta['article_id'] = int(meta['article_id'])

print('__RESULT__:')
print(json.dumps({
    "total_articles": len(all_articles),
    "europe_articles": len(europe_metadata),
    "sample_article": all_articles[0],
    "sample_metadata": europe_metadata[0]
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969c6f7e874579a946f4fbb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c6f7e874579a946f4fbc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c6f7e874579a946f4fbd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c6f7e874579a946f4fbe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c6f7e874579a946f4fbf', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'_id': '6969c6f7e874579a946f4fbb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c6f7e874579a946f4fbc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c6f7e874579a946f4fbd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c6f7e874579a946f4fbe', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c6f7e874579a946f4fbf', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': {'num_articles': 5, 'num_metadata': 14860, 'sample_articles': [{'_id': '6969c6f7e874579a946f4fbb', 'article_id': 0, 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c6f7e874579a946f4fbc', 'article_id': 1, 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}], 'sample_metadata': [{'article_id': 3, 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': 9, 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

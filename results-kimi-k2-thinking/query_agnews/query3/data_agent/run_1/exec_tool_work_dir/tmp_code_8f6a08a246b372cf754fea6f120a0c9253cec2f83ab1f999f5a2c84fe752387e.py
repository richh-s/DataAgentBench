code = """import json
import os

# Access the Europe metadata results
metadata_key = 'var_functions.query_db:8'
metadata_result = locals().get(metadata_key)

# Handle file path or direct result
if isinstance(metadata_result, str) and metadata_result.endswith('.json'):
    with open(metadata_result, 'r') as f:
        europe_metadata = json.load(f)
else:
    europe_metadata = metadata_result

# Access the articles data
articles_key = 'var_functions.query_db:2'
articles_data = locals().get(articles_key)

print(f"Total Europe articles 2010-2020: {len(europe_metadata)}")
print(f"Sample article IDs: {[item['article_id'] for item in europe_metadata[:5]]}")

# Extract unique article IDs from metadata for matching
metadata_article_ids = {item['article_id'] for item in europe_metadata}
print(f"Unique article IDs count: {len(metadata_article_ids)}")

# Show available article data
print(f"Total articles in sample data: {len(articles_data)}")
print(f"Sample article data IDs: {[article['article_id'] for article in articles_data[:5]]}")"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969a9e8d3fee090036ad705', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969a9e8d3fee090036ad706', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969a9e8d3fee090036ad707', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969a9e8d3fee090036ad708', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969a9e8d3fee090036ad709', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'count': '127600'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

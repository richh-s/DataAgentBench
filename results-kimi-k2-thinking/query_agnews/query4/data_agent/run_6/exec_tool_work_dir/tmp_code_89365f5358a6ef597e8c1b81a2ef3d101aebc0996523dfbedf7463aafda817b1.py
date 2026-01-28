code = """import json, os
metadata_file = locals()['var_functions.query_db:0']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Extract unique article IDs as strings
article_ids_2015 = list(set(row['article_id'] for row in metadata_2015))

# Create region mapping for 2015 articles
region_map = {}
for row in metadata_2015:
    region_map[row['article_id']] = row['region']

result_data = {
    'total_2015_articles': len(metadata_2015),
    'unique_article_count': len(article_ids_2015),
    'sample_ids': article_ids_2015[:10],
    'region_sample': {k: region_map[k] for k in list(region_map.keys())[:5]}
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'count': 6696, 'message': 'Found 6696 articles from 2015'}, 'var_functions.query_db:10': [{'_id': '6969d4ae855c9d59985346e5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d4ae855c9d59985346e6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d4ae855c9d59985346e7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d4ae855c9d59985346e8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d4ae855c9d59985346e9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'total_articles_2015': 6696, 'articles_with_content': 0}, 'var_functions.execute_python:16': {'metadata_sample_ids': ['13', '18', '26', '51', '52'], 'articles_sample_ids': ['0', '1', '2', '3', '4']}, 'var_functions.execute_python:18': {'total_ids': 6696}}

exec(code, env_args)

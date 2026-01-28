code = """import json

# Load 50,000 articles
articles_file = locals()['var_functions.query_db:44']
with open(articles_file, 'r') as f:
    articles_data = json.load(f)

# Load 2015 metadata
metadata_file = locals()['var_functions.query_db:19']
with open(metadata_file, 'r') as f:
    metadata = json.load(f)

# Check which article_ids we actually have
available_article_ids = set(str(a['article_id']) for a in articles_data)

# Filter metadata to only articles we have
filtered_metadata = []
for m in metadata:
    if str(m['article_id']) in available_article_ids:
        filtered_metadata.append(m)

print('__RESULT__:')
print(json.dumps({
    'total_2015_metadata': len(metadata),
    'available_articles_count': len(available_article_ids),
    'filtered_2015_count': len(filtered_metadata),
    'available_range': {
        'min': min(int(a) for a in available_article_ids),
        'max': max(int(a) for a in available_article_ids)
    }
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:19': {'metadata_type': "<class 'str'>", 'articles_type': "<class 'list'>"}, 'var_functions.execute_python:12': {'world_articles_count': 1, 'region_counts': {}, 'top_region': None}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_2015_articles': 3, 'world_articles_count': 0, 'region_world_counts': {}, 'top_region': None, 'top_region_count': 0}, 'var_functions.query_db:18': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.execute_python:24': {'total_2015_articles': 0, 'world_articles_total': 0, 'world_articles_by_region': {}, 'top_region': None, 'top_region_count': 0}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'metadata_2015_count': 6696, 'all_articles_count': 1000, 'sample_article': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'sample_metadata': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}]}, 'var_functions.execute_python:30': {'metadata_count': 6696, 'sample_ids': ['13', '18', '26', '51', '52']}, 'var_functions.execute_python:32': {'article_ids_sample': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97'], 'total_ids': 100}, 'var_functions.query_db:34': [], 'var_functions.execute_python:36': {'min_id': 13, 'max_id': 127570, 'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [], 'var_functions.execute_python:42': {'min_id': 0, 'max_id': 999, 'sample_ids': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)

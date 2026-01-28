code = """import json, os
# Load metadata 2015
metadata_file = locals()['var_functions.query_db:0']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)
# Build region map: article_id (str) -> region
region_map = {row['article_id']: row['region'] for row in metadata_2015}
article_ids_2015 = set(region_map.keys())

# Load articles list directly (it's a list)
articles = locals()['var_functions.query_db:26']

# Filter articles from 2015
filtered = []
for a in articles:
    a_id = a.get('article_id')
    if a_id is None:
        continue
    if str(a_id) in article_ids_2015:
        # add region info to article
        a['region'] = region_map[str(a_id)]
        filtered.append(a)

# Show how many 2015 articles we have filtered
result = {'filtered_count': len(filtered)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'count': 6696, 'message': 'Found 6696 articles from 2015'}, 'var_functions.query_db:10': [{'_id': '6969d4ae855c9d59985346e5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d4ae855c9d59985346e6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d4ae855c9d59985346e7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d4ae855c9d59985346e8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d4ae855c9d59985346e9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'total_articles_2015': 6696, 'articles_with_content': 0}, 'var_functions.execute_python:16': {'metadata_sample_ids': ['13', '18', '26', '51', '52'], 'articles_sample_ids': ['0', '1', '2', '3', '4']}, 'var_functions.execute_python:18': {'total_ids': 6696}, 'var_functions.execute_python:20': {'total_2015_articles': 6696, 'unique_article_count': 6696, 'sample_ids': ['55936', '54113', '28308', '58511', '74988', '5031', '59364', '14780', '89973', '48077'], 'region_sample': {'13': 'Europe', '18': 'South America', '26': 'Africa', '51': 'South America', '52': 'Africa'}}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'_id': '6969d4ae855c9d59985346f2', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_functions.query_db:26': [{'_id': '6969d4ae855c9d59985346e5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d4ae855c9d59985346e6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d4ae855c9d59985346e7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d4ae855c9d59985346e8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d4ae855c9d59985346e9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:30': {'metadata_type': "<class 'str'>", 'metadata_is_str': True, 'articles_type': "<class 'list'>", 'articles_is_str': False, 'articles_is_list': True}}

exec(code, env_args)

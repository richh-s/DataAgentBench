code = """import json
import pandas as pd
import re

# Load all data
metadata_path = locals()['var_functions.query_db:10']
articles_path = locals()['var_functions.query_db:40']

with open(metadata_path, 'r') as f:
    metadata_2015 = json.load(f)

with open(articles_path, 'r') as f:
    all_articles = json.load(f)

print('Loaded:', len(metadata_2015), '2015 metadata,', len(all_articles), 'articles')

# Process categorization efficiently
def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Simple keyword matching for World category
    world_keywords = ['war', 'conflict', 'iraq', 'iran', 'afghanistan', 'israel', 'palestine', 
                     'china', 'japan', 'africa', 'europe', 'asia', 'america', 'international', 
                     'global', 'world', 'united nations', 'diplomatic', 'foreign', 'crisis', 
                     'refugee', 'terrorist', 'military', 'nation', 'country', 'embassy']
    
    # Check if it's world news
    for kw in world_keywords:
        if kw in text:
            return 'World'
    return 'Other'

# Get 2015 article IDs
article_ids_2015 = set(doc['article_id'] for doc in metadata_2015)
region_lookup = {doc['article_id']: doc['region'] for doc in metadata_2015}

# Process articles
world_articles_by_region = {}
processed = 0

for article in all_articles:
    article_id = str(article['article_id'])
    if article_id in article_ids_2015:
        region = region_lookup.get(article_id)
        category = categorize_article(article['title'], article.get('description', ''))
        
        if category == 'World':
            world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1
        
        processed += 1

print('Processed', processed, '2015 articles')
print('World articles by region:', world_articles_by_region)

result = {
    'processed': processed,
    'world_counts': world_articles_by_region
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'author_id': '387', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'author_id': '684', 'region': 'Africa', 'publication_date': '2015-06-02'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'_id': '6969dd5b60aed15af3bfcdc3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969dd5b60aed15af3bfcdc4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969dd5b60aed15af3bfcdc5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969dd5b60aed15af3bfcdc6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969dd5b60aed15af3bfcdc7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'count': 6696, 'sample': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}]}, 'var_functions.execute_python:18': {'total': 6696, 'sample': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97', '116', '117', '141', '165', '179', '203', '240', '243', '266', '271', '309', '314', '364', '365', '369', '379', '408', '429', '488', '498', '501', '509', '519', '534', '606', '652', '698', '743', '745', '879', '885', '902', '907', '924', '932', '935', '941', '970', '987', '993', '1001', '1045', '1053', '1061', '1065', '1077', '1084', '1108', '1137', '1171', '1190', '1242', '1244', '1277', '1332', '1363', '1366', '1386', '1435', '1470', '1477', '1494', '1531', '1548', '1570', '1589', '1611', '1631', '1662', '1678', '1689', '1720', '1727', '1736', '1769', '1791', '1792', '1848', '1853', '1866', '1880', '1905', '1910', '1969', '1978', '1996', '2009', '2010', '2017', '2023']}, 'var_functions.query_db:20': [{'_id': '6969dd5b60aed15af3bfcdc3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969dd5b60aed15af3bfcdc4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969dd5b60aed15af3bfcdc5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969dd5b60aed15af3bfcdc6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969dd5b60aed15af3bfcdc7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:22': [{'_id': '6969dd5b60aed15af3bfcdc3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969dd5b60aed15af3bfcdc4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969dd5b60aed15af3bfcdc5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969dd5b60aed15af3bfcdc6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969dd5b60aed15af3bfcdc7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:24': {'total_articles': 6696, 'regions': ['Europe', 'South America', 'Africa', 'Asia', 'North America'], 'region_counts': {'Europe': 1357, 'Africa': 1345, 'Asia': 1333, 'South America': 1332, 'North America': 1329}}, 'var_functions.query_db:26': [{'_id': '6969dd5b60aed15af3bfcdc3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969dd5b60aed15af3bfcdc4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969dd5b60aed15af3bfcdc5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969dd5b60aed15af3bfcdc6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969dd5b60aed15af3bfcdc7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:30': {'total_2015_articles': 6696, 'sample_article_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97', '116', '117', '141', '165', '179', '203', '240', '243', '266', '271', '309', '314', '364', '365', '369', '379', '408', '429', '488', '498', '501', '509', '519', '534', '606', '652', '698', '743', '745', '879', '885', '902', '907', '924', '932', '935', '941', '970', '987', '993', '1001', '1045', '1053', '1061', '1065', '1077', '1084', '1108', '1137', '1171', '1190', '1242', '1244', '1277', '1332', '1363', '1366', '1386', '1435', '1470', '1477', '1494', '1531', '1548', '1570', '1589', '1611', '1631', '1662', '1678', '1689', '1720', '1727', '1736', '1769', '1791', '1792', '1848', '1853', '1866', '1880', '1905', '1910', '1969', '1978', '1996', '2009', '2010', '2017', '2023']}, 'var_functions.query_db:32': [], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'total_2015': 6696, 'sample_articles': 100, 'sample_article_ids': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'metadata_count': 6696, 'articles_count': 10000, 'filtered_2015': 494, 'merged_count': 494}, 'var_functions.execute_python:44': {'total_matched': 494, 'sample_categories': {'World': 44, 'Uncategorized': 38, 'Business': 9, 'Science/Technology': 6, 'Sports': 3}, 'world_sample': 44}}

exec(code, env_args)

code = """import json
import os

# Load metadata for all 2015 articles
metadata_file = locals()['var_functions.query_db:6']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Create region mapping
region_map = {}
for record in metadata_2015:
    region_map[int(record['article_id'])] = record['region']

# Load the 2000 articles we queried
articles_2000_file = locals()['var_functions.query_db:46']
with open(articles_2000_file, 'r') as f:
    articles_2000 = json.load(f)

# Get only 2015 articles from this batch
articles_2015 = []
for article in articles_2000:
    article_id = int(article['article_id'])
    if article_id in region_map:
        articles_2015.append({
            'article_id': article_id,
            'region': region_map[article_id],
            'title': article['title'],
            'description': article['description']
        })

print(f'Found {len(articles_2015)} articles from 2015 in current batch')

# Category classification
world_keywords = ['war', 'peace', 'diplomat', 'treaty', 'united nations', 'un', 'security council', 'afghanistan', 'iraq', 'iran', 'israel', 'palestine', 'china', 'russia', 'ukraine', 'syria', 'global', 'international', 'foreign', 'embassy', 'ambassador', 'trade deficit', 'trade', 'military', 'defense', 'nuclear', 'weapon', 'terrorist', 'terrorism', 'world', 'foreign policy', 'diplomacy', 'united', 'nations']

def classify_article(title, description):
    text = f"{title} {description}".lower()
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    return 'Other'

# Count World articles by region
world_counts = {'North America': 0, 'Europe': 0, 'Asia': 0, 'South America': 0, 'Africa': 0}
world_articles_list = []

for article in articles_2015:
    category = classify_article(article['title'], article['description'])
    if category == 'World':
        region = article['region']
        world_counts[region] += 1
        world_articles_list.append({
            'article_id': article['article_id'],
            'region': region,
            'title': article['title']
        })

# Save results
with open('/tmp/world_articles_batch1.json', 'w') as f:
    json.dump(world_articles_list, f)

print('__RESULT__:')
print(json.dumps({
    'world_counts_batch': world_counts,
    'world_articles_found': len(world_articles_list),
    'total_processed': len(articles_2015)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e9310b470561e5db3037', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e9310b470561e5db3038', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e9310b470561e5db3039', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e9310b470561e5db303a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e9310b470561e5db303b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:4': ['authors', 'article_metadata'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'count': 6696, 'sample': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:14': [], 'var_functions.execute_python:16': {'total_count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'id_type': "<class 'int'>"}, 'var_functions.execute_python:22': {'query': '{"collection": "articles", "filter": {"article_id": {"$in": [13,18,26,51,52,67,70,74,86,97,116,117,141,165,179,203,240,243,266,271,309,314,364,365,369,379,408,429,488,498,501,509,519,534,606,652,698,743,745,879,885,902,907,924,932,935,941,970,987,993,1001,1045,1053,1061,1065,1077,1084,1108,1137,1171,1190,1242,1244,1277,1332,1363,1366,1386,1435,1470,1477,1494,1531,1548,1570,1589,1611,1631,1662,1678,1689,1720,1727,1736,1769,1791,1792,1848,1853,1866,1880,1905,1910,1969,1978,1996,2009,2010,2017,2023]}}, "limit": 100}'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_articles_2015': 6696, 'regions': {'Europe': 1357, 'Africa': 1345, 'Asia': 1333, 'South America': 1332, 'North America': 1329}}, 'var_functions.execute_python:30': {'total_batches': 14, 'batch_size': 500, 'total_articles': 6696, 'first_batch_sample': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:32': {'total_to_process': 6696, 'batches_created': 14, 'processed_count': 6696}, 'var_functions.execute_python:34': {'processed_in_first_batch': 100, 'world_articles_found': {'South America': 13, 'Asia': 16, 'Africa': 9, 'Europe': 16, 'North America': 8}, 'remaining_to_fetch': 6596, 'total_2015_articles': 6696}, 'var_functions.execute_python:36': {'total_batches': 14, 'batch_size': 500, 'total_articles': 6696, 'world_counts_initial': {'North America': 0, 'Europe': 0, 'Asia': 0, 'South America': 0, 'Africa': 0}}, 'var_functions.execute_python:38': {'total_batches': 14, 'articles_to_process': 6696}, 'var_functions.execute_python:40': {'total_articles': 6696, 'processed': 100, 'remaining': 6596}, 'var_functions.execute_python:42': {'world_counts_initial': {'North America': 8, 'Europe': 16, 'Asia': 16, 'South America': 13, 'Africa': 9}, 'processed_in_first_batch': 100, 'total_remaining': 6596, 'total_batches': 14}, 'var_functions.execute_python:44': {'world_counts_from_first_100': {'North America': 8, 'Europe': 16, 'Asia': 16, 'South America': 13, 'Africa': 9}, 'world_articles_found': 62, 'regions_covered': ['South America', 'North America', 'Asia', 'Africa', 'Europe']}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': {'total_2015_articles': 6696, 'found_in_current_batch': 96, 'sample_article_id': '13'}}

exec(code, env_args)

code = """import json
import pandas as pd

# Load all 2015 metadata
metadata_file = locals()['var_functions.query_db:6']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Create region mapping
region_map = {int(record['article_id']): record['region'] for record in metadata_2015}
all_article_ids = sorted(list(region_map.keys()))

print(f'Total 2015 articles: {len(all_article_ids)}')
print(f'ID range: {min(all_article_ids)} to {max(all_article_ids)}')

# Load all articles we've already fetched (2000 + 3000 = 5000 articles)
fetched_files = [
    locals()['var_functions.query_db:46'],  # First 2000
    locals()['var_functions.query_db:58']   # Next 3000
]

all_fetched_articles = []
for file_path in fetched_files:
    with open(file_path, 'r') as f:
        articles = json.load(f)
        all_fetched_articles.extend(articles)

print(f'Total fetched articles: {len(all_fetched_articles)}')

# Filter to only 2015 articles
articles_2015 = []
for article in all_fetched_articles:
    article_id = int(article['article_id'])
    if article_id in region_map:
        articles_2015.append({
            'article_id': article_id,
            'region': region_map[article_id],
            'title': article['title'],
            'description': article['description']
        })

print(f'2015 articles in fetched data: {len(articles_2015)}')

# Find missing IDs
fetched_ids = {article['article_id'] for article in articles_2015}
missing_ids = [aid for aid in all_article_ids if aid not in fetched_ids]
print(f'Missing articles: {len(missing_ids)}')

print('__RESULT__:')
print(json.dumps({
    'total_2015': len(all_article_ids),
    'fetched_2015': len(articles_2015),
    'missing': len(missing_ids),
    'missing_sample': missing_ids[:10] if missing_ids else []
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e9310b470561e5db3037', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e9310b470561e5db3038', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e9310b470561e5db3039', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e9310b470561e5db303a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e9310b470561e5db303b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:4': ['authors', 'article_metadata'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'count': 6696, 'sample': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:14': [], 'var_functions.execute_python:16': {'total_count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'id_type': "<class 'int'>"}, 'var_functions.execute_python:22': {'query': '{"collection": "articles", "filter": {"article_id": {"$in": [13,18,26,51,52,67,70,74,86,97,116,117,141,165,179,203,240,243,266,271,309,314,364,365,369,379,408,429,488,498,501,509,519,534,606,652,698,743,745,879,885,902,907,924,932,935,941,970,987,993,1001,1045,1053,1061,1065,1077,1084,1108,1137,1171,1190,1242,1244,1277,1332,1363,1366,1386,1435,1470,1477,1494,1531,1548,1570,1589,1611,1631,1662,1678,1689,1720,1727,1736,1769,1791,1792,1848,1853,1866,1880,1905,1910,1969,1978,1996,2009,2010,2017,2023]}}, "limit": 100}'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_articles_2015': 6696, 'regions': {'Europe': 1357, 'Africa': 1345, 'Asia': 1333, 'South America': 1332, 'North America': 1329}}, 'var_functions.execute_python:30': {'total_batches': 14, 'batch_size': 500, 'total_articles': 6696, 'first_batch_sample': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:32': {'total_to_process': 6696, 'batches_created': 14, 'processed_count': 6696}, 'var_functions.execute_python:34': {'processed_in_first_batch': 100, 'world_articles_found': {'South America': 13, 'Asia': 16, 'Africa': 9, 'Europe': 16, 'North America': 8}, 'remaining_to_fetch': 6596, 'total_2015_articles': 6696}, 'var_functions.execute_python:36': {'total_batches': 14, 'batch_size': 500, 'total_articles': 6696, 'world_counts_initial': {'North America': 0, 'Europe': 0, 'Asia': 0, 'South America': 0, 'Africa': 0}}, 'var_functions.execute_python:38': {'total_batches': 14, 'articles_to_process': 6696}, 'var_functions.execute_python:40': {'total_articles': 6696, 'processed': 100, 'remaining': 6596}, 'var_functions.execute_python:42': {'world_counts_initial': {'North America': 8, 'Europe': 16, 'Asia': 16, 'South America': 13, 'Africa': 9}, 'processed_in_first_batch': 100, 'total_remaining': 6596, 'total_batches': 14}, 'var_functions.execute_python:44': {'world_counts_from_first_100': {'North America': 8, 'Europe': 16, 'Asia': 16, 'South America': 13, 'Africa': 9}, 'world_articles_found': 62, 'regions_covered': ['South America', 'North America', 'Asia', 'Africa', 'Europe']}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': {'total_2015_articles': 6696, 'found_in_current_batch': 96, 'sample_article_id': '13'}, 'var_functions.execute_python:50': {'world_counts_batch': {'North America': 8, 'Europe': 16, 'Asia': 16, 'South America': 11, 'Africa': 9}, 'world_articles_found': 60, 'total_processed': 96}, 'var_functions.execute_python:52': {'total_2015': 6696, 'already_have': 2000, 'still_missing': 6600, 'missing_batches': 14}, 'var_functions.execute_python:54': {'min_id': 13, 'max_id': 127570, 'id_ranges': [[0, 50], [1000, 46], [2000, 49], [3000, 54], [4000, 38], [5000, 60], [6000, 50], [7000, 52], [8000, 46], [9000, 49], [10000, 47], [11000, 53], [12000, 54], [13000, 52], [14000, 47], [15000, 50], [16000, 39], [17000, 53], [18000, 59], [19000, 50], [20000, 53], [21000, 54], [22000, 53], [23000, 56], [24000, 49], [25000, 37], [26000, 41], [27000, 52], [28000, 47], [29000, 47], [30000, 52], [31000, 47], [32000, 47], [33000, 68], [34000, 51], [35000, 52], [36000, 60], [37000, 56], [38000, 50], [39000, 61], [40000, 54], [41000, 56], [42000, 55], [43000, 53], [44000, 61], [45000, 55], [46000, 62], [47000, 63], [48000, 59], [49000, 57], [50000, 50], [51000, 51], [52000, 61], [53000, 57], [54000, 48], [55000, 53], [56000, 49], [57000, 60], [58000, 70], [59000, 57], [60000, 70], [61000, 62], [62000, 40], [63000, 49], [64000, 60], [65000, 47], [66000, 69], [67000, 55], [68000, 44], [69000, 51], [70000, 64], [71000, 33], [72000, 66], [73000, 54], [74000, 53], [75000, 59], [76000, 47], [77000, 51], [78000, 46], [79000, 51], [80000, 65], [81000, 45], [82000, 53], [83000, 50], [84000, 58], [85000, 49], [86000, 52], [87000, 53], [88000, 37], [89000, 42], [90000, 55], [91000, 37], [92000, 58], [93000, 55], [94000, 44], [95000, 48], [96000, 38], [97000, 56], [98000, 55], [99000, 43], [100000, 43], [101000, 59], [102000, 50], [103000, 65], [104000, 53], [105000, 64], [106000, 43], [107000, 49], [108000, 43], [109000, 55], [110000, 47], [111000, 52], [112000, 43], [113000, 56], [114000, 52], [115000, 52], [116000, 55], [117000, 57], [118000, 57], [119000, 67], [120000, 55], [121000, 51], [122000, 52], [123000, 52], [124000, 54], [125000, 53], [126000, 53], [127000, 38]]}, 'var_functions.execute_python:56': {'world_counts_current_batch': {'North America': 8, 'Europe': 16, 'Asia': 16, 'South America': 11, 'Africa': 9}, 'world_articles_in_batch': 60, 'total_processed': 96, 'remaining_to_fetch': 6600, 'total_2015_articles': 6696}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)

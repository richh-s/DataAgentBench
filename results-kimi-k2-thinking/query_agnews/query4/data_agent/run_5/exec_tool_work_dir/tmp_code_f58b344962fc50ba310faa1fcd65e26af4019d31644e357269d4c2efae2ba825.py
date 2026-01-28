code = """import json
import pandas as pd

# Load metadata  
metadata_file = locals()['var_functions.query_db:2']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Sample 100 articles for development
sample_articles = metadata_2015[:100]
sample_ids = [item['article_id'] for item in sample_articles]

# Create MongoDB query
test_query = {
    "collection": "articles", 
    "filter": {"article_id": {"$in": sample_ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1}
}

print('__RESULT__:')
print(json.dumps(test_query))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'total_articles_2015': 6696, 'sample_article_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'total_articles_2015': 6696, 'regions': {'Europe': 1357, 'Africa': 1345, 'Asia': 1333, 'South America': 1332, 'North America': 1329}, 'sample_article_ids': [13, 18, 26, 51, 52]}, 'var_functions.query_db:16': [{'_id': '6969d2e9f019e7d9c4967ba7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d2e9f019e7d9c4967ba8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d2e9f019e7d9c4967ba9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d2e9f019e7d9c4967baa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d2e9f019e7d9c4967bab', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:18': {'collection': 'articles', 'filter': {'article_id': {'$in': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271, 309, 314, 364, 365, 369, 379, 408, 429, 488, 498, 501, 509, 519, 534, 606, 652, 698, 743, 745, 879, 885, 902, 907, 924, 932, 935, 941, 970, 987, 993, 1001, 1045, 1053, 1061, 1065, 1077, 1084, 1108, 1137, 1171, 1190, 1242, 1244, 1277, 1332, 1363, 1366, 1386, 1435, 1470, 1477, 1494, 1531, 1548, 1570, 1589, 1611, 1631, 1662, 1678, 1689, 1720, 1727, 1736, 1769, 1791, 1792, 1848, 1853, 1866, 1880, 1905, 1910, 1969, 1978, 1996, 2009, 2010, 2017, 2023]}}, 'projection': {'article_id': 1, 'title': 1, 'description': 1}}, 'var_functions.query_db:20': []}

exec(code, env_args)

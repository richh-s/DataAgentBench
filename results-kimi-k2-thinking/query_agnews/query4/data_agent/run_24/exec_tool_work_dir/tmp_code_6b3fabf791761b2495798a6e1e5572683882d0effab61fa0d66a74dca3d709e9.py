code = """import json

# Load 2015 metadata and articles
metadata_file = locals()['var_functions.query_db:58']
articles_file = locals()['var_functions.query_db:59']

with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Create article lookup
articles_dict = {a['article_id']: a for a in all_articles}

# Match articles with metadata
articles_to_analyze = []
for meta in metadata_2015:
    article_id = meta['article_id']
    if article_id in articles_dict:
        articles_to_analyze.append({
            'article_id': article_id,
            'title': articles_dict[article_id]['title'],
            'description': articles_dict[article_id]['description'],
            'region': meta['region']
        })

# Define category keywords
category_keywords = {
    'Sports': ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'nfl', 'nba', 'mlb', 'nhl', 'world cup', 'olympics', 'tournament', 'championship', 'coach', 'player', 'team'],
    'Business': ['stock market', 'economy', 'economic', 'business', 'wall st', 'wall street', 'company', 'corporate', 'financial', 'investment', 'profit', 'revenue', 'bank', 'ipo'],
    'Science/Technology': ['technology', 'tech', 'science', 'research', 'study', 'digital', 'internet', 'computer', 'nuclear', 'solar', 'renewable'],
    'World': ['iraq', 'iran', 'afghanistan', 'japan', 'south korea', 'north korea', 'china', 'saudi', 'militia', 'rebels', 'eurozone', 'eu', 'united nations', 'un', 'peace', 'war', 'conflict', 'diplomatic', 'embassy', 'foreign', 'global', 'international']
}

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    for category, keywords in category_keywords.items():
        if any(keyword in text for keyword in keywords):
            return category
    
    return 'Other'

# Categorize articles and count World articles by region
world_articles_by_region = {}
total_world = 0

for article in articles_to_analyze:
    category = categorize_article(article['title'], article['description'])
    
    if category == 'World':
        region = article['region']
        world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1
        total_world += 1

# Find region with most World articles
if world_articles_by_region:
    top_region = max(world_articles_by_region, key=world_articles_by_region.get)
    top_count = world_articles_by_region[top_region]
else:
    top_region = None
    top_count = 0

print('__RESULT__:')
print(json.dumps({
    'total_articles_analyzed': len(articles_to_analyze),
    'total_world_articles': total_world,
    'world_articles_by_region': world_articles_by_region,
    'top_region': top_region,
    'top_region_count': top_count
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:19': {'metadata_type': "<class 'str'>", 'articles_type': "<class 'list'>"}, 'var_functions.execute_python:12': {'world_articles_count': 1, 'region_counts': {}, 'top_region': None}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_2015_articles': 3, 'world_articles_count': 0, 'region_world_counts': {}, 'top_region': None, 'top_region_count': 0}, 'var_functions.query_db:18': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.execute_python:24': {'total_2015_articles': 0, 'world_articles_total': 0, 'world_articles_by_region': {}, 'top_region': None, 'top_region_count': 0}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'metadata_2015_count': 6696, 'all_articles_count': 1000, 'sample_article': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'sample_metadata': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}]}, 'var_functions.execute_python:30': {'metadata_count': 6696, 'sample_ids': ['13', '18', '26', '51', '52']}, 'var_functions.execute_python:32': {'article_ids_sample': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97'], 'total_ids': 100}, 'var_functions.query_db:34': [], 'var_functions.execute_python:36': {'min_id': 13, 'max_id': 127570, 'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_functions.query_db:38': [], 'var_functions.query_db:40': [], 'var_functions.execute_python:42': {'min_id': 0, 'max_id': 999, 'sample_ids': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'total_2015_metadata': 6696, 'available_articles_count': 50000, 'filtered_2015_count': 2606, 'available_range': {'min': 0, 'max': 49999}}, 'var_functions.query_db:48': [], 'var_functions.query_db:50': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:52': {'total_2015_articles_analyzed': 0, 'world_articles_by_region': {}, 'top_region': None, 'top_region_count': 0, 'total_world_articles': 0}, 'var_functions.execute_python:54': {'first_metadata': {'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, 'article_id_type': "<class 'str'>", 'sample_article_ids_from_articles': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, 'var_functions.execute_python:56': {'metadata_count': 6696, 'articles_count': 5, 'common_ids_count': 0, 'common_ids_sample': []}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.execute_python:62': {'total_2015_in_metadata': 6696, 'total_articles_fetched': 100000, 'matched_articles': 5226, 'sample_matched': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators.", 'region': 'Europe'}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.', 'region': 'South America'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.', 'region': 'Africa'}]}}

exec(code, env_args)

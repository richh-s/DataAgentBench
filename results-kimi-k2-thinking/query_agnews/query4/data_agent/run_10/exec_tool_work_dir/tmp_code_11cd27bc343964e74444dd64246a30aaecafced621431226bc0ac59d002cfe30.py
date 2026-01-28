code = """import json
from collections import Counter

# Load data
articles_file = locals()['var_functions.query_db:32']
metadata_file = locals()['var_functions.query_db:24']

with open(articles_file, 'r') as f:
    articles = json.load(f)

with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

articles_dict = {str(a['article_id']): a for a in articles}

# Get matching 2015 articles
articles_2015 = []
for meta in metadata_2015:
    aid = str(meta['article_id'])
    if aid in articles_dict:
        article = articles_dict[aid]
        articles_2015.append({
            'region': meta['region'],
            'title': article['title'],
            'desc': article['description'],
            'text': (article['title'] + ' ' + article['description']).lower()
        })

# Classify articles by category
business_terms = ['stock', 'market', 'economy', 'business', 'ipo', 'profit', 'shares', 'dollar', 'trade deficit', 'trade gap', 'stocks', 'wall st', 'finance', 'investment']
sports_terms = ['sports', 'game', 'match', 'olympics', 'football', 'soccer', 'basketball', 'tennis', 'nba', 'nfl', 'baseball']
tech_terms = ['science', 'technology', 'digital', 'software', 'internet', 'google', 'apple', 'microsoft', 'intel', 'computer', 'web']
world_terms = ['war', 'conflict', 'iraq', 'iran', 'israel', 'afghanistan', 'pakistan', 'refugee', 'humanitarian', 'peace', 'military', 'terror', 'diplomatic', 'united nations', 'un', 'ambassador', 'treaty', 'sanctions', 'aid', 'foreign', 'global crisis', 'chad', 'sudan', 'lebanon', 'syria']

world_counts = Counter()
for article in articles_2015:
    text = article['text']
    
    # Skip if clearly business/sports/tech
    if any(t in text for t in business_terms[:5]): 
        continue
    if any(t in text for t in sports_terms):
        continue
    if any(t in text for t in tech_terms[:3]):
        continue
    
    # Check if world
    if any(t in text for t in world_terms):
        world_counts[article['region']] += 1

# Get top region
top_region = world_counts.most_common(1)

result = {
    'total_world_articles': sum(world_counts.values()),
    'by_region': dict(world_counts),
    'top_region': top_region[0] if top_region else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'articles_in_database': 100, 'metadata_entries_2015': 6696, 'matching_articles_2015': 10}, 'var_functions.query_db:16': [{'_id': '6969d8cb28fdce3a67a0b6d0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d8cb28fdce3a67a0b6d1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d8cb28fdce3a67a0b6d2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d8cb28fdce3a67a0b6d3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d8cb28fdce3a67a0b6d4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:20': {'total_articles': 5, 'total_metadata_2015': 6696, 'total_matches': 0}, 'var_functions.query_db:22': [{'_id': '6969d8cb28fdce3a67a0b6d0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d8cb28fdce3a67a0b6d1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d8cb28fdce3a67a0b6d2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d8cb28fdce3a67a0b6d3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d8cb28fdce3a67a0b6d4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [{'_id': '6969d8cb28fdce3a67a0b6d0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d8cb28fdce3a67a0b6d1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d8cb28fdce3a67a0b6d2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d8cb28fdce3a67a0b6d3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d8cb28fdce3a67a0b6d4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:28': [{'_id': '6969d8cb28fdce3a67a0b6d0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d8cb28fdce3a67a0b6d1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d8cb28fdce3a67a0b6d2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d8cb28fdce3a67a0b6d3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d8cb28fdce3a67a0b6d4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:30': [{'_id': '6969d8cb28fdce3a67a0b6d0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d8cb28fdce3a67a0b6d1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d8cb28fdce3a67a0b6d2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d8cb28fdce3a67a0b6d3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d8cb28fdce3a67a0b6d4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'total_articles': 10000, 'total_metadata_2015': 6696, 'total_matches': 494}, 'var_functions.execute_python:38': {'total_matching_articles': 494, 'sample_articles': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators.", 'region': 'Europe'}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.', 'region': 'South America'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.', 'region': 'Africa'}]}, 'var_functions.execute_python:42': {'world_articles_total': 196, 'world_articles_by_region': {'North America': 36, 'Asia': 37, 'Africa': 45, 'Europe': 34, 'South America': 44}, 'top_region': ['Africa', 45]}}

exec(code, env_args)

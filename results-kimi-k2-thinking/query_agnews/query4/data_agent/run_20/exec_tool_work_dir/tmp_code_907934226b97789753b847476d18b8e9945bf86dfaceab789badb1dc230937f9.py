code = """import json
import re

# Load all data
meta_path = locals()['var_functions.query_db:2']
arts_path = locals()['var_functions.query_db:44']

with open(meta_path, 'r') as f:
    metadata_2015 = json.load(f)

with open(arts_path, 'r') as f:
    articles_all = json.load(f)

# Create mappings
article_region_map = {int(rec['article_id']): rec['region'] for rec in metadata_2015}
articles_lookup = {int(rec['article_id']): rec for rec in articles_all}

# Get common articles
common_ids = set(article_region_map.keys()) & set(articles_lookup.keys())

# Categorize articles as World
world_keywords = ['world', 'global', 'international', 'united nations', 'un', 'war', 'conflict', 'peace', 'diplomat', 'embassy', 'crisis', 'foreign', 'relations']
sports_keywords = ['sports', 'game', 'match', 'team', 'player', 'coach', 'league', 'tournament', 'championship', 'football', 'soccer', 'basketball', 'baseball', 'tennis']
business_keywords = ['business', 'economy', 'stock', 'market', 'company', 'corporate', 'investment', 'finance', 'bank', 'earnings', 'profit', 'loss', 'trading']
scitech_keywords = ['science', 'technology', 'research', 'study', 'scientist', 'tech', 'internet', 'software', 'hardware', 'computer', 'digital', 'data', 'innovation']

def categorize_article(title, description):
    """Categorize article based on title and description"""
    text = (title + ' ' + description).lower()
    
    # Check for sports
    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    
    # Check for business
    if any(keyword in text for keyword in business_keywords):
        return 'Business'
    
    # Check for science/technology
    if any(keyword in text for keyword in scitech_keywords):
        return 'Science/Technology'
    
    # Check for world news
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    
    # Default based on content patterns
    if 'oil' in text or 'opec' in text or 'trade' in text or 'dollar' in text:
        if 'economy' in text or 'market' in text or 'stock' in text or 'price' in text:
            return 'Business'
        return 'World'
    
    if any(country in text for country in ['iraq', 'iran', 'saudi', 'israel', 'palestine', 'afghanistan', 'pakistan', 'india', 'china', 'japan', 'korea', 'africa']):
        return 'World'
    
    return 'Other'

# Process only 2015 articles with content
world_articles_by_region = {}
total_checked = 0

for article_id in common_ids:
    article = articles_lookup[article_id]
    title = article.get('title', '')
    description = article.get('description', '')
    
    category = categorize_article(title, description)
    total_checked += 1
    
    if category == 'World':
        region = article_region_map[article_id]
        world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1

print('Total 2015 articles checked:', total_checked)
print('World articles by region:')
for region in sorted(world_articles_by_region.keys(), key=lambda x: world_articles_by_region[x], reverse=True):
    print(f'  {region}: {world_articles_by_region[region]}')

# Find region with most World articles
if world_articles_by_region:
    top_region = max(world_articles_by_region, key=world_articles_by_region.get)
    print(f'\nTop region for World articles: {top_region} ({world_articles_by_region[top_region]} articles)')
else:
    print('No World category articles found')

result = {
    'total_checked': total_checked,
    'world_by_region': world_articles_by_region,
    'top_region': max(world_articles_by_region, key=world_articles_by_region.get) if world_articles_by_region else None
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'metadata_count': 6696, 'articles_count': 5}, 'var_functions.query_db:16': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:28': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:48': {'metadata_2015_count': 6696, 'articles_all_count': 50000, 'common_ids_count': 2606}, 'var_functions.execute_python:50': {'total_2015_articles': 2606, 'region_counts': {'Asia': 517, 'North America': 489, 'South America': 529, 'Europe': 535, 'Africa': 536}}}

exec(code, env_args)

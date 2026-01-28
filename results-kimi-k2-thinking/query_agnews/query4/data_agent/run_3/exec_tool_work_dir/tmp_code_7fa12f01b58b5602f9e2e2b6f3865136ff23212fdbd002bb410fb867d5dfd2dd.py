code = """import json
import re

# Read the 2015 metadata from file
metadata_file = locals()['var_functions.query_db:2']
with open(metadata_file, 'r') as f:
    all_2015_metadata = json.load(f)

# Read all articles from file
articles_file = locals()['var_functions.query_db:12']
with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Create dictionaries for easier lookup
metadata_dict = {item['article_id']: item for item in all_2015_metadata}
articles_dict = {str(article['article_id']): article for article in all_articles}

# Find intersection - articles that exist in both datasets and are from 2015
common_article_ids = set(metadata_dict.keys()) & set(articles_dict.keys())

# World category keywords based on typical news patterns
world_keywords = [
    'world', 'global', 'international', 'united nations', 'un',
    'war', 'conflict', 'peace', 'diplomatic', 'diplomacy',
    'europe', 'asia', 'africa', 'america', 'middle east',
    'iraq', 'iran', 'afghanistan', 'china', 'russia', 'ukraine',
    'crisis', 'treaty', 'summit', 'foreign', 'embassy',
    'military', 'nato', 'eu', 'european union',
    'israel', 'palestine', 'peace talks', 'austerity',
    'climate', 'global warming', 'emissions', 'carbon'
]

# Sports keywords (to exclude)
sports_keywords = [
    'olympic', 'olympics', 'world cup', 'football', 'soccer',
    'basketball', 'baseball', 'tennis', 'golf', 'nfl', 'nba',
    'championship', 'tournament', 'coach', 'player', 'game',
    'match', 'score', 'victory', 'defeat', 'team'
]

# Business keywords (to exclude)
business_keywords = [
    'stock', 'stocks', 'wall st', 'wall street', 'finance',
    'financial', 'economy', 'economic', 'market', 'markets',
    'investment', 'investing', 'profits', 'earnings', 'shares',
    'trading', 'quarterly', 'business', 'company', 'companies'
]

# Science/Technology keywords (to exclude)
science_tech_keywords = [
    'science', 'technology', 'tech', 'research', 'study',
    'scientist', 'scientists', 'digital', 'internet', 'web',
    'computer', 'computers', 'software', 'hardware', 'data',
    'ai', 'artificial intelligence', 'robot', 'robotics',
    'space', 'nasa', 'satellite', 'physics', 'chemistry',
    'medical', 'medicine', 'health', 'disease', 'vaccine'
]

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
    if any(keyword in text for keyword in science_tech_keywords):
        return 'Science/Technology'
    
    # Check for world
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    
    # Default to World if unclear (many political/international stories)
    return 'World'

# Count articles by region for World category only
world_articles_by_region = {}
total_processed = 0
world_count = 0

for article_id in common_article_ids:
    article = articles_dict[article_id]
    title = article.get('title', '')
    description = article.get('description', '')
    
    category = categorize_article(title, description)
    total_processed += 1
    
    if category == 'World':
        world_count += 1
        region = metadata_dict[article_id]['region']
        world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1

# Find region with most World articles
if world_articles_by_region:
    max_region = max(world_articles_by_region.items(), key=lambda x: x[1])
else:
    max_region = ('None', 0)

print('__RESULT__:')
print(json.dumps({
    'total_processed': total_processed,
    'world_articles': world_count,
    'world_by_region': world_articles_by_region,
    'top_region': max_region[0],
    'top_count': max_region[1]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:12': [{'_id': '6969d1d05681768c0793155f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d1d05681768c07931560', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d1d05681768c07931561', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d1d05681768c07931562', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d1d05681768c07931563', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': 6696, 'var_functions.execute_python:16': 6696}

exec(code, env_args)

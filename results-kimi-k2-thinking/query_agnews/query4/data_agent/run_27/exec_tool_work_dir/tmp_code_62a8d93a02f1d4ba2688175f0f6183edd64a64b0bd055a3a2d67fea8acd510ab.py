code = """import json

# Load all articles data from file path
articles_path = var_functions.query_db:18
with open(articles_path, 'r') as f:
    all_articles = json.load(f)

# Load metadata for 2015 from file path
metadata_path = var_functions.query_db:3
with open(metadata_path, 'r') as f:
    all_metadata = json.load(f)

# Filter for 2015 articles
metadata_2015 = [m for m in all_metadata if m.get('publication_date', '').startswith('2015-')]

print(f'Loaded {len(all_articles)} total articles')
print(f'Found {len(metadata_2015)} articles from 2015')

# Categorize World articles
def is_world_category(title, description):
    """Determine if article belongs to World category"""
    text = (title + ' ' + description).lower()
    
    # World news indicators
    world_terms = [
        'iraq', 'iran', 'afghanistan', 'sudan', 'chad', 'nigeria', 
        'saudi', 'japan', 'china', 'india', 'korea', 'eurozone', 'euro',
        'united nations', 'refugee', 'war', 'conflict', 'militia',
        'oil', 'opec', 'pipeline', 'export', 'dollar', 'trade deficit',
        'global', 'world', 'international'
    ]
    
    # Sports indicators (to exclude)
    sports_terms = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 
                   'olympics', 'world cup', 'game', 'match', 'player', 'team']
    
    # Business indicators (to exclude)
    business_terms = ['stock', 'shares', 'profit', 'company', 'market', 'ipo',
                     'investment', 'funds', 'economy', 'economic']
    
    # Check if it's World news
    world_score = sum(1 for term in world_terms if term in text)
    sports_score = sum(1 for term in sports_terms if term in text)
    business_score = sum(1 for term in business_terms if term in text)
    
    # Simple heuristic: if world terms dominate, it's World category
    if world_score > sports_score and world_score > business_score and world_score > 0:
        return True
    return False

# Find World category articles from 2015
world_articles_2015 = []
for article in all_articles:
    article_id = int(article['article_id'])
    # Check if this article has 2015 metadata
    if article_id in [int(m['article_id']) for m in metadata_2015]:
        if is_world_category(article['title'], article['description']):
            # Find matching metadata
            metadata = next((m for m in metadata_2015 if int(m['article_id']) == article_id), None)
            if metadata:
                world_articles_2015.append({
                    'article_id': article_id,
                    'region': metadata['region'],
                    'title': article['title']
                })

print(f'Found {len(world_articles_2015)} World category articles from 2015')

# Count articles by region
from collections import Counter
region_counts = Counter([art['region'] for art in world_articles_2015])
print(f'Region counts: {region_counts}')

# Find region with most articles
if region_counts:
    top_region = region_counts.most_common(1)[0]
    print(f'Top region: {top_region[0]} with {top_region[1]} articles')
    
    print('__RESULT__:')
    print(json.dumps({
        'top_region': top_region[0],
        'article_count': top_region[1],
        'all_counts': dict(region_counts)
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No World category articles found'}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e431beeeb5230db76b0e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e431beeeb5230db76b0f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e431beeeb5230db76b10', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e431beeeb5230db76b11', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e431beeeb5230db76b12', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:16': {'articles_type': "<class 'list'>", 'articles_length': 5, 'metadata_type': "<class 'str'>", 'metadata_is_str': True}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)

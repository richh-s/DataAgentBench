code = """import json
import pandas as pd
from collections import Counter
import re

# Load metadata
print('Loading metadata...')
metadata_key = 'var_functions.query_db:5'
metadata_data = locals().get(metadata_key)

if isinstance(metadata_data, str) and metadata_data.endswith('.json'):
    with open(metadata_data, 'r') as f:
        metadata = json.load(f)
else:
    metadata = metadata_data

metadata_df = pd.DataFrame(metadata)
print(f'Metadata loaded: {len(metadata_df)} articles from 2015')

# Load articles from file
print('Loading articles...')
articles_key = 'var_functions.query_db:14'
articles_path = locals().get(articles_key)

if isinstance(articles_path, str) and articles_path.endswith('.json'):
    with open(articles_path, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_path

articles_df = pd.DataFrame(articles)
print(f'Articles loaded: {len(articles_df)} total articles')

# Merge data
print('Merging data...')
merged_df = metadata_df.merge(articles_df, left_on='article_id', right_on='article_id', how='left')
print(f'Merged dataset: {len(merged_df)} articles from 2015 with content')

# Define World category keywords (based on the hints)
world_keywords = [
    'iraq', 'iraqi', 'afghanistan', 'afghan', 'iran', 'israel', 'palestine', 'palestinian',
    'north korea', 'south korea', 'korean', 'china', 'chinese', 'japan', 'japanese',
    'russia', 'russian', 'putin', 'europe', 'european', 'germany', 'german', 'france', 'french',
    'britain', 'british', 'uk', 'africa', 'african', 'india', 'indian', 'pakistan', 'pakistani',
    'mexico', 'mexican', 'canada', 'canadian', 'australia', 'australian',
    'un', 'united nations', 'world bank', 'imf', 'wto', 'world trade organization',
    'war', 'peace', 'diplomatic', 'diplomat', 'embassy', 'ambassador', 'treaty',
    'global', 'international', 'foreign', 'abroad', 'overseas',
    'oil', 'crude', 'opec', 'energy prices', 'climate', 'global warming'
]

def is_world_article(title, description):
    """Classify if an article belongs to World category"""
    if pd.isna(title):
        title = ''
    if pd.isna(description):
        description = ''
    
    text = (title + ' ' + description).lower()
    
    # Count keyword matches
    for keyword in world_keywords:
        if keyword in text:
            return True
    return False

# Classify World articles
print('Classifying World articles...')
world_mask = merged_df.apply(lambda row: is_world_article(row['title'], row['description']), axis=1)
world_articles = merged_df[world_mask]

print(f'World articles found: {len(world_articles)}')

# Count by region
region_counts = Counter(world_articles['region'])
print(f'World articles by region: {dict(region_counts)}')

# Find region with most World articles
if region_counts:
    top_region = region_counts.most_common(1)[0]
    result = {
        'top_region': top_region[0],
        'article_count': top_region[1],
        'total_world_articles': len(world_articles)
    }
else:
    result = {'error': 'No World articles found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'_id': '6969ed34a6e02032ce7d406b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969ed34a6e02032ce7d406c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969ed34a6e02032ce7d406d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969ed34a6e02032ce7d406e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969ed34a6e02032ce7d406f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'total_2015_articles': 6696, 'total_articles': 5, 'merged_size': 6696, 'columns': ['article_id', 'region', 'publication_date', '_id', 'title', 'description'], 'sample': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17', 'title': nan}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15', 'title': nan}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03', 'title': nan}, {'article_id': '51', 'region': 'South America', 'publication_date': '2015-06-14', 'title': nan}, {'article_id': '52', 'region': 'Africa', 'publication_date': '2015-06-02', 'title': nan}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

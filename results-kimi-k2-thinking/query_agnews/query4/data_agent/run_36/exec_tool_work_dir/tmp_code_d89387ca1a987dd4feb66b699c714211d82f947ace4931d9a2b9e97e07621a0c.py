code = """import json
from collections import Counter
import math

# Load the metadata for 2015 articles
metadata_file = var_functions.query_db:5
with open(metadata_file) as f:
    metadata_list = json.load(f)

# Load all articles
articles_file = var_functions.query_db:14
with open(articles_file) as f:
    articles_list = json.load(f)

# Create article lookup by article_id
article_lookup = {str(a['article_id']): a for a in articles_list}

# Combine metadata with article content
combined = []
for meta in metadata_list:
    article_id = str(meta['article_id'])
    article = article_lookup.get(article_id, {})
    
    combined.append({
        'article_id': article_id,
        'region': meta['region'],
        'publication_date': meta['publication_date'],
        'title': article.get('title', ''),
        'description': article.get('description', '')
    })

# Classify World articles based on keywords in title/description
world_keywords = [
    'global', 'international', 'world', 'foreign', 'diplomatic',
    'war', 'iraq', 'iran', 'afghanistan', 'china', 'japan', 'russia',
    'europe', 'africa', 'korea', 'united nations', 'un', 'treaty',
    'peace', 'embassy', 'ambassador', 'climate', 'opec'
]

world_articles = []
for item in combined:
    title = item['title'].lower() if item['title'] else ''
    description = item['description'].lower() if item['description'] else ''
    text = title + ' ' + description
    
    if any(keyword in text for keyword in world_keywords):
        world_articles.append(item)

# Count by region
region_counts = Counter()
for article in world_articles:
    region = article['region']
    if region and isinstance(region, str):
        region_counts[region] += 1

# Get top region
top_region = region_counts.most_common(1)[0] if region_counts else ('None', 0)

result = {
    'top_region': top_region[0],
    'count': top_region[1],
    'total_world_articles': len(world_articles),
    'regions': dict(region_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'_id': '6969ed34a6e02032ce7d406b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969ed34a6e02032ce7d406c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969ed34a6e02032ce7d406d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969ed34a6e02032ce7d406e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969ed34a6e02032ce7d406f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'total_2015_articles': 6696, 'total_articles': 5, 'merged_size': 6696, 'columns': ['article_id', 'region', 'publication_date', '_id', 'title', 'description'], 'sample': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17', 'title': nan}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15', 'title': nan}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03', 'title': nan}, {'article_id': '51', 'region': 'South America', 'publication_date': '2015-06-14', 'title': nan}, {'article_id': '52', 'region': 'Africa', 'publication_date': '2015-06-02', 'title': nan}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:32': [{'total_2015': '6696'}]}

exec(code, env_args)

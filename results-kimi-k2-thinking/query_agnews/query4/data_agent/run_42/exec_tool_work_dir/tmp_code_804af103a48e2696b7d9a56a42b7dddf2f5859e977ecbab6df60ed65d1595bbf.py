code = """import json

# Read full metadata file
with open('/tmp/tmpz2v4h6i1.json', 'r') as f:
    metadata = json.load(f)

# Read articles data (this was returned directly)
articles = [{"article_id": "0", "title": "Wall St. Bears Claw Back Into the Black (Reuters)", "description": "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {"article_id": "1", "title": "Carlyle Looks Toward Commercial Aerospace (Reuters)", "description": "Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market."}, {"article_id": "2", "title": "Oil and Economy Cloud Stocks' Outlook (Reuters)", "description": "Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums."}, {"article_id": "3", "title": "Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)", "description": "Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday."}, {"article_id": "4", "title": "Oil prices soar to all-time record, posing new menace to US economy (AFP)", "description": "AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections."}]

# Filter 2015 articles and create article_id to region mapping
metadata_2015 = [m for m in metadata if m['publication_date'].startswith('2015-')]
article_to_region = {m['article_id']: m['region'] for m in metadata_2015}

# Get articles that are in 2015 metadata
articles_2015 = [a for a in articles if a['article_id'] in article_to_region]

# Classify articles based on title/description keywords
def classify_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Business keywords
    if any(word in text for word in ['stock', 'wall st', 'economy', 'oil', 'business', 'reuters', 'investment', 'market', 'commercial', 'aerospace', 'carlyle', 'company', 'finance']):
        return 'Business'
    
    # World keywords
    world_keywords = ['iraq', 'war', 'rebel', 'militia', 'middle east', 'conflict', 'attack', 'bomb', 'terror', 'political', 'presidential', 'election']
    if any(word in text for word in world_keywords):
        return 'World'
        
    return None

# Process the articles
results = []
for article in articles_2015:
    article_id = article['article_id']
    title = article['title']
    description = article['description']
    
    category = classify_article(title, description)
    region = article_to_region.get(article_id, 'Unknown')
    
    results.append({
        'article_id': article_id,
        'title': title,
        'category': category,
        'region': region,
        'year': '2015'
    })

# Filter for World category
world_articles = [r for r in results if r['category'] == 'World']

# Count by region
from collections import Counter
region_counts = Counter([article['region'] for article in world_articles])

# Find region with max count
if region_counts:
    max_region = max(region_counts, key=region_counts.get)
    max_count = region_counts[max_region]
else:
    max_region = "None"
    max_count = 0

output = {
    'world_articles_count': len(world_articles),
    'region_counts': dict(region_counts),
    'top_region': max_region,
    'top_region_count': max_count
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)

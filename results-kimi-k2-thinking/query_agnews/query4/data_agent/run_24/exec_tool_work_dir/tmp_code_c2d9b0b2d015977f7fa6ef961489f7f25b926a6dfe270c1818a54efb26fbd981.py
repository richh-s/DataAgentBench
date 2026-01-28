code = """import json

# Load all article data from the file
articles_file = locals()['var_functions.query_db:14']
with open(articles_file, 'r') as f:
    articles_data = json.load(f)

# Load 2015 metadata from the previous file
metadata_file = locals()['var_functions.query_db:4']
with open(metadata_file, 'r') as f:
    metadata = json.load(f)

# Build a set of 2015 article IDs for quick lookup
article_ids_2015 = set(str(m['article_id']) for m in metadata)

# Get 2015 articles
articles_2015 = [a for a in articles_data if str(a.get('article_id')) in article_ids_2015]

# Categorization logic - more refined
# World keywords focus on geopolitical/international
world_prefixes = ['world:', 'international:', 'global:']
world_keywords = ['iraq', 'iran', 'afghanistan', 'china', 'japan', 'south korea', 'saudi', 'iraq', 'iran', 'taliban', 'rebels', 'militia', 'nato', 'united nations', 'diplomatic', 'embassy', 'ambassador', 'treaty', 'alliance', 'europe', 'asia', 'africa', 'south america', 'african', 'asian', 'european', 'middle east', 'global', 'international']

# Category keywords
sports_keywords = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'olympics', 'world cup', 'championship', 'tournament', 'playoffs', 'coach', 'player', 'team', 'won', 'defeat', 'victory', 'score', 'game', 'match']

business_keywords = ['stock', 'market', 'share', 'economy', 'economic', 'business', 'company', 'corporate', 'financial', 'investment', 'profit', 'revenue', 'trade', 'stocks', 'wall st', 'federal reserve', 'bank', 'banking', 'interest rates']

science_tech_keywords = ['technology', 'tech', 'science', 'research', 'study', 'experiment', 'digital', 'internet', 'software', 'hardware', 'computer', 'innovation', 'scientist', 'discovery', 'nuclear', 'solar', 'renewable', 'energy', 'medical', 'health']

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Check category indicators
    is_sports = any(word in text for word in sports_keywords)
    is_business = any(word in text for word in business_keywords)
    is_science = any(word in text for word in science_tech_keywords)
    
    # World category - focus on international/geopolitical
    is_world = False
    
    # Check for world prefixes at start
    cleaned_title = title.lower().strip()
    if any(cleaned_title.startswith(prefix) for prefix in world_prefixes):
        is_world = True
    
    # Check for geopolitical keywords (and not business/stock focused)
    if not (is_business or is_sports or is_science):
        if any(keyword in text for keyword in world_keywords):
            is_world = True
    
    # If multiple flags, use priority: Sports > Business > Science > World
    if is_sports:
        return 'Sports'
    elif is_business:
        return 'Business'
    elif is_science:
        return 'Science/Technology'
    elif is_world:
        return 'World'
    else:
        return 'Other'

# Categorize all 2015 articles
categorized_articles = []
world_articles = []

for article in articles_2015:
    article_id = str(article.get('article_id'))
    title = article.get('title', '')
    description = article.get('description', '')
    
    category = categorize_article(title, description)
    categorized_articles.append({
        'article_id': article_id,
        'title': title,
        'category': category
    })
    
    if category == 'World':
        world_articles.append(article_id)

# Count world articles by region
region_world_counts = {}
for meta in metadata:
    article_id = str(meta['article_id'])
    region = meta['region']
    
    if article_id in world_articles:
        region_world_counts[region] = region_world_counts.get(region, 0) + 1

# Find top region
top_region = None
max_count = 0
for region, count in region_world_counts.items():
    if count > max_count:
        max_count = count
        top_region = region

result = {
    'total_2015_articles': len(categorized_articles),
    'world_articles_count': len(world_articles),
    'region_world_counts': region_world_counts,
    'top_region': top_region,
    'top_region_count': max_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:19': {'metadata_type': "<class 'str'>", 'articles_type': "<class 'list'>"}, 'var_functions.execute_python:12': {'world_articles_count': 1, 'region_counts': {}, 'top_region': None}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

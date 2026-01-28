code = """import json

# Load full article data (direct list)
articles_data = locals()['var_functions.query_db:18']

# Load 2015 metadata 
metadata_file = locals()['var_functions.query_db:19']
with open(metadata_file, 'r') as f:
    metadata = json.load(f)

# Create a dictionary for quick article lookup
articles_dict = {str(a['article_id']): a for a in articles_data}

# Get 2015 articles
articles_2015 = []
for meta in metadata:
    article_id = str(meta['article_id'])
    if article_id in articles_dict:
        article = articles_dict[article_id]
        articles_2015.append({
            'article_id': article_id,
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'region': meta.get('region', '')
        })

# Categorize articles
def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Sports indicators
    if any(word in text for word in ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'nfl', 'nba', 'mlb', 'nhl', 'world cup', 'olympics', 'tournament', 'championship', 'coach', 'player', 'team']):
        return 'Sports'
    
    # Business indicators
    if any(word in text for word in ['stock market', 'economy', 'economic', 'business', 'wall st', 'wall street', 'company', 'corporate', 'financial', 'investment', 'profit', 'revenue', 'bank', 'interest rates', 'dow jones', 'nasdaq']):
        return 'Business'
    
    # Science/Tech indicators
    if any(word in text for word in ['technology', 'tech', 'science', 'research', 'study', 'digital', 'internet', 'software', 'hardware', 'computer', 'innovation', 'nuclear', 'solar', 'renewable', 'medical', 'health', 'scientist']):
        return 'Science/Technology'
    
    # World indicators - geopolitical/international focus
    world_indicators = ['iraq', 'iran', 'afghanistan', 'israel', 'palestine', 'syria', 'lebanon', 'pakistan', 'india', 'china', 'japan', 'south korea', 'north korea', 'russia', 'ukraine', 'nato', 'united nations', 'diplomatic', 'embassy', 'ambassador', 'treaty', 'alliance', 'europe', 'asia', 'africa', 'south america', 'middle east', 'militia', 'rebels', 'global', 'international']
    
    if any(indicator in text for indicator in world_indicators):
        return 'World'
    
    return 'Other'

# Categorize and count
world_articles_by_region = {}
for article in articles_2015:
    category = categorize_article(article['title'], article['description'])
    region = article['region']
    
    if category == 'World':
        world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1

# Find top region
top_region = max(world_articles_by_region, key=world_articles_by_region.get) if world_articles_by_region else None
top_count = world_articles_by_region.get(top_region, 0)

result = {
    'total_2015_articles': len(articles_2015),
    'world_articles_total': sum(world_articles_by_region.values()),
    'world_articles_by_region': world_articles_by_region,
    'top_region': top_region,
    'top_region_count': top_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:19': {'metadata_type': "<class 'str'>", 'articles_type': "<class 'list'>"}, 'var_functions.execute_python:12': {'world_articles_count': 1, 'region_counts': {}, 'top_region': None}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_2015_articles': 3, 'world_articles_count': 0, 'region_world_counts': {}, 'top_region': None, 'top_region_count': 0}, 'var_functions.query_db:18': [{'_id': '6969e22fc8ea0d34cb738e98', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e22fc8ea0d34cb738e99', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e22fc8ea0d34cb738e9a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e22fc8ea0d34cb738e9b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e22fc8ea0d34cb738e9c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json'}

exec(code, env_args)

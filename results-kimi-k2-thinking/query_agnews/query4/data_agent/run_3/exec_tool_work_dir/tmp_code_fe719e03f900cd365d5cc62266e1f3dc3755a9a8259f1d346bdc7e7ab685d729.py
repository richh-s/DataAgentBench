code = """import json

# Load metadata for 2015 articles
metadata_file = str(locals()['var_functions.query_db:2'])
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Load all articles
articles_file = str(locals()['var_functions.query_db:12'])
with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Create lookup dictionaries
metadata_dict = {item['article_id']: item for item in metadata_2015}
articles_dict = {str(article['article_id']): article for article in all_articles}

# Keywords for categorization
world_keywords = [
    'world', 'global', 'international', 'war', 'conflict', 'peace', 'diplomatic', 'diplomacy',
    'europe', 'asia', 'africa', 'america', 'middle east', 'iraq', 'iran', 'afghanistan', 'china', 'russia', 'ukraine',
    'crisis', 'treaty', 'summit', 'foreign', 'military', 'nato', 'eu', 'european union',
    'israel', 'palestine', 'climate', 'global warming', 'emissions', 'carbon'
]

sports_keywords = ['olympic', 'olympics', 'world cup', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'game', 'match']

business_keywords = ['stock', 'stocks', 'wall st', 'wall street', 'finance', 'financial', 'economy', 'economic', 'market', 'business', 'company']

science_tech_keywords = ['science', 'technology', 'tech', 'research', 'study', 'scientist', 'digital', 'internet', 'computer', 'software', 'space', 'nasa', 'medical', 'health']

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    if any(keyword in text for keyword in business_keywords):
        return 'Business'
    if any(keyword in text for keyword in science_tech_keywords):
        return 'Science/Technology'
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    return 'World'  # Default for political/international news

# Count World articles by region in 2015
world_by_region = {}
common_ids = set(metadata_dict.keys()) & set(articles_dict.keys())

for article_id in common_ids:
    article = articles_dict[article_id]
    category = categorize_article(article.get('title', ''), article.get('description', ''))
    
    if category == 'World':
        region = metadata_dict[article_id]['region']
        world_by_region[region] = world_by_region.get(region, 0) + 1

# Find region with most World articles
top_region = max(world_by_region.items(), key=lambda x: x[1]) if world_by_region else ('None', 0)

print('__RESULT__:')
print(json.dumps({
    'world_articles_by_region': world_by_region,
    'top_region': top_region[0],
    'top_count': top_region[1]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:12': [{'_id': '6969d1d05681768c0793155f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d1d05681768c07931560', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d1d05681768c07931561', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d1d05681768c07931562', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d1d05681768c07931563', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': 6696, 'var_functions.execute_python:16': 6696, 'var_functions.list_db:24': ['authors', 'article_metadata'], 'var_functions.execute_python:32': {'count': 6696}}

exec(code, env_args)

code = """import json
import re

# Load the 2015 articles from previous query
articles_2015 = locals()['articles_2015']
article_region_map = locals()['article_region_map']

# Categorization function
def categorize_article(title, description):
    # Combine title and description (lowercase for easier matching)
    text = (title + ' ' + description).lower()
    
    # World category indicators
    world_keywords = [
        'iraq', 'iran', 'saudi', 'israel', 'palestine', 'afghanistan', 'pakistan', 'india', 'china', 'japan',
        'korea', 'africa', 'europe', 'asia', 'america', 'mexico', 'canada', 'australia', 'uk', 'britain',
        'france', 'germany', 'spain', 'italy', 'russia', 'ukraine', 'syria', 'lebanon', 'turkey',
        'refugee', 'war', 'peace', 'diplomatic', 'united nations', 'un', 'world', 'global',
        'international', 'foreign', 'embassy', 'ambassador', 'summit', 'treaty',
        'tsunami', 'earthquake', 'hurricane', 'flood', 'disaster', 'crisis'
    ]
    
    # Business keywords
    business_keywords = [
        'stocks', 'stock market', 'wall st', 'wall street', 'shares', 'profit', 'loss',
        'earnings', 'revenue', 'IPO', 'merger', 'acquisition', 'bankruptcy',
        'oil prices', 'commodity', 'oil', 'gold', 'dollar', 'euro', 'interest rates',
        'economy', 'economic', 'gdp', 'inflation', 'fed', 'economist', 'finance'
    ]
    
    # Sports keywords
    sports_keywords = [
        'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf',
        'olympics', 'world cup', 'championship', 'tournament', 'coach', 'player',
        'team', 'league', 'match', 'game', 'score', 'victory', 'defeat', 'win', 'lose'
    ]
    
    # Science/Technology keywords
    tech_keywords = [
        'google', 'microsoft', 'apple', 'intel', 'hp', 'dell', 'technology', 'tech',
        'science', 'scientist', 'research', 'study', 'researchers', 'internet', 'web',
        'computer', 'software', 'hardware', 'semiconductor', 'chip', 'nanotechnology',
        'biotech', 'genetics', 'space', 'NASA', 'satellite', 'robot', 'AI', 'artificial intelligence'
    ]
    
    # Score each category
    scores = {'World': 0, 'Business': 0, 'Sports': 0, 'Science/Technology': 0}
    
    # Check World
    for keyword in world_keywords:
        if keyword in text:
            scores['World'] += 1
    
    # Check Business
    for keyword in business_keywords:
        if keyword in text:
            scores['Business'] += 1
            
    # Check Sports
    for keyword in sports_keywords:
        if keyword in text:
            scores['Sports'] += 1
            
    # Check Science/Technology
    for keyword in tech_keywords:
        if keyword in text:
            scores['Science/Technology'] += 1
    
    # Find the category with highest score
    max_score = max(scores.values())
    if max_score == 0:
        return 'World'  # Default category if no clear match
    
    # Return category with highest score
    for category, score in scores.items():
        if score == max_score:
            return category

# Categorize all 2015 articles
categorized_articles = []
world_articles = []

for article in articles_2015:
    category = categorize_article(article['title'], article['description'])
    categorized_articles.append({
        'article_id': article['article_id'],
        'title': article['title'],
        'category': category,
        'region': article_region_map.get(article['article_id'], 'Unknown')
    })
    
    if category == 'World':
        world_articles.append(article['article_id'])

print('Total 2015 articles categorized:', len(categorized_articles))
print('World category articles:', len(world_articles))

# Show samples
print('\nSample World articles:')
for article in categorized_articles[:20]:
    if article['category'] == 'World':
        print(f"- {article['title'][:80]}... (Region: {article['region']})")

print('__RESULT__:')
print(json.dumps({
    'total_2015_articles': len(categorized_articles),
    'world_articles_count': len(world_articles)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e2f52f04fcdaecf22318', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e2f52f04fcdaecf22319', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e2f52f04fcdaecf2231a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e2f52f04fcdaecf2231b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e2f52f04fcdaecf2231c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:4': ['authors', 'article_metadata'], 'var_functions.query_db:6': [{'_id': '6969e2f52f04fcdaecf22318', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e2f52f04fcdaecf22319', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e2f52f04fcdaecf2231a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e2f52f04fcdaecf2231b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e2f52f04fcdaecf2231c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_articles_2015': 6696, 'regions': {'Europe': 1357, 'South America': 1332, 'Africa': 1345, 'Asia': 1333, 'North America': 1329}}, 'var_functions.query_db:20': [{'_id': '6969e2f52f04fcdaecf22318', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e2f52f04fcdaecf22319', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e2f52f04fcdaecf2231a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e2f52f04fcdaecf2231b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e2f52f04fcdaecf2231c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:22': {'total_articles': 5, 'articles_2015_count': 0, 'article_ids_2015_count': 6696}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_articles': 10000, 'articles_2015_count': 494}}

exec(code, env_args)

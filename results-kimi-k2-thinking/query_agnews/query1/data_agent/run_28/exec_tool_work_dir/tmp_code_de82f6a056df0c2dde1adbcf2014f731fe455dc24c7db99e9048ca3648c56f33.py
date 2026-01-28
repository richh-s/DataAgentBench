code = """import json

# Load the articles
articles_key = 'var_functions.query_db:0'
articles = locals()[articles_key]

# If it's a file path, read it
if isinstance(articles, str):
    with open(articles, 'r') as f:
        articles = json.load(f)

# Categorize articles based on title/description keywords
sports_keywords = ['sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympics', 'world cup', 'super bowl', 'nfl', 'nba', 'mlb', 'nhl', 'match', 'game', 'player', 'team', 'coach', 'league', 'tournament', 'championship']

business_keywords = ['business', 'wall st', 'stock', 'economy', 'market', 'company', 'firm', 'investment', 'finance', 'corporate']
world_keywords = ['iraq', 'war', 'peace', 'conflict', 'oil', 'pipeline', 'presidential', 'elections']
scitech_keywords = ['technology', 'science', 'research', 'study', 'scientist', 'tech', 'innovation', 'space']

articles_categorized = []

for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    text = title + ' ' + description
    
    # Check for sports
    is_sports = any(keyword in text for keyword in sports_keywords)
    
    # Check for business
    is_business = any(keyword in text for keyword in business_keywords)
    
    # Check for world news  
    is_world = any(keyword in text for keyword in world_keywords)
    
    # Check for science/tech
    is_scitech = any(keyword in text for keyword in scitech_keywords)
    
    # Assign category based on highest match
    if is_sports:
        category = 'Sports'
    elif is_business:
        category = 'Business'
    elif is_world:
        category = 'World'
    elif is_scitech:
        category = 'Science/Technology'
    else:
        category = 'Uncategorized'
    
    articles_categorized.append({
        'article_id': article.get('article_id'),
        'title': article.get('title'),
        'description': article.get('description'),
        'description_length': len(article.get('description', '')),
        'category': category
    })

# Filter sports articles
sports_articles = [a for a in articles_categorized if a['category'] == 'Sports']

print('__RESULT__:')
print(json.dumps({
    'all_articles': articles_categorized,
    'sports_articles': sports_articles,
    'total_articles': len(articles_categorized),
    'total_sports': len(sports_articles)
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'_id': '696974d78d4ca6ceda5b83fc', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696974d78d4ca6ceda5b83fd', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696974d78d4ca6ceda5b83fe', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696974d78d4ca6ceda5b83ff', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696974d78d4ca6ceda5b8400', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:2': {'total_articles': 5, 'preview': [{'_id': '696974d78d4ca6ceda5b83fc', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696974d78d4ca6ceda5b83fd', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696974d78d4ca6ceda5b83fe', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.execute_python:5': {'articles': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'description_length': 94}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.', 'description_length': 214}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.', 'description_length': 184}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'description_length': 195}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.', 'description_length': 160}], 'total_count': 5}}

exec(code, env_args)

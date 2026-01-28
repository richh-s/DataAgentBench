code = """import json
import re

# Get all articles
articles = var_functions.query_db:10

# Define sports keywords to identify sports articles
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey',
    'olympics', 'world cup', 'championship', 'tournament', 'match', 'game',
    'player', 'team', 'coach', 'league', 'season', 'score', 'victory', 'defeat',
    'sport', 'sports', 'athlete', 'athletic', 'race', 'racing', 'marathon',
    'medal', 'win', 'won', 'loss', 'competition', 'final', 'quarter', 'semi',
    'nba', 'nfl', 'mlb', 'nhl', 'premier league', 'champions league',
    'grand slam', 'wimbledon', 'us open', 'australian open', 'french open',
    'world series', 'super bowl', 'stanley cup'
]

def is_sports_article(title, description):
    """Check if article is sports-related based on title and description"""
    text = (title + ' ' + description).lower()
    for keyword in sports_keywords:
        if keyword in text:
            return True
    return False

# Categorize articles
sports_articles = []
business_articles = []
world_articles = []
scitech_articles = []

for article in articles:
    title = article.get('title', '')
    description = article.get('description', '')
    
    if is_sports_article(title, description):
        sports_articles.append(article)
    elif any(word in title.lower() for word in ['oil', 'economy', 'stocks', 'wall st', 'reuters', 'carlyle', 'group', 'market']):
        business_articles.append(article)
    elif any(word in title.lower() for word in ['iraq', 'pipeline', 'authorities', 'militia']):
        world_articles.append(article)
    else:
        # Default based on content
        if 'economy' in description.lower() or 'market' in description.lower() or 'stock' in description.lower():
            business_articles.append(article)
        else:
            world_articles.append(article)

print(f"Total articles: {len(articles)}")
print(f"Sports articles: {len(sports_articles)}")
print(f"Business articles: {len(business_articles)}")
print(f"World articles: {len(world_articles)}")
print(f"Science/Tech articles: {len(scitech_articles)}")

# If no sports articles found, we need to query for more
result = {
    'sports_articles': sports_articles,
    'business_articles': business_articles,
    'world_articles': world_articles,
    'scitech_articles': scitech_articles,
    'need_more_articles': len(sports_articles) == 0
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69696a7443295558a7f48161', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696a7443295558a7f48162', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696a7443295558a7f48163', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696a7443295558a7f48164', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696a7443295558a7f48165', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': [{'_id': '69696a7443295558a7f48161', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696a7443295558a7f48162', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696a7443295558a7f48163', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696a7443295558a7f48164', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696a7443295558a7f48165', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:10': [{'_id': '69696a7443295558a7f48161', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696a7443295558a7f48162', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696a7443295558a7f48163', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696a7443295558a7f48164', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696a7443295558a7f48165', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

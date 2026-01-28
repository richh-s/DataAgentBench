code = """import json
import re

# Retrieve the articles data
articles_data = locals()['var_functions.query_db:0']

# Check if it's a file path (string) or direct data
if isinstance(articles_data, str):
    # It's a file path, read the JSON file
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    # It's direct data
    articles = articles_data

# Define sports keywords to identify sports articles
sports_keywords = [
    'sports', 'game', 'games', 'football', 'basketball', 'baseball', 'soccer', 
    'tennis', 'golf', 'olympic', 'olympics', 'championship', 'tournament',
    'league', 'team', 'player', 'coach', 'season', 'score', 'victory',
    'defeat', 'match', 'race', 'racing', 'athlete', 'athletes', 'sport',
    'quarterback', 'pitcher', 'goal', 'points', 'yards', 'nba', 'nfl',
    'mlb', 'nhl', 'world cup', 'super bowl', 'playoff', 'playoffs'
]

# Function to check if an article is about sports
def is_sports_article(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            return True
    return False

# Filter sports articles and calculate description lengths
sports_articles = []
for article in articles:
    if is_sports_article(article['title'], article['description']):
        desc_length = len(article['description'])
        sports_articles.append({
            'article_id': article['article_id'],
            'title': article['title'],
            'description': article['description'],
            'desc_length': desc_length
        })

# Sort by description length to find the longest
sports_articles_sorted = sorted(sports_articles, key=lambda x: x['desc_length'], reverse=True)

# Debug: print what we found
print('__RESULT__:')
print(json.dumps({
    'sports_articles_count': len(sports_articles),
    'sports_articles': sports_articles_sorted[:5] if sports_articles_sorted else []
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696cfeb5fadd9f9fe575e8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696cfeb5fadd9f9fe575e9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696cfeb5fadd9f9fe575ea', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696cfeb5fadd9f9fe575eb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696cfeb5fadd9f9fe575ec', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

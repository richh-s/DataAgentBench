code = """import json
import os

# Load articles from file
file_path = locals()['var_functions.query_db:16']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Look at some articles to understand the dataset better
print('First 20 articles:')
for i, article in enumerate(articles[:20]):
    print(f"{i}: {article.get('title')}")

print('\n' + '='*60)
print('SCANNING FOR SPORTS ARTICLES...')
print('='*60)

# Let's be more explicit about sports identification
sports_keywords = [
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'hockey',
    'tennis', 'golf', 'cricket', 'rugby', 'volleyball', 'swimming', 'olympic',
    'athlete', 'athletes', 'game', 'games', 'team', 'teams', 'player', 'players',
    'coach', 'coaches', 'league', 'leagues', 'tournament', 'tournament',
    'match', 'matches', 'score', 'scores', 'championship', 'championships',
    'nba', 'nfl', 'mlb', 'nhl', 'world cup', 'super bowl', 'world series',
    'champion', 'champions', 'title', 'titles', 'victory', 'victories'
]

def is_sports_article(title, description):
    title_lower = title.lower()
    desc_lower = description.lower()
    
    # Count how many sports keywords appear
    keyword_count = sum(1 for keyword in sports_keywords if keyword in title_lower or keyword in desc_lower)
    
    # Must have at least 2 sports-specific terms to be classified as sports
    # (this avoids false positives like "game theory" or "team building")
    sports_specific_terms = ['football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 
                            'cricket', 'rugby', 'volleyball', 'nba', 'nfl', 'mlb', 'nhl', 'world cup',
                            'super bowl', 'olympics', 'championship', 'athlete', 'athletes']
    
    specific_count = sum(1 for term in sports_specific_terms if term in title_lower or term in desc_lower)
    
    return specific_count >= 1 or keyword_count >= 3

sports_articles = []

for article in articles:
    if is_sports_article(article.get('title', ''), article.get('description', '')):
        sports_articles.append({
            'article_id': article.get('article_id'),
            'title': article.get('title'),
            'description': article.get('description'),
            'description_length': len(article.get('description', ''))
        })

print(f"\nFound {len(sports_articles)} sports articles")

if sports_articles:
    print("\nSports articles found:")
    for article in sports_articles:
        print(f"ID {article['article_id']}: {article['title']}")
        print(f"Desc length: {article['description_length']}")
        print()
    
    # Find the sports article with longest description
    longest_article = max(sports_articles, key=lambda x: x['description_length'])
    
    result = {
        'title': longest_article['title'],
        'description_length': longest_article['description_length'],
        'article_id': longest_article['article_id']
    }
else:
    result = {
        'title': None,
        'message': 'No sports articles found',
        'total_articles_checked': len(articles)
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'title': None, 'message': 'No sports articles'}, 'var_functions.query_db:14': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'title': None, 'message': 'No sports articles found in current sample', 'total_articles_checked': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'title': "Why Windows isn't Unix"}}

exec(code, env_args)

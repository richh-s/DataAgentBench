code = """import json
import os

# Load articles from file
file_path = locals()['var_functions.query_db:16']
with open(file_path, 'r') as f:
    articles = json.load(f)

print('Total articles loaded:', len(articles))

# ONLY very specific sports keywords (avoid false positives)
specific_sports_terms = [
    'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis',
    'golf', 'cricket', 'rugby', 'volleyball', 'badminton', 'squash',
    'boxing', 'wrestling', 'mma', 'ufc', 'nascar', 'formula 1', 'f1',
    'olympics', 'olympic', 'nba', 'nfl', 'mlb', 'nhl', 'ncaa', 'fifa',
    'world cup', 'super bowl', 'world series', 'euro cup', 'champions league',
    'premier league', 'athlete', 'athletes', 'track and field', 'swimming',
    'gymnastics', 'cycling', 'cyclist', 'marathon', 'sprint', 'medal', 'medals'
]

# General sports terms (need more of these to count)
general_sports_terms = ['coach', 'coaches', 'player', 'players', 'team', 'teams', 
                        'league', 'leagues', 'season', 'championship', 'tournament']

def is_sports_article(title, description):
    text = (title + ' ' + description).lower()
    
    # If we find specific sports terms, it's likely sports
    for term in specific_sports_terms:
        if term in text:
            return True
    
    # Need at least 3 general terms to count as sports (reduces false positives)
    general_count = sum(1 for term in general_sports_terms if term in text)
    return general_count >= 3

sports_articles = []

for article in articles:
    if is_sports_article(article.get('title', ''), article.get('description', '')):
        sports_articles.append({
            'id': article.get('article_id'),
            'title': article.get('title'),
            'length': len(article.get('description', ''))
        })

print('Sports articles found:', len(sports_articles))

if sports_articles:
    # Print first 10 to verify
    print('\nFirst few sports articles found:')
    for i, article in enumerate(sports_articles[:10]):
        print(f"{i+1}: {article['title']}")
    
    # Find longest
    longest = max(sports_articles, key=lambda x: x['length'])
    result = {'title': longest['title']}
else:
    # Let's see what went wrong by checking some random articles
    print('\nSample articles (first 10):')
    for i, article in enumerate(articles[:10]):
        print(f"{i}: {article.get('title')}")
    
    result = {'title': None, 'sports_count': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'title': None, 'message': 'No sports articles'}, 'var_functions.query_db:14': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'title': None, 'message': 'No sports articles found in current sample', 'total_articles_checked': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'title': "Why Windows isn't Unix"}, 'var_functions.execute_python:24': {'title': 'China Begins Countdown for Next Manned Space Flight'}}

exec(code, env_args)

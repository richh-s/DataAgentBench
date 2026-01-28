code = """import json
import os

# Load the full dataset
file_path = locals()['var_functions.query_db:16']
with open(file_path, 'r') as f:
    all_articles = json.load(f)

print('Total articles:', len(all_articles))

# Sports detection function
def is_sports(title, desc):
    text = (title + ' ' + desc).lower()
    
    # Specific sports - high confidence
    specific = ['football', 'soccer', 'basketball', 'tennis', 'golf', 'cricket', 'baseball', 'hockey', 'boxing', 'wrestling']
    for sport in specific:
        if sport in text:
            return True
    
    # Sports leagues
    leagues = ['nba', 'nfl', 'mlb', 'nhl', 'fifa', 'ncaa']
    for league in leagues:
        if league in text:
            return True
    
    # Sports events
    events = ['world cup', 'super bowl', 'olympics', 'olympic', 'championship']
    for event in events:
        if event in text:
            return True
    
    # General sports terms - need multiple matches
    general = ['athlete', 'player', 'players', 'team', 'teams', 'game', 'games', 'coach', 'coaches', 'league', 'season']
    general_count = sum(1 for term in general if term in text)
    
    return general_count >= 2

# Find sports articles
sports = []
for article in all_articles:
    if is_sports(article.get('title', ''), article.get('description', '')):
        sports.append({
            'id': article.get('article_id'),
            'title': article.get('title'),
            'length': len(article.get('description', ''))
        })

print('Sports articles found:', len(sports))

if sports:
    # Find longest
    longest = max(sports, key=lambda x: x['length'])
    print('Longest:', longest['title'])
    result = {'title': longest['title']}
else:
    result = {'title': None}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'title': None, 'message': 'No sports articles'}, 'var_functions.query_db:14': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'title': None, 'message': 'No sports articles found in current sample', 'total_articles_checked': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'title': "Why Windows isn't Unix"}, 'var_functions.execute_python:24': {'title': 'China Begins Countdown for Next Manned Space Flight'}, 'var_functions.execute_python:30': {'title': 'China Begins Countdown for Next Manned Space Flight'}, 'var_functions.query_db:34': [{'_id': '69696fbf477cc36744114c00', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696fbf477cc36744114c01', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696fbf477cc36744114c02', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696fbf477cc36744114c03', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696fbf477cc36744114c04', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:38': {'title': 'AMD starts shipping 90-nanometer chips to customers'}, 'var_functions.list_db:40': ['authors', 'article_metadata']}

exec(code, env_args)

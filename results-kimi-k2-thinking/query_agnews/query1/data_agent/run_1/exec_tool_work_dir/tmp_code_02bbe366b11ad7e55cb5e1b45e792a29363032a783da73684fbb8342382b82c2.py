code = """import json
import re

# Load all articles from file
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define sports keywords and patterns
sports_keywords = [
    'sports?', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'olympic', 'world cup', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl',
    'cricket', 'rugby', 'hockey', 'athlete', 'athletic', 'medal',
    'championship', 'tournament', 'match', 'game', 'player', 'coach',
    'season', 'league', 'team', 'score', 'victory', 'defeat', 'win',
    'lose', 'goal', 'points', 'yards', 'pitch', 'field', 'stadium'
]

sports_patterns = [
    r'\b(red sox|yankees|dodgers|cubs|mets)\b',
    r'\b(patriots|eagles|steelers|cowboys)\b',
    r'\b(lakers|celtics|warriors|bulls)\b',
    r'\b(arsenal|manchester|liverpool|chelsea)\b',
    r'\b(tiger woods|michael jordan|tom brady)\b'
]

sports_articles = []
for article in articles:
    title = article['title'].lower()
    description = article['description'].lower()
    
    is_sports = False
    
    # Check keywords
    for keyword in sports_keywords:
        if re.search(r'\b' + keyword + r'\b', title) or re.search(r'\b' + keyword + r'\b', description):
            is_sports = True
            break
    
    # Check patterns if not already identified
    if not is_sports:
        for pattern in sports_patterns:
            if re.search(pattern, title) or re.search(pattern, description):
                is_sports = True
                break
    
    if is_sports:
        sports_articles.append({
            'article_id': int(article['article_id']),
            'title': article['title'],
            'description': article['description'],
            'desc_length': len(article['description'])
        })

# Find the sports article with the longest description
if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['desc_length'])
    result = {
        'found_sports_articles': len(sports_articles),
        'longest_article': longest_article
    }
else:
    result = {
        'found_sports_articles': 0,
        'message': 'No sports articles found'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969634fcb9584e5a9a9cd5a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969634fcb9584e5a9a9cd5b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969634fcb9584e5a9a9cd5c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969634fcb9584e5a9a9cd5d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969634fcb9584e5a9a9cd5e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': {'type': "<class 'list'>", 'is_string': False, 'preview': [{'_id': '6969634fcb9584e5a9a9cd5a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969634fcb9584e5a9a9cd5b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}]}, 'var_functions.query_db:8': [{'_id': '6969634fcb9584e5a9a9cd5a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969634fcb9584e5a9a9cd5b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969634fcb9584e5a9a9cd5c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969634fcb9584e5a9a9cd5d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969634fcb9584e5a9a9cd5e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'desc_length': 94, 'appears_sports': False}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.', 'desc_length': 214, 'appears_sports': False}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.', 'desc_length': 184, 'appears_sports': False}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'desc_length': 195, 'appears_sports': False}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.', 'desc_length': 160, 'appears_sports': False}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_articles': 1000, 'sample_articles': [{'_id': '6969634fcb9584e5a9a9cd5a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969634fcb9584e5a9a9cd5b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969634fcb9584e5a9a9cd5c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}}

exec(code, env_args)

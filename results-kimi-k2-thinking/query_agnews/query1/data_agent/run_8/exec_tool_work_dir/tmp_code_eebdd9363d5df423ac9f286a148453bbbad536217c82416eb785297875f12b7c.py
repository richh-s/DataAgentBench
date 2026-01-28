code = """import json

file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    articles = json.load(f)

sports_keywords = ['sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'olympics', 'olympic', 'athlete', 'team', 'coach', 'player', 'race', 'championship', 'league', 'game', 'match', 'goal', 'score', 'win', 'loss', 'play', 'court', 'field', 'stadium', 'nfl', 'nba', 'mlb', 'nhl', 'golf', 'swimming', 'running', 'cycling', 'marathon', 'tournament']

sports_articles = []
for article in articles:
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    is_sports = False
    for keyword in sports_keywords:
        if keyword in title_lower or keyword in desc_lower:
            is_sports = True
            break
    
    if is_sports:
        sports_articles.append(article)

if sports_articles:
    longest_article = max(sports_articles, key=lambda x: len(x.get('description', '')))
    result = longest_article.get('title', '')
else:
    result = 'No sports articles found'

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696948203b0b87ea9f48a0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696948203b0b87ea9f48a1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696948203b0b87ea9f48a2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696948203b0b87ea9f48a3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696948203b0b87ea9f48a4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': 'No sports articles found', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': 'Technology as Fashion'}

exec(code, env_args)

code = """import json

articles_file = locals()['var_functions.query_db:16']
with open(articles_file, 'r') as f:
    articles = json.load(f)

sports_indicators = ['football', 'basketball', 'soccer', 'tennis', 'golf', 'baseball', 'hockey', 'cricket', 'rugby', 'volleyball', 'olympics', 'world cup', 'championship', 'league', 'player', 'team', 'game', 'coach', 'athlete', 'match', 'tournament', 'competition', 'score', 'season', 'playoff', 'medal', 'race', 'stadium', 'goal', 'win', 'lose', 'victory', 'defeat']

sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    desc = article.get('description', '').lower()
    combined = title + ' ' + desc
    
    for indicator in sports_indicators:
        if indicator in combined:
            sports_articles.append({
                'title': article['title'],
                'desc': article['description'],
                'len': len(article['description'])
            })
            break

if sports_articles:
    longest = max(sports_articles, key=lambda x: x['len'])
    result = longest['title']
else:
    result = "No sports articles found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '696976e1a4757cb31760c321', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696976e1a4757cb31760c322', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696976e1a4757cb31760c323', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696976e1a4757cb31760c324', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696976e1a4757cb31760c325', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': {'data_type': "<class 'list'>", 'is_str': False, 'is_list': True}, 'var_functions.execute_python:14': {'type': 'list', 'length': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': 39}

exec(code, env_args)

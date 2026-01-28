code = """import json

# Get all articles from the previous query
articles = locals()['var_functions.query_db:0']

# More strict sports classification
sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf',
    'hockey', 'cricket', 'rugby', 'volleyball', 'athlete', 'athletes',
    'olympic', 'olympics', 'nba', 'nfl', 'mlb', 'nhl', 'ncaa',
    'fifa', 'uefa', 'premier league', 'world cup', 'tournament',
    'championship', 'marathon', 'competition', 'coach', 'quarterback',
    'pitcher', 'goalie', 'striker', 'defender', 'midfielder'
]

sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    desc = article.get('description', '').lower()
    
    for keyword in sports_keywords:
        if keyword in title or keyword in desc:
            desc_length = len(article.get('description', ''))
            sports_articles.append({
                'title': article['title'],
                'description': article['description'],
                'desc_length': desc_length
            })
            break

result = None
if sports_articles:
    longest = max(sports_articles, key=lambda x: x['desc_length'])
    result = longest['title']
else:
    result = "No sports articles found in the dataset"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696304c44a224a53ec8f86', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696304c44a224a53ec8f87', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696304c44a224a53ec8f88', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696304c44a224a53ec8f89', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696304c44a224a53ec8f8a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:5': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)'}

exec(code, env_args)

code = """import json
records = var_call_5qZ5B0kSVghyUUnZHXzSnw0z

sport_keywords = [
    'football','soccer','basketball','baseball','cricket','tennis','golf','rugby',
    'match','game','tournament','season','league','player','coach','scored','goal',
    'win','defeat','victory','olympic','nfl','nba','mlb','nhl','score','kick','pitch',
    'matchup','cup','final','series','racing','f1','motorsport','boxing','wrestling'
]

sports_articles = []
for r in records:
    title = r.get('title','')
    desc = r.get('description','')
    combined = (title + ' ' + desc).lower()
    is_sport = any(kw in combined for kw in sport_keywords)
    if is_sport:
        sports_articles.append({'article_id': r.get('article_id'), 'title': title, 'description_length': len(desc)})

if sports_articles:
    # find the one with max description_length
    selected = max(sports_articles, key=lambda x: x['description_length'])
    selected_title = selected['title']
else:
    selected_title = None

result = {'sports_articles': sports_articles, 'selected_title': selected_title}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5qZ5B0kSVghyUUnZHXzSnw0z': [{'_id': '69598377f0ee892084a2184e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69598377f0ee892084a2184f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69598377f0ee892084a21850', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69598377f0ee892084a21851', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69598377f0ee892084a21852', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

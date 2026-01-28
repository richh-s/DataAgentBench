code = """import json, re
articles = var_functions.query_db:2
# Count total articles
print('Total articles', len(articles))
# Look for sports keywords
sports_keywords = ['sport', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympic', 'game', 'team', 'player', 'champion', 'league', 'tournament', 'match', 'win', 'loss', 'score', 'coach']
sports_articles = []
for a in articles:
    title = a.get('title','').lower()
    desc = a.get('description','').lower()
    combined = title + ' ' + desc
    if any(kw in combined for kw in sports_keywords):
        sports_articles.append(a)
print('Potential sports articles count', len(sports_articles))
# Show them
for a in sports_articles[:20]:
    print('ID:', a.get('article_id'), 'Title:', a.get('title'))
    print('Desc:', a.get('description')[:200])
    print('---')"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '696977808c517ff138e9d721', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696977808c517ff138e9d722', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696977808c517ff138e9d723', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696977808c517ff138e9d724', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696977808c517ff138e9d725', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

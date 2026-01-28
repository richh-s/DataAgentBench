code = """import json
# var_call_kkRXo8BHhul4StspqtJQ7OtV is available from previous query
records = var_call_kkRXo8BHhul4StspqtJQ7OtV

sports_keywords = [
    'sport', 'sports', 'game', 'match', 'team', 'coach', 'goal', 'score', 'scored', 'season',
    'tournament', 'league', 'athlete', 'olympic', 'olympics', 'baseball', 'football', 'soccer',
    'basketball', 'tennis', 'golf', 'cricket', 'hockey', 'boxing', 'boxing', 'nba', 'mlb', 'nfl', 'nhl', 'fifa', 'racing', 'motorsport'
]

sports_articles = []
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    text = (title + ' ' + desc).lower()
    if any(kw in text for kw in sports_keywords):
        # Additional heuristic: avoid false positive for financial 'bears' or corporate terms
        # if 'wall st' in text or 'private investment' in text or 'oil' in text or 'crude' in text:
        #     continue
        sports_articles.append({'title': title, 'description': desc, 'desc_len': len(desc)})

if not sports_articles:
    result = json.dumps({'answer': None, 'message': 'No sports articles found'})
else:
    # find max by desc_len
    best = max(sports_articles, key=lambda x: x['desc_len'])
    result = json.dumps({'answer': best['title'], 'description_length': best['desc_len']})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_kkRXo8BHhul4StspqtJQ7OtV': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

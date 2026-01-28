code = """import json

data = var_call_xNJkC4XlIKiLE9GY0eisrEd6

sports_keywords = [
    'sport','football','soccer','basketball','baseball','cricket','tennis','golf',
    'olympic','olympics','coach','team','match','tournament','score','season','playoff',
    'boxing','mma','wrestling','hockey','goal','cup','racing','f1','nascar','mlb','nba','nfl',
    'athlete','stadium','pitch','kick','touchdown','home run','batting'
]

results = []
for rec in data:
    title = rec.get('title','')
    desc = rec.get('description','') or ''
    text = (title + ' ' + desc).lower()
    is_sports = any(kw in text for kw in sports_keywords)
    results.append({'article_id': rec.get('article_id'), 'title': title, 'description': desc, 'is_sports': is_sports, 'desc_len': len(desc)})

sports = [r for r in results if r['is_sports']]
if sports:
    best = max(sports, key=lambda r: r['desc_len'])
    out = {'title': best['title'], 'desc_len': best['desc_len']}
else:
    out = {'title': None, 'note': 'No sports articles found'}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_xNJkC4XlIKiLE9GY0eisrEd6': [{'_id': '695980e308a0855d807ebe67', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '695980e308a0855d807ebe68', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '695980e308a0855d807ebe69', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '695980e308a0855d807ebe6a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '695980e308a0855d807ebe6b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json
# data from previous query
data = var_call_XMJYmyn1pkBNiBZ1v40cLZ9d
sports_keywords = set(["sport","sports","game","games","match","season","league","score","scores","tournament","goal","goals","coach","player","team","teams","athlete","athletes","inning","bat","basketball","soccer","football","baseball","hockey","golf","tennis","olympic","olympics","fifa","nba","nfl","mlb","nhl"])

sports_articles = []
for rec in data:
    title = rec.get('title','') or ''
    desc = rec.get('description','') or ''
    combined = (title + ' ' + desc).lower()
    if any(k in combined for k in sports_keywords):
        sports_articles.append({'title': title, 'description': desc, 'desc_len': len(desc)})

if not sports_articles:
    result = json.dumps("No sports articles found.")
else:
    # find article with max description length
    best = max(sports_articles, key=lambda x: x['desc_len'])
    result = json.dumps(best['title'])

print("__RESULT__:")
print(result)"""

env_args = {'var_call_XMJYmyn1pkBNiBZ1v40cLZ9d': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

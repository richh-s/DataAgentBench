code = """import json

data = var_call_7G2NSpVuYyqGMvD5D9A1G1Dw
sports_keywords = ['game','match','team','teams','season','score','scores','player','players','goal','goals','league','tournament','coach','coaches','inning','quarter','bat','pitcher','soccer','football','baseball','basketball','hockey','tennis','golf','boxing','rugby','olympic','copa','fifa']

sports_articles = []
for rec in data:
    text = (rec.get('title','') + ' ' + rec.get('description','')).lower()
    if any(k in text for k in sports_keywords):
        sports_articles.append(rec)

if not sports_articles:
    result = "No sports articles found."
else:
    max_rec = max(sports_articles, key=lambda r: len(r.get('description','')))
    result = max_rec.get('title','')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_7G2NSpVuYyqGMvD5D9A1G1Dw': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

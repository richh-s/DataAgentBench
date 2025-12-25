code = """import json
articles = json.loads(locals()['var_function-call-232385937965345746']['query_db_response']['results'][0])
sports_articles = []
for article in articles:
    if 'sports' in article['title'].lower() or 'sports' in article['description'].lower() or 'football' in article['title'].lower() or 'football' in article['description'].lower() or 'basketball' in article['title'].lower() or 'basketball' in article['description'].lower() or 'baseball' in article['title'].lower() or 'baseball' in article['description'].lower() or 'soccer' in article['title'].lower() or 'soccer' in article['description'].lower() or 'golf' in article['title'].lower() or 'golf' in article['description'].lower() or 'tennis' in article['title'].lower() or 'tennis' in article['description'].lower() or 'olympics' in article['title'].lower() or 'olympics' in article['description'].lower():
        sports_articles.append(article)

max_desc_len = -1
article_with_max_desc = None

for article in sports_articles:
    desc_len = len(article['description'])
    if desc_len > max_desc_len:
        max_desc_len = desc_len
        article_with_max_desc = article

if article_with_max_desc:
    print('__RESULT__:')
    print(json.dumps(article_with_max_desc['title']))
else:
    print('__RESULT__:')
    print(json.dumps('No sports articles found.'))"""

env_args = {'var_function-call-232385937965345746': [{'_id': '6943c50fad6aebdd1613d354', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c50fad6aebdd1613d355', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c50fad6aebdd1613d356', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c50fad6aebdd1613d357', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c50fad6aebdd1613d358', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

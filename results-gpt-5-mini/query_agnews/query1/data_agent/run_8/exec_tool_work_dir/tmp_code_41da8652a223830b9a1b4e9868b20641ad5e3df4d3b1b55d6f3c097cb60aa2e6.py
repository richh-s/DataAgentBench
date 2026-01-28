code = """import json
# Access the query result stored in var_call_WDh1SpyB5i6K6Yvvr5dL9HNK
records = var_call_WDh1SpyB5i6K6Yvvr5dL9HNK

sports_keywords = ['sport','sports','football','soccer','basketball','baseball','cricket','tennis','golf','match','tournament','league','season','goal','score','scored','inning','nba','nfl','mlb','nhl','athlete','coach','team','rally','olympic']

sports_articles = []
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    text = (title + ' ' + desc).lower()
    is_sports = any(k in text for k in sports_keywords)
    if is_sports:
        sports_articles.append({'article_id': r.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

if sports_articles:
    # find article with max description length
    max_article = max(sports_articles, key=lambda x: x['desc_len'])
    result = {'sports_articles_count': len(sports_articles), 'longest_description_title': max_article['title'], 'longest_description_length': max_article['desc_len']}
else:
    result = {'sports_articles_count': 0, 'longest_description_title': None, 'longest_description_length': 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CDWMhk833Fe0Pe5DYgEC0S4f': ['articles'], 'var_call_WDh1SpyB5i6K6Yvvr5dL9HNK': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

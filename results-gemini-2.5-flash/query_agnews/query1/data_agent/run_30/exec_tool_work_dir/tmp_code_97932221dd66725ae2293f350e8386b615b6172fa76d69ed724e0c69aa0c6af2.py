code = """import json

articles_json_string = locals()['var_function-call-17656590824723793859']['query_db_response']['results'][0]
articles = json.loads(articles_json_string)

sports_keywords = ['sport', 'football', 'basketball', 'soccer', 'baseball', 'tennis', 'golf', 'olympics', 'game', 'match', 'team', 'player', 'championship', 'cup', 'league', 'race', 'athletic', 'tournament']

sports_articles = []
for article in articles:
    is_sports = False
    # Check in title
    for keyword in sports_keywords:
        if keyword in article['title'].lower():
            is_sports = True
            break
    if not is_sports: # Only check description if not already identified as sports from title
        for keyword in sports_keywords:
            if keyword in article['description'].lower():
                is_sports = True
                break
    
    if is_sports:
        sports_articles.append(article)

if not sports_articles:
    print('__RESULT__:')
    print(json.dumps('No sports articles found.'))
else:
    max_desc_len = -1
    title_with_max_desc = ''
    for article in sports_articles:
        desc_len = len(article['description'])
        if desc_len > max_desc_len:
            max_desc_len = desc_len
            title_with_max_desc = article['title']
    print('__RESULT__:')
    print(json.dumps(title_with_max_desc))"""

env_args = {'var_function-call-17656590824723793859': [{'_id': '6943ca909219f8345dbe46d8', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943ca909219f8345dbe46d9', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943ca909219f8345dbe46da', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943ca909219f8345dbe46db', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943ca909219f8345dbe46dc', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

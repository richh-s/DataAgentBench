code = """import json
# data from previous query
data = var_call_S1QTBXvbTnSWSUKYSLVReiU3

# Define simple keyword-based categorization
sports_keywords = {"game","games","team","teams","season","coach","player","players","match","score","scores","tournament","league","cup","olympic","olympics","goal","goals","runs","inning","basketball","football","soccer","baseball","tennis","golf","nba","nfl","mlb","nhl"}
science_keywords = {"technology","scientific","science","research","technology","tech","space","nasa","robot","ai","artificial intelligence","computer","software","hardware","biotech"}
business_keywords = {"market","markets","stocks","stock","economy","oil","prices","investment","investor","investors","firm","business","commercial","earnings","revenue","wall st","wall street","short-sellers","short sellers"}

classified = []
for doc in data:
    title = doc.get('title','')
    desc = doc.get('description','')
    text = (title + ' ' + desc).lower()
    category = None
    if any(k in text for k in sports_keywords):
        category = 'Sports'
    elif any(k in text for k in science_keywords):
        category = 'Science/Technology'
    elif any(k in text for k in business_keywords):
        category = 'Business'
    else:
        category = 'World'
    doc_len = len(desc) if desc is not None else 0
    classified.append({
        'article_id': doc.get('article_id'),
        'title': title,
        'description_length': doc_len,
        'category': category
    })

# Find sports articles
sports_articles = [d for d in classified if d['category']=='Sports']
if sports_articles:
    # choose one with max description length
    best = max(sports_articles, key=lambda x: x['description_length'])
    result = {'sports_article_title': best['title']}
else:
    result = {'sports_article_title': None, 'message': 'No articles classified as Sports were found.'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_S1QTBXvbTnSWSUKYSLVReiU3': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

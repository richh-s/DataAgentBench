code = """import json
records = var_call_rU1BzOtLaLjGf5OncjrY6nv6

# Define keyword sets for categories
sports_kw = ['game','season','scored','coach','team','match','tournament','olympic','win','loss','goal','league','playoff','inning','bat','basket','basketball','football','soccer','baseball','tennis','golf','hockey','stadium','player','players','score','defeat','victory','draw','cup','manager']
business_kw = ['stock','stocks','economy','market','investment','investor','firm','carlyle','private','bank','earnings','oil','crude','exports','export','presidential','president','short-sellers','short-seller','financial','finance']
world_kw = ['rebel','iraq','militia','authorities','pipeline','strike','infrastructure','government','war','conflict','global','world','country','border','presidential','election']
tech_kw = ['technology','computer','software','internet','scientist','research','nasa','tech','device','digital','ai','artificial intelligence','robot','space']

classified = []
sports_articles = []
for r in records:
    title = (r.get('title') or '')
    desc = (r.get('description') or '')
    text = (title + ' ' + desc).lower()
    scores = {
        'Sports': sum(text.count(k) for k in sports_kw),
        'Business': sum(text.count(k) for k in business_kw),
        'World': sum(text.count(k) for k in world_kw),
        'Science/Technology': sum(text.count(k) for k in tech_kw)
    }
    # Choose category with highest score; ties -> choose max by priority Business, World, Sports, Science/Technology
    sorted_scores = sorted(scores.items(), key=lambda x: (x[1], {'Business':4,'World':3,'Sports':2,'Science/Technology':1}[x[0]]), reverse=True)
    category = sorted_scores[0][0] if sorted_scores[0][1] > 0 else 'Unknown'
    rec = {'article_id': r.get('article_id'), 'title': title, 'description': desc, 'category': category, 'scores': scores}
    classified.append(rec)
    if category == 'Sports':
        sports_articles.append({'article_id': r.get('article_id'), 'title': title, 'description_length': len(desc)})

if sports_articles:
    maxrec = max(sports_articles, key=lambda x: x['description_length'])
    result = {'sports_found': True, 'title': maxrec['title'], 'article_id': maxrec['article_id'], 'description_length': maxrec['description_length'], 'classified': classified}
else:
    result = {'sports_found': False, 'message': 'No sports articles found in the articles collection.', 'classified': classified}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BJHoyOhggtoLFTT5HX0MTygz': ['articles'], 'var_call_rU1BzOtLaLjGf5OncjrY6nv6': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_5wQaHmp4wCtP7sGmpkYs8bwG': {'found': True, 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'article_id': '0', 'description_length': 94}, 'var_call_xmy4hD81nwkfb6xpb3nvgqJV': ['authors', 'article_metadata'], 'var_call_GetGROWfeOObFmSrxCPj61A0': 'file_storage/call_GetGROWfeOObFmSrxCPj61A0.json', 'var_call_ldhXMScKZODbd3xQ2xtl0U9i': {'found': False, 'message': 'No sports articles found in articles collection.'}}

exec(code, env_args)

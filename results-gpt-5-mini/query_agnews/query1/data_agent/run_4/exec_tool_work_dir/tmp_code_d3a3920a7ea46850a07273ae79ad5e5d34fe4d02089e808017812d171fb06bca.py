code = """import json

# var_call_aYwEdI71mN6wGG94ecHhpeiC is available from previous query
records = var_call_aYwEdI71mN6wGG94ecHhpeiC

sports_keywords = {"game","match","tournament","goal","score","football","soccer","baseball","basketball","tennis","golf","season","coach","team","league","win","defeat","played","player","players","stadium","cup"}

business_keywords = {"wall st","short-seller","short-sellers","stock","market","economy","investment","private","firm","shares","earnings","crude","oil prices","oil","aerospace","defense","billion"}

world_keywords = {"iraq","rebel","militia","pipeline","export","authorities","southern","strike","infrastructure","presidential","election","country","government"}

tech_keywords = {"technology","tech","scient","research","innovation","software","hardware","aerospace"}

sports_articles = []

for r in records:
    title = r.get('title','')
    desc = r.get('description','')
    text = (title + ' ' + desc).lower()
    # determine category with priority: sports, business, world, tech
    category = None
    if any(k in text for k in sports_keywords):
        category = 'Sports'
    elif any(k in text for k in business_keywords):
        category = 'Business'
    elif any(k in text for k in world_keywords):
        category = 'World'
    elif any(k in text for k in tech_keywords):
        category = 'Science/Technology'
    else:
        category = 'Unknown'
    desc_len = len(desc)
    if category == 'Sports':
        sports_articles.append({'article_id': r.get('article_id'), 'title': title, 'description_length': desc_len})

if not sports_articles:
    out = {"sports_found": False, "message": "No sports articles found"}
else:
    # pick max description_length
    best = max(sports_articles, key=lambda x: x['description_length'])
    out = {"sports_found": True, "title": best['title'], "description_length": best['description_length']}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_aYwEdI71mN6wGG94ecHhpeiC': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

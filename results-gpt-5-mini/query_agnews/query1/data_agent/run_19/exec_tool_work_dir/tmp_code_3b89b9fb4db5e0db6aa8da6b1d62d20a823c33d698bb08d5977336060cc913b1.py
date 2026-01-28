code = """import json

# var_call_G5TnIIBlc4ymJJpp50Fw1kWh is available from previous query_db call
records = var_call_G5TnIIBlc4ymJJpp50Fw1kWh

# Prepare keyword lists for simple heuristic classification
sports_kw = ['sport', 'sports', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 'golf', 'cricket', 'olympic', 'olympics', 'hockey', 'nhl', 'nfl', 'mlb', 'coach', 'team', 'match', 'tournament', 'season', 'goal', 'scored', 'win', 'wins', 'lost', 'defeat']
business_kw = ['wall st', 'wall street', 'stock', 'stocks', 'market', 'investment', 'firm', 'business', 'economy', 'earnings', 'private investment', 'carlyle', 'aerospace', 'commercial aerospace', 'company', 'companies', 'shares', 'crude', 'oil prices', 'oil']
world_kw = ['iraq', 'authorities', 'rebel', 'militia', 'southern', 'pipeline', 'exports', 'government', 'president', 'country', 'world']
tech_kw = ['technology', 'tech', 'scientists', 'research', 'nasa', 'scientific', 'science', 'technology', 'software', 'hardware']

def classify(text):
    t = text.lower()
    scores = {'Sports':0, 'Business':0, 'World':0, 'Science/Technology':0}
    for kw in sports_kw:
        if kw in t:
            scores['Sports'] += 1
    for kw in business_kw:
        if kw in t:
            scores['Business'] += 1
    for kw in world_kw:
        if kw in t:
            scores['World'] += 1
    for kw in tech_kw:
        if kw in t:
            scores['Science/Technology'] += 1
    # Choose max score; if all zero, default to World (conservative)
    max_cat = max(scores, key=lambda k: scores[k])
    if scores[max_cat] == 0:
        # fallback: try to infer from some words
        if 'reuters' in t or 'afp' in t or 'authorities' in t or 'iraq' in t:
            return 'World'
        return 'Business'
    return max_cat

# Classify each record and compute description lengths
for r in records:
    title = r.get('title','')
    desc = r.get('description','')
    combined = f"{title} {desc}"
    cat = classify(combined)
    r['category'] = cat
    r['desc_len'] = len(desc)

# Filter sports articles
sports_articles = [r for r in records if r['category']=='Sports']

if len(sports_articles) == 0:
    result = {'found': False, 'message': 'No sports articles found in the articles collection.'}
else:
    # find max desc_len
    best = max(sports_articles, key=lambda x: x['desc_len'])
    result = {'found': True, 'article_id': best.get('article_id'), 'title': best.get('title'), 'desc_len': best.get('desc_len')}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ydAfvbc1a5CI1dEhPNQ4mmhb': ['articles'], 'var_call_G5TnIIBlc4ymJJpp50Fw1kWh': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

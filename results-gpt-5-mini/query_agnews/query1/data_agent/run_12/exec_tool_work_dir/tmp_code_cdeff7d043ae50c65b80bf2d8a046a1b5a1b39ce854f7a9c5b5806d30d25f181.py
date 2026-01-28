code = """import json

docs = var_call_eAHBwvq2Yw7LPhQpM5EnbD6G

sports_keywords = [
    'game','match','tournament','season','goal','scored','coach','team','teams',
    'football','soccer','basketball','baseball','tennis','golf','olympic','olympics',
    'boxing','wrestling','cricket','hockey','score','win','loss','defeat','victory',
    'innings','quarterback','pitcher','goalkeeper','foul','league'
]

business_keywords = ['wall st','carlyle','investment','stock','stocks','economy','market','oil prices','reuters - private investment']
world_keywords = ['iraq','country','president','government','rebel','international','world','afp','reuters']
science_keywords = ['technology','scient','research','space','computer','software','hardware']

results = []
for d in docs:
    title = d.get('title','')
    desc = d.get('description','')
    text = (title + ' ' + desc).lower()
    category = None
    # simple categorization
    if any(k in text for k in sports_keywords):
        category = 'Sports'
    elif any(k in text for k in business_keywords):
        category = 'Business'
    elif any(k in text for k in world_keywords):
        category = 'World'
    elif any(k in text for k in science_keywords):
        category = 'Science/Technology'
    else:
        category = 'Unknown'
    results.append({'article_id': d.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc), 'category': category})

# find sports articles
sports = [r for r in results if r['category']=='Sports']
if not sports:
    out = json.dumps("No sports articles found in the articles collection.")
else:
    # find max desc_len
    max_len = max(r['desc_len'] for r in sports)
    candidates = [r for r in sports if r['desc_len']==max_len]
    # if multiple, return list of titles
    if len(candidates)==1:
        out = json.dumps(candidates[0]['title'])
    else:
        out = json.dumps([c['title'] for c in candidates])

print("__RESULT__:")
print(out)"""

env_args = {'var_call_OQNyfvPLFZnKbJXFrx8wdl9J': ['articles'], 'var_call_eAHBwvq2Yw7LPhQpM5EnbD6G': [{'_id': '695981b6b345fa2c2348fdc4', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '695981b6b345fa2c2348fdc5', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '695981b6b345fa2c2348fdc6', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '695981b6b345fa2c2348fdc7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '695981b6b345fa2c2348fdc8', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

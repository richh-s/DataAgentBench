code = """import json
from collections import Counter

# Load metadata 2015 entries from file
with open(var_call_sPHxAEet36BCsb0lyj6rO3bR, 'r') as f:
    meta = json.load(f)

# Load articles list from var_call_At8taWQaqt7txVJ56sljCjiZ
articles = var_call_At8taWQaqt7txVJ56sljCjiZ

# Build mapping from article_id (int) to title+description
art_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    art_map[aid] = (title + ' ' + desc).lower()

# Define keyword sets
business_kw = ['stock','stocks','market','markets','economy','oil','shares','bank','company','companies','revenue','invest','investment','merger','profit','earnings','wall st','carlyle','ft.','bloomberg']
Sports_kw = ['match','goal','goals','season','league','tournament','score','scores','won','beat','defeat','defeated','cup','football','soccer','basketball','nba','mlb','nfl','coach','player','players','race','olympic']
scitech_kw = ['technology','scientist','scientists','research','space','nasa','robot','software','tech','scientific','internet','ai','artificial intelligence','cyber','satellite','gadget']

# Classifier function
def classify(text):
    if not text:
        return 'World'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in Sports_kw:
        if kw in text:
            return 'Sports'
    for kw in scitech_kw:
        if kw in text:
            return 'Science/Technology'
    # fallback: if contains clearly world/politics keywords
    world_kw = ['president','minister','election','killed','militia','clashes','border','police','attack','attacked','terror','terrorist','united nations','diplomat','government','parliament','sanction','iraq','afghanistan','syria','korea','trump','obama']
    for kw in world_kw:
        if kw in text:
            return 'World'
    # default
    return 'World'

# Count regions for articles classified as World
region_counter = Counter()
unknown_articles = 0
for item in meta:
    try:
        aid = int(item.get('article_id'))
    except:
        continue
    region = item.get('region') or 'Unknown'
    text = art_map.get(aid, '').lower()
    if text == '':
        unknown_articles += 1
    cat = classify(text)
    if cat == 'World':
        region_counter[region] += 1

if not region_counter:
    result = {'error': 'No World articles found in 2015.'}
else:
    max_count = max(region_counter.values())
    top_regions = [r for r,c in region_counter.items() if c==max_count]
    result = {'top_regions': top_regions, 'count': max_count}

# Print result as JSON string
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_sPHxAEet36BCsb0lyj6rO3bR': 'file_storage/call_sPHxAEet36BCsb0lyj6rO3bR.json', 'var_call_TDLL7CPTtsGEdqUn62wVnUsR': 'file_storage/call_TDLL7CPTtsGEdqUn62wVnUsR.json', 'var_call_At8taWQaqt7txVJ56sljCjiZ': [{'_id': '6959a773a192c205671f58d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a773a192c205671f58d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a773a192c205671f58d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a773a192c205671f58da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a773a192c205671f58db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

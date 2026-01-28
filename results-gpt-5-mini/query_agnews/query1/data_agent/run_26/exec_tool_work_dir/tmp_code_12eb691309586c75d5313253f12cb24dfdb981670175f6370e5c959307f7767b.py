code = """import json
records = var_call_MxLHbXI7sU5fe0YBJVHVJ3L6
sports_kw = ['football','soccer','nba','nfl','mlb','mls','hockey','baseball','basketball','golf','tennis','match','tournament','goal','score','scored','coach','team','season','league','cup','olympic','win','defeat','players','game','games','points']
business_kw = ['wall street','wall st','short-sellers','short sellers','stock','stocks','market','investment','firm','economy','earnings','private investment','shares','bonds','revenue','financial','bank','carlyle','oil prices','crude','economy','business']
world_kw = ['iraq','pipeline','rebel','militia','oil exports','authorities','country','presidential','elections','world','afp','reuters','government']
science_kw = ['technology','aerospace','space','science','research','tech','software','hardware','internet','scient']

candidates = []
for r in records:
    title = r.get('title','')
    desc = r.get('description','')
    text = (title + ' ' + desc).lower()
    sports_count = sum(1 for k in sports_kw if k in text)
    business_count = sum(1 for k in business_kw if k in text)
    world_count = sum(1 for k in world_kw if k in text)
    science_count = sum(1 for k in science_kw if k in text)
    # choose category by max count
    counts = {'Sports': sports_count, 'Business': business_count, 'World': world_count, 'Science/Technology': science_count}
    category = max(counts, key=counts.get)
    # require that chosen category has at least one keyword match
    if counts[category] == 0:
        category = None
    r['__category'] = category
    r['__counts'] = counts
    if category == 'Sports':
        candidates.append(r)

if candidates:
    # pick one with longest description
    chosen = max(candidates, key=lambda x: len(x.get('description') or ''))
    result = chosen.get('title')
else:
    result = None

# prepare printable JSON-serializable string
out = result if result is not None else 'No sports articles found'
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_MxLHbXI7sU5fe0YBJVHVJ3L6': [{'_id': '6959849ca7b209977a4322c5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959849ca7b209977a4322c6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959849ca7b209977a4322c7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959849ca7b209977a4322c8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959849ca7b209977a4322c9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

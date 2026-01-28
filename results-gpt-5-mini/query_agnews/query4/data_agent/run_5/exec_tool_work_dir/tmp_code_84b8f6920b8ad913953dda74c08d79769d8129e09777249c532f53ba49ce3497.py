code = """import json
from collections import Counter

# Load metadata 2015 records from previous query result path
meta_path = var_call_fOQSuxuaXAf1pWrPhROahiqT
with open(meta_path, 'r') as f:
    meta = json.load(f)

# Load full articles from MongoDB query file
articles_path = var_call_NbAzKdKAr6hgyNfwphTVWbW1
with open(articles_path, 'r') as f:
    articles = json.load(f)

# build mapping from article_id (int) to text
article_text = {}
for a in articles:
    aid = a.get('article_id')
    if aid is None:
        continue
    try:
        aid_i = int(str(aid).strip())
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    article_text[aid_i] = (title + ' ' + desc).lower()

# define keywords
world_kw = ["president","election","minister","government","war","attack","bomb","killed","dead","protest","diplomat","border","u.n.","united nations","refugee","iraq","syria","iran","china","russia","terror","ceasefire","military","sanction","embassy","parliament","prime minister","conflict","peace","clashes","soldier","voted","election","elections","presidential","president", "reuters", "ap -", "breaking"]
SPORTS_KW = ["game","match","season","goal","scored","tournament","championship","fifa","olympic","coach","player","score","victory","defeat","league","pitch","bat","basketball","soccer","football","tennis","cricket","boxing","golf","race","runner","goalkeeper","striker","win","lost","defeated"]
BUSINESS_KW = ["stock","market","shares","ipo","firm","investment","economy","bank","financial","revenue","profit","loss","merger","acquisition","earnings","oil","crude","economy","inflation","fed","interest rate","interest rates"]
SCI_KW = ["technology","scientist","research","scientific","nasa","space","robot","software","computer","internet","phone","tech","study","researchers","scientists","biology","chemistry","physics","discovery","medical","disease","clinical","research study"]

# classification function
def classify(text):
    scores = {"World":0, "Sports":0, "Business":0, "Science/Technology":0}
    for kw in world_kw:
        if kw in text:
            scores['World'] += 1
    for kw in SPORTS_KW:
        if kw in text:
            scores['Sports'] += 1
    for kw in BUSINESS_KW:
        if kw in text:
            scores['Business'] += 1
    for kw in SCI_KW:
        if kw in text:
            scores['Science/Technology'] += 1
    # choose max
    if sum(scores.values()) == 0:
        return 'World'
    return max(scores.items(), key=lambda x: x[1])[0]

# Count world articles by region for 2015 metadata
region_counts = Counter()
not_found = 0
for rec in meta:
    try:
        aid = int(str(rec.get('article_id')).strip())
    except:
        continue
    region = rec.get('region')
    text = article_text.get(aid)
    if text is None:
        not_found += 1
        continue
    cat = classify(text)
    if cat == 'World':
        region_counts[region] += 1

# find region with max
if region_counts:
    top_region, top_count = region_counts.most_common(1)[0]
else:
    top_region, top_count = None, 0

output = {"region": top_region, "count": top_count, "breakdown": dict(region_counts), "not_found": not_found}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_fOQSuxuaXAf1pWrPhROahiqT': 'file_storage/call_fOQSuxuaXAf1pWrPhROahiqT.json', 'var_call_n302qwLZtBlSYUbzuQtZ02zC': 'file_storage/call_n302qwLZtBlSYUbzuQtZ02zC.json', 'var_call_ksGnXaxvEiv9KRgWVrhOqYMB': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_8sZoHyHiWjQCUVxKXgavouTb': {'region': None, 'count': 0, 'breakdown': {}}, 'var_call_NbAzKdKAr6hgyNfwphTVWbW1': 'file_storage/call_NbAzKdKAr6hgyNfwphTVWbW1.json'}

exec(code, env_args)

code = """import json
from collections import Counter

# Load metadata 2015 records from file path variable
meta_path = var_call_uhQeRuiHYv64OeMnsHMjVwST
with open(meta_path, 'r') as f:
    meta2015 = json.load(f)

# Load articles list variable
articles = var_call_YaNxlXQuU2itwNfMIHtzuSc6

# Build mapping article_id (int) -> combined text
article_text = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    article_text[aid] = (title + ' ' + desc).lower()

# Define keyword lists
world_kw = ['president','election','government','conflict','war','attack','killed','protest','summit','un','international','diplomat','ceasefire','terror','refugee','negotiat','minister','border','expel','sanction']
sports_kw = ['football','soccer','match','tournament','league','goal','olympic','nba','mlb','nfl','rugby','cricket','tennis','win','defeat','coach','player','season','score','cup']
business_kw = ['market','stocks','economy','business','firm','company','invest','investment','trade','merger','acquisition','revenue','bank','banking','oil','economy','stock']
science_kw = ['technology','scientist','research','scientific','nasa','space','software','computer','internet','tech','study','science','cell','robot','ai','artificial intelligence','gadget','physics','biology']

# Function to score categories
def score_text(text, kws):
    s = 0
    for kw in kws:
        if kw in text:
            s += text.count(kw)
    return s

# Classify metadata records
region_world_counts = Counter()
missed = 0
for rec in meta2015:
    try:
        aid = int(rec.get('article_id'))
    except:
        continue
    region = rec.get('region') or 'Unknown'
    text = article_text.get(aid)
    if text is None:
        missed += 1
        continue
    # compute scores
    scores = {
        'World': score_text(text, world_kw),
        'Sports': score_text(text, sports_kw),
        'Business': score_text(text, business_kw),
        'Science/Technology': score_text(text, science_kw)
    }
    # if all zero, attempt simple heuristic: presence of Reuters/AFP etc -> Business if contains market/stocks else World default
    if all(v == 0 for v in scores.values()):
        # fallback: look for business words
        if any(kw in text for kw in business_kw):
            chosen = 'Business'
        else:
            chosen = 'World'
    else:
        # choose max score; tie-break by priority World, Sports, Business, Science/Technology
        maxscore = max(scores.values())
        candidates = [k for k,v in scores.items() if v == maxscore]
        priority = ['World','Sports','Business','Science/Technology']
        for p in priority:
            if p in candidates:
                chosen = p
                break
    if chosen == 'World':
        region_world_counts[region] += 1

# Determine region with maximum count
if region_world_counts:
    max_region, max_count = region_world_counts.most_common(1)[0]
else:
    max_region, max_count = None, 0

result = {'region': max_region, 'count': max_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uhQeRuiHYv64OeMnsHMjVwST': 'file_storage/call_uhQeRuiHYv64OeMnsHMjVwST.json', 'var_call_pmlog0QfCdhKZYQG6i1DJQ6o': 'file_storage/call_pmlog0QfCdhKZYQG6i1DJQ6o.json', 'var_call_YaNxlXQuU2itwNfMIHtzuSc6': [{'_id': '6959aaa5dd937f5045d1ed74', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959aaa5dd937f5045d1ed75', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959aaa5dd937f5045d1ed76', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959aaa5dd937f5045d1ed77', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959aaa5dd937f5045d1ed78', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

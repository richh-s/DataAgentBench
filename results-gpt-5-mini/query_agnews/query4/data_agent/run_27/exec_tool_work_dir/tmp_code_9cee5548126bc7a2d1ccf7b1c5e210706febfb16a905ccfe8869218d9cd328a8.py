code = """import json, re
# Load metadata (file path stored in var_call_omp3ddExYwoslFqB4uKYS5tq)
meta_path = var_call_omp3ddExYwoslFqB4uKYS5tq
with open(meta_path, 'r') as f:
    meta = json.load(f)

# Articles list is available directly
articles = var_call_fQhii1PVu53kRkgR2E8jKubt

# Build mapping article_id -> region for 2015
meta_map = {int(item['article_id']): item['region'] for item in meta}

# Build mapping article_id -> combined text
article_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    article_map[aid] = (title + ' ' + desc).lower()

# Keyword sets
sports_kw = ['football','soccer','world cup','match','tournament','season','goal','coach','player','nba','mlb','nfl','olympic','olympics','cup','race','athlete','score','bat','inning','goalkeeper']
business_kw = ['stock','stocks','market','economy','invest','firm','company','shares','bank','trading','billion','million','merger','acquisition','ipo','ceo','cfo','economy','profit','loss']
science_kw = ['scientist','study','research','nasa','space','technology','tech','scientific','robot','software','internet','ai','machine learning','chemical','physics','biology','experiment','study finds']

# helper
def contains_any(text, kws):
    for kw in kws:
        if kw in text:
            return True
    return False

# Classify and count World articles by region
counts_by_region = {}
for aid, region in meta_map.items():
    text = article_map.get(aid)
    if not text:
        continue
    if contains_any(text, sports_kw):
        cat = 'Sports'
    elif contains_any(text, business_kw):
        cat = 'Business'
    elif contains_any(text, science_kw):
        cat = 'Science/Technology'
    else:
        cat = 'World'
    if cat == 'World':
        counts_by_region[region] = counts_by_region.get(region, 0) + 1

if counts_by_region:
    max_count = max(counts_by_region.values())
    winners = sorted([r for r,c in counts_by_region.items() if c == max_count])
else:
    max_count = 0
    winners = []

result = {'counts': counts_by_region, 'winners': winners, 'top_count': max_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_omp3ddExYwoslFqB4uKYS5tq': 'file_storage/call_omp3ddExYwoslFqB4uKYS5tq.json', 'var_call_McgbruQEYnesqaAWqZD3e4b2': 'file_storage/call_McgbruQEYnesqaAWqZD3e4b2.json', 'var_call_fQhii1PVu53kRkgR2E8jKubt': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

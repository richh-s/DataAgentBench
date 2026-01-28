code = """import json, re
# Load metadata (2015 records) from file path variable
meta_path = var_call_bqG3p4Xgp7PyD8VJ6yZy1zuT
with open(meta_path, 'r') as f:
    metadata = json.load(f)
# Load articles list from var_call_1S7GdAIoABWsmP6yuw4I0k7I
articles = var_call_1S7GdAIoABWsmP6yuw4I0k7I
# Build article map
article_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title','') or ''
    desc = a.get('description','') or ''
    article_map[aid] = {'title': title, 'description': desc, 'text': (title+' '+desc).lower()}

# keyword sets
world_kw = [
    'president','election','government','minister','rebel','attack','killed','died','siege','crisis','protest','bomb','refugee','war','security','diplomat','diplomatic','border','united nations','un ','military','parliament','coup','sanction','embassy'
]
# include country/region names for world signal
world_kw += ['iraq','syria','iran','afghanistan','russia','china','europe','asia','africa','north america','south america','venezuela','uk','britain','germany','france','spain','italy']

business_kw = [
    'market','stock','stocks','shares','economy','economies','oil prices','oil','financial','bank','banks','investment','investor','investors','company','companies','merger','acquisition','revenue','profits','profit','business','firm','carlyle','wall street','short-sellers','dow','nasdaq'
]

sports_kw = [
    'match','season','win','wins','defeat','defeated','goal','goals','score','scored','league','cup','tournament','coach','player','players','football','soccer','basketball','baseball','cricket','olympic','olympics','fifa','nfl','nba','mlb','penalty'
]

sci_kw = [
    'technology','scientist','research','study','scientific','nasa','space','robot','software','internet','mobile','tech','engineering','laboratory','chip','ai','artificial intelligence','scientists','discovery'
]

# function to compute score
def score_text(text, keywords):
    s = 0
    for kw in keywords:
        # count word occurrences with simple substring match
        s += text.count(kw)
    return s

# classify each metadata entry
from collections import defaultdict
region_world_counts = defaultdict(int)
classified_counts = defaultdict(int)

for item in metadata:
    try:
        aid = int(item.get('article_id'))
    except:
        continue
    region = item.get('region') or 'Unknown'
    art = article_map.get(aid)
    text = ''
    if art:
        text = art['text']
    else:
        # if article text missing, fall back to empty
        text = ''
    # compute scores
    s_world = score_text(text, world_kw)
    s_business = score_text(text, business_kw)
    s_sports = score_text(text, sports_kw)
    s_sci = score_text(text, sci_kw)
    scores = {'World': s_world, 'Business': s_business, 'Sports': s_sports, 'Science/Technology': s_sci}
    # choose highest score; if all zero, attempt to use simple heuristics: look for country words -> World, else Business
    best_cat = max(scores, key=lambda k: scores[k])
    if scores[best_cat] == 0:
        # fallback: if any country/region word appears, World
        if any(w in text for w in ['iraq','syria','china','russia','afghanistan','europe','asia','africa','north america','south america','venezuela','uk','britain','germany']):
            best_cat = 'World'
        else:
            # fallback to Business
            best_cat = 'Business'
    # increment
    classified_counts[best_cat] += 1
    if best_cat == 'World':
        region_world_counts[region] += 1

# find max region(s)
if region_world_counts:
    max_count = max(region_world_counts.values())
    top_regions = [r for r,c in region_world_counts.items() if c==max_count]
else:
    max_count = 0
    top_regions = []

result = {'top_regions': top_regions, 'max_count': max_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OkEHZh9DF3cWuFn5tW0QpXox': ['articles'], 'var_call_bqG3p4Xgp7PyD8VJ6yZy1zuT': 'file_storage/call_bqG3p4Xgp7PyD8VJ6yZy1zuT.json', 'var_call_w6XrTEw7BARUFt2WYri8b7hs': 'file_storage/call_w6XrTEw7BARUFt2WYri8b7hs.json', 'var_call_1S7GdAIoABWsmP6yuw4I0k7I': [{'_id': '6959a8b7b1a41abdc80f31b3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a8b7b1a41abdc80f31b4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a8b7b1a41abdc80f31b5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a8b7b1a41abdc80f31b6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a8b7b1a41abdc80f31b7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

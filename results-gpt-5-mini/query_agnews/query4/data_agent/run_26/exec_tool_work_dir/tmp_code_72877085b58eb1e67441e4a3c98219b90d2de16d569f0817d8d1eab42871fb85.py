code = """import json, re
# Load metadata and full articles
meta_path = var_call_bqG3p4Xgp7PyD8VJ6yZy1zuT
arts_path = var_call_lFR40Rca8YsmLaKxRGUL36GA
with open(meta_path,'r') as f:
    metadata = json.load(f)
with open(arts_path,'r') as f:
    articles = json.load(f)

# build article map
article_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = (a.get('title') or '').strip()
    desc = (a.get('description') or '').strip()
    text = (title + ' ' + desc).lower()
    article_map[aid] = {'title': title, 'description': desc, 'text': text}

# keyword lists
world_terms = ['president','prime minister','election','government','minister','rebel','rebels','attack','attacked','killed','died','siege','crisis','protest','protests','bomb','refugee','war','security','diplomat','diplomatic','border','united nations','military','parliament','coup','sanction','embassy','ceasefire','insurgency']
country_terms = ['iraq','syria','iran','afghanistan','russia','china','india','pakistan','israel','palestine','egypt','libya','tunisia','algeria','morocco','south africa','kenya','nigeria','somalia','ukraine','uk','britain','germany','france','spain','italy','europe','asia','africa','north america','south america','venezuela','brazil','argentina','colombia','mexico']
# business and sports/sci for tie-breaking
business_terms = ['market','stock','stocks','shares','economy','economies','oil prices','oil','financial','bank','banks','investment','investor','company','companies','merger','acquisition','revenue','profits','profit','business','firm','wall street','dollar','fed','unemployment']
sports_terms = ['match','season','win','wins','defeat','defeated','goal','goals','score','scored','league','cup','tournament','coach','player','players','football','soccer','basketball','baseball','cricket','olympic','olympics','fifa']
sci_terms = ['technology','scientist','research','study','scientific','nasa','space','robot','software','internet','tech','ai','artificial intelligence']

# helper
def contains_any(text, terms):
    for t in terms:
        if re.search(r'\b' + re.escape(t) + r'\b', text):
            return True
    return False

from collections import defaultdict
region_world_counts = defaultdict(int)
region_total_counts = defaultdict(int)
classified_counts = defaultdict(int)

for item in metadata:
    try:
        aid = int(item.get('article_id'))
    except:
        continue
    region = item.get('region') or 'Unknown'
    region_total_counts[region] += 1
    art = article_map.get(aid)
    text = art['text'] if art else ''
    # classify
    is_world = False
    if contains_any(text, world_terms) or contains_any(text, country_terms):
        is_world = True
    else:
        # if title starts with location (e.g., 'WASHINGTON/NEW YORK') pattern
        if art and re.search(r'^[A-Z\- ]{2,20}\(', art['title']):
            is_world = True
    if is_world:
        classified = 'World'
        region_world_counts[region] += 1
    else:
        # check business
        if contains_any(text, business_terms):
            classified = 'Business'
        elif contains_any(text, sports_terms):
            classified = 'Sports'
        elif contains_any(text, sci_terms):
            classified = 'Science/Technology'
        else:
            classified = 'Business'
    classified_counts[classified] += 1

# compute top region(s)
if region_world_counts:
    max_count = max(region_world_counts.values())
    top_regions = [r for r,c in region_world_counts.items() if c==max_count]
else:
    max_count = 0
    top_regions = []
# prepare region counts sorted
region_counts_sorted = dict(sorted(region_world_counts.items(), key=lambda x: x[1], reverse=True))
result = {'top_regions': top_regions, 'max_count': max_count, 'region_counts': region_counts_sorted, 'classified_totals': dict(classified_counts)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OkEHZh9DF3cWuFn5tW0QpXox': ['articles'], 'var_call_bqG3p4Xgp7PyD8VJ6yZy1zuT': 'file_storage/call_bqG3p4Xgp7PyD8VJ6yZy1zuT.json', 'var_call_w6XrTEw7BARUFt2WYri8b7hs': 'file_storage/call_w6XrTEw7BARUFt2WYri8b7hs.json', 'var_call_1S7GdAIoABWsmP6yuw4I0k7I': [{'_id': '6959a8b7b1a41abdc80f31b3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a8b7b1a41abdc80f31b4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a8b7b1a41abdc80f31b5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a8b7b1a41abdc80f31b6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a8b7b1a41abdc80f31b7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_OAaM3dVyYxDRFrESEqlcJYjz': {'top_regions': [], 'max_count': 0}, 'var_call_ltEZjPhfuEwHslXZ0tUf6Hlq': {'classified_counts_sample500': {'Business': 500}, 'region_world_counts_sample500': {}, 'examples': []}, 'var_call_lFR40Rca8YsmLaKxRGUL36GA': 'file_storage/call_lFR40Rca8YsmLaKxRGUL36GA.json'}

exec(code, env_args)

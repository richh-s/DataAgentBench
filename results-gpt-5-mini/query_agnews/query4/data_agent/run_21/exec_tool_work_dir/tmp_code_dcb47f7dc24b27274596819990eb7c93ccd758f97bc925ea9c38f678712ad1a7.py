code = """import json, re
# Load metadata records from 2015 (file path stored in var_call_mdnPRBN1N7wUInnWRo8kyd6d)
meta_path = var_call_mdnPRBN1N7wUInnWRo8kyd6d
with open(meta_path, 'r', encoding='utf-8') as f:
    meta_records = json.load(f)
# Articles list available in var_call_K1kJ6R2kaX6QWlVfbuJ32F5H
articles = var_call_K1kJ6R2kaX6QWlVfbuJ32F5H
# Build article_id -> (title, description) map
art_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    art_map[aid] = (title, desc)

# Keywords for classification
world_kw = ['president','prime minister','minister','government','election','protest','protests','war','attack','bomb','military','soldier','killed','dies','death','dead','refugee','refugees','parliament','ceasefire','border','visa','iraq','syria','russia','china','united states','united kingdom','uk','u.s.','u.s','u.k.','afghanistan','pakistan','north korea','south korea','venezuela','venezeula','venezuela']
sports_kw = ['game','match','goal','score','scored','tournament','coach','season','league','player','players','football','soccer','basketball','nba','mlb','nfl','olympic','world cup','cup final','innings','strike','defeat','victory','pitcher','matchday']
business_kw = ['market','markets','stock','stocks','economy','business','company','companies','firm','investment','investor','earnings','shares','billion','million','trade','bank','oil','crude','wall st','wall-st','short-sellers','short sellers']
tech_kw = ['technology','technolog','scientist','scientists','research','nasa','space','internet','software','apps','apple','google','microsoft','facebook','tech','smartphone','robot','robotics','ai ','artificial intelligence','scientific','study','studies','breakthrough']

# Precompile regexes
def contains_any(text, kw_list):
    for kw in kw_list:
        if kw in text:
            return True
    return False

region_counts = {}
classified_counts = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}

for rec in meta_records:
    try:
        aid = int(rec.get('article_id'))
    except:
        continue
    region = rec.get('region') or 'Unknown'
    title, desc = art_map.get(aid, ('',''))
    text = (title + ' ' + desc).lower()
    cat = None
    # World first
    if contains_any(text, world_kw):
        cat = 'World'
    elif contains_any(text, sports_kw):
        cat = 'Sports'
    elif contains_any(text, tech_kw):
        cat = 'Science/Technology'
    elif contains_any(text, business_kw):
        cat = 'Business'
    else:
        # default: World
        cat = 'World'
    classified_counts[cat] = classified_counts.get(cat,0) + 1
    if cat == 'World':
        region_counts[region] = region_counts.get(region, 0) + 1

# Find region with max world count
if region_counts:
    top_region = max(region_counts.items(), key=lambda x: x[1])[0]
    top_count = region_counts[top_region]
else:
    top_region = None
    top_count = 0

result = {'region_counts': region_counts, 'top_region': top_region, 'top_count': top_count, 'classified_counts': classified_counts}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mdnPRBN1N7wUInnWRo8kyd6d': 'file_storage/call_mdnPRBN1N7wUInnWRo8kyd6d.json', 'var_call_iyStsrWXBlVQr64Cbz6hBq87': 'file_storage/call_iyStsrWXBlVQr64Cbz6hBq87.json', 'var_call_K1kJ6R2kaX6QWlVfbuJ32F5H': [{'_id': '6959a70254bf81ff63bdf099', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a70254bf81ff63bdf09a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a70254bf81ff63bdf09b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a70254bf81ff63bdf09c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a70254bf81ff63bdf09d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

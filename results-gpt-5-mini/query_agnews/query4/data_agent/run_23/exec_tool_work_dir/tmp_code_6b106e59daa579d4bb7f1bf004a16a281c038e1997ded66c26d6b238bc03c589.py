code = """import json
from pathlib import Path
# Load metadata records for 2015
md_path = var_call_s92epc8s6ZPW1a1CQbTAvYyW
with open(md_path, 'r') as f:
    md_records = json.load(f)
# Build mapping article_id -> region
id_to_region = {int(r['article_id']): r['region'] for r in md_records}
# Load articles list
articles = var_call_AWRklRTWDpB9IFy555JHMrbS
# Helper classify
sports_kw = ['match','defeat','defeats','beat','beats','win','wins','won','goal','goals','season','tournament','cup','olympic','fifa','nba','mlb','nfl','soccer','football','cricket','tennis','victory','score','scored','race','grand prix','coach','inning','innings','batting','homered','home run','pitch','penalty']
business_kw = ['stock','stocks','market','markets','economy','economic','bank','banks','share','shares','firm','company','companies','merger','acquisition','earnings','revenue','invest','investor','investors','wall st','wallstreet','oil prices','oil','bonds','fed','central bank']
tech_kw = ['technology','tech','scientist','scientists','nasa','space','research','study','scientific','software','internet','computer','ai','robot','robotics','drone','biotech','mobile','smartphone','app','apple','google','microsoft','facebook','cyber','battery','chip','gps','satellite','laboratory','vaccine']

import re

def contains_kw(text, kwlist):
    for kw in kwlist:
        if kw in text:
            return True
    return False

counts = {}
world_article_ids = []
for art in articles:
    try:
        aid = int(art.get('article_id'))
    except:
        continue
    if aid not in id_to_region:
        continue
    title = (art.get('title') or '')
    desc = (art.get('description') or '')
    text = (title + ' ' + desc).lower()
    category = None
    if contains_kw(text, sports_kw):
        category = 'Sports'
    elif contains_kw(text, business_kw):
        category = 'Business'
    elif contains_kw(text, tech_kw):
        category = 'Science/Technology'
    else:
        category = 'World'
    if category == 'World':
        region = id_to_region[aid]
        counts[region] = counts.get(region, 0) + 1
        world_article_ids.append(aid)

# Determine top region
if counts:
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c==max_count]
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': top_regions,
    'count': max_count,
    'counts': counts,
    'world_article_ids_sample': world_article_ids[:20]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wgMhGs49Dd75ZYDmKjsPgn1N': ['articles'], 'var_call_hqHuuBktfuXB0n5Pqb01qHF7': ['authors', 'article_metadata'], 'var_call_s92epc8s6ZPW1a1CQbTAvYyW': 'file_storage/call_s92epc8s6ZPW1a1CQbTAvYyW.json', 'var_call_MldGj7PyI9Y6W4AQh5xn7lZj': 'file_storage/call_MldGj7PyI9Y6W4AQh5xn7lZj.json', 'var_call_AWRklRTWDpB9IFy555JHMrbS': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json
from collections import Counter

# Load metadata 2015 from file path provided by the query tool
metadata_path = var_call_A3gKlg2KoW0J4hsAL9mcZEA5
with open(metadata_path, 'r', encoding='utf-8') as f:
    metadata_2015 = json.load(f)

# Load articles list from the articles query result variable
articles = var_call_RygEP6h5DzY5egJyAE4FRqBC

# Convert article_id to int for both datasets and build map
for m in metadata_2015:
    try:
        m['article_id'] = int(m['article_id'])
    except:
        pass

for a in articles:
    try:
        a['article_id'] = int(a['article_id'])
    except:
        pass

article_map = {a['article_id']: {'title': a.get('title',''), 'description': a.get('description','')} for a in articles}

# Simple keyword-based classifier for categories
sports_keywords = [
    'football','soccer','match','tournament','goal','nba','mlb','nfl','cricket','olympic','olympics',
    'coach','season','league','world cup','grand prix','tennis','basketball','score','pitcher','fifa','rugby','goalkeeper'
]
business_keywords = [
    'stock','stocks','market','economy','business','invest','investment','shares','bank','financial',
    'earnings','profit','loss','revenue','ceo','cfo','ipo','merger','acquisition','billion','million','wall st','wall street'
]
science_keywords = [
    'research','scientist','study','technology','tech','nasa','space','scientific','science','robot','computer',
    'software','internet','ai','artificial intelligence','algorithm','physics','chemistry','biology','experiment','researchers',
    'startup','smartphone'
]

def classify(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    # check sports
    for kw in sports_keywords:
        if kw in text:
            return 'Sports'
    for kw in business_keywords:
        if kw in text:
            return 'Business'
    for kw in science_keywords:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Merge metadata with article text, classify, and count World by region
world_counts = Counter()
missing_text = 0
for m in metadata_2015:
    aid = m.get('article_id')
    region = m.get('region')
    art = article_map.get(aid)
    if not art:
        missing_text += 1
        # If missing article text, conservatively skip classification
        continue
    cat = classify(art.get('title',''), art.get('description',''))
    if cat == 'World':
        world_counts[region] += 1

# Determine top region(s)
if world_counts:
    max_count = max(world_counts.values())
    top_regions = sorted([r for r,c in world_counts.items() if c == max_count])
else:
    max_count = 0
    top_regions = []

result = {
    'top_regions': top_regions,
    'top_count': max_count,
    'breakdown': dict(world_counts),
    'missing_article_text_entries_skipped': missing_text
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YymsuwkBiR8whn4s5H1PYndc': ['authors', 'article_metadata'], 'var_call_A3gKlg2KoW0J4hsAL9mcZEA5': 'file_storage/call_A3gKlg2KoW0J4hsAL9mcZEA5.json', 'var_call_SIq8xplPzRPYgycSB1juTKih': ['articles'], 'var_call_RygEP6h5DzY5egJyAE4FRqBC': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

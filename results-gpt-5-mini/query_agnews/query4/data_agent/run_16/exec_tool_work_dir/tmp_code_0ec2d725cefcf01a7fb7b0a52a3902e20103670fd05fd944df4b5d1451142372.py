code = """import json
from pathlib import Path
# load metadata from file
meta_path = Path(var_call_SgR6L4G39ERD0I0uBygA9Iie)
with meta_path.open() as f:
    metadata = json.load(f)
# articles list variable
articles = var_call_h9Fc95ybkBuqgDU5tmEqn6Az
# build article text mapping
art_text = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title','') or ''
    desc = a.get('description','') or ''
    art_text[aid] = (title + ' ' + desc).lower()
# keyword lists
sports_kw = ['match','goal','season','coach','scored','beat','defeat','draw','tournament','league','world cup','olympic','fifa','nba','mlb','nfl','rugby','soccer','tennis','cup final','hat-trick','won','loss','victory','penalty','goalkeeper','striker','midfielder','score']
business_kw = ['stocks','market','economy','oil','shares','billion','million','company','firm','investment','bank','finance','dow','nasdaq','reuters - private','private investment','carlyle','earnings','investors']
tech_kw = ['technology','scientist','study','research','nasa','space','tech','software','google','apple','microsoft','robot','ai','artificial intelligence','cyber','startup','gadgets','innovation','scientists','researchers']

def classify(text):
    if not text:
        return 'World'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# count world articles by region for 2015 metadata
from collections import defaultdict
counts = defaultdict(int)
missing = 0
for m in metadata:
    aid = int(m.get('article_id'))
    region = m.get('region')
    text = art_text.get(aid)
    if text is None:
        missing += 1
        continue
    cat = classify(text)
    if cat == 'World':
        counts[region] += 1
# normalize to regular dict
counts = dict(counts)
# find max
if counts:
    max_count = max(counts.values())
    top_regions = sorted([r for r,c in counts.items() if c==max_count])
else:
    max_count = 0
    top_regions = []
output = {'top_regions': top_regions, 'max_count': max_count, 'counts': counts, 'missing_articles_in_articles_collection': missing}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_lWz7iHXHJfUOvbbLTESfglyU': ['articles'], 'var_call_SgR6L4G39ERD0I0uBygA9Iie': 'file_storage/call_SgR6L4G39ERD0I0uBygA9Iie.json', 'var_call_cNGtrlby6RR7Nzw749H8Qw0n': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271]}, 'var_call_h9Fc95ybkBuqgDU5tmEqn6Az': [{'_id': '6959a5f0c1b2c86a659322b2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a5f0c1b2c86a659322b3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a5f0c1b2c86a659322b4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a5f0c1b2c86a659322b5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a5f0c1b2c86a659322b6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

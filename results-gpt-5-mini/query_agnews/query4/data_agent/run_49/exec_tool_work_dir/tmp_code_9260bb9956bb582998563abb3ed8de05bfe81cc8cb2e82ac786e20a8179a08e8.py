code = """import json
# load metadata records from previous SQL query result file
meta_path = var_call_oR48nCoSS3crui4ofOHyzrxU
with open(meta_path, 'r') as f:
    metadata = json.load(f)
# load articles from Mongo query result file
articles_path = var_call_imd0tQkmzeZZB3ZP7rBjGfSb
with open(articles_path, 'r') as f:
    articles = json.load(f)
# build article_id -> text mapping
article_text = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    article_text[aid] = (title + ' ' + desc).lower()
# keyword lists
sports_kw = ['score','goal','match','tournament','season','league','player','coach','football','soccer','basketball','tennis','cricket','inning','innings','home run','touchdown','cup','championship','olympic','fifa','nba','mlb','nfl']
business_kw = ['market','stocks','shares','dow','nasdaq','ftse','economy','investment','investor','profit','loss','bank','revenue','earnings','ipo','merger','acquisition','trade deficit','bond','inflation','interest rate','opec','oil price','oil','company','business','commercial','economic']
science_kw = ['technology','tech','scientist','research','study','space','nasa','scientific','software','computer','internet','ai','robot','science','device','innovation','satellite','physics','chemistry','biology','genetic','robotics','biotech']

def classify(text):
    if not text:
        return 'World'
    # check sports
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in science_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# count per region for 2015 and world category
from collections import Counter
region_counts = Counter()
world_article_ids = []
for m in metadata:
    try:
        aid = int(m.get('article_id'))
    except:
        continue
    region = m.get('region')
    text = article_text.get(aid, '')
    cat = classify(text)
    if cat == 'World':
        region_counts[region] += 1
        world_article_ids.append(aid)

if region_counts:
    top_region, top_count = region_counts.most_common(1)[0]
else:
    top_region, top_count = None, 0

result = {'top_region': top_region, 'count': top_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_qMiNgwVc36YZfdlB2I4IxgdJ': ['articles'], 'var_call_BvZHzmfCGDz0iOEWZLcI26cH': ['authors', 'article_metadata'], 'var_call_oR48nCoSS3crui4ofOHyzrxU': 'file_storage/call_oR48nCoSS3crui4ofOHyzrxU.json', 'var_call_05bFVhHO5OzvBfJjOTRKoOFF': 'file_storage/call_05bFVhHO5OzvBfJjOTRKoOFF.json', 'var_call_imd0tQkmzeZZB3ZP7rBjGfSb': 'file_storage/call_imd0tQkmzeZZB3ZP7rBjGfSb.json'}

exec(code, env_args)

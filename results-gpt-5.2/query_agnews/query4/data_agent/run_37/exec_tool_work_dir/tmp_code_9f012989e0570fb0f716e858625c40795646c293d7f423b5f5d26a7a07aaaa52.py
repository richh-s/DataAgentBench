code = """import json, pandas as pd

# load 2015 metadata rows
path = var_call_SsrtNrU5YEv5reKQ65A55cPa
with open(path, 'r') as f:
    meta = json.load(f)

# build list of article_ids (ints)
article_ids = sorted({int(r['article_id']) for r in meta})

# keyword-based classifier for categories
world_kw = {
    'war','wars','conflict','ceasefire','refugee','refugees','migrant','migrants','asylum','border','borders','election','elections','vote','parliament','president','prime minister','government','cabinet',
    'diplomat','diplomacy','sanction','sanctions','un','u.n.','united nations','nato','treaty','summit','coup','protest','protests','terror','terrorist','terrorism','isis','islamic state','taliban','al qaeda','bomb','bombing','attack','attacks','militant','militants','hostage',
    'earthquake','tsunami','cyclone','typhoon','flood','floods','hurricane','drought','outbreak','ebola','zika','cholera','pope','vatican','royal','king','queen','monarch',
    'country','embassy'
}
sports_kw = {'game','games','match','matches','tournament','league','cup','olympic','olympics','nba','nfl','mlb','nhl','fifa','uefa','soccer','football','basketball','baseball','hockey','tennis','golf','cricket','rugby','coach','player','players','team','teams','season','championship','final','score','win','wins','lost','victory'}
business_kw = {'stock','stocks','market','markets','economy','economic','trade','deal','merger','acquisition','ipo','earnings','revenue','profit','loss','bank','banks','oil','gas','currency','dollar','euro','yen','inflation','interest rate','rates','unemployment','jobs','company','companies','startup','start-up','ceo','investor','investors','fund','funds'}
science_kw = {'science','scientist','research','study','studies','space','nasa','spacex','rocket','satellite','mars','planet','telescope','physics','chemistry','biology','genetic','genome','dna','climate','temperature','carbon','emissions','technology','tech','software','app','apps','internet','cyber','robot','ai','artificial intelligence','quantum','vaccine','medical','medicine','health','disease'}

def categorize(text: str) -> str:
    t = (text or '').lower()
    scores = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for kw in world_kw:
        if kw in t:
            scores['World'] += 1
    for kw in sports_kw:
        if kw in t:
            scores['Sports'] += 1
    for kw in business_kw:
        if kw in t:
            scores['Business'] += 1
    for kw in science_kw:
        if kw in t:
            scores['Science/Technology'] += 1
    # choose max; default World if all zero (general news)
    best = max(scores.items(), key=lambda x: x[1])
    if best[1] == 0:
        return 'World'
    return best[0]

# map article_id -> region
region_by_id = {int(r['article_id']): r['region'] for r in meta}

# query Mongo in chunks via query_db results are not available here; so instead compute list for later tool call
# We'll just output article_ids list and region map size summary for next step
out = {'n_2015_articles': len(article_ids), 'min_id': min(article_ids) if article_ids else None, 'max_id': max(article_ids) if article_ids else None, 'article_ids': article_ids}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SsrtNrU5YEv5reKQ65A55cPa': 'file_storage/call_SsrtNrU5YEv5reKQ65A55cPa.json'}

exec(code, env_args)

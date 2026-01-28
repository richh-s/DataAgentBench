code = """import json, pandas as pd

# load metadata 2015 from file
path = var_call_U3ia6z8a8k18x4ZeAEc7wavj
with open(path, 'r') as f:
    meta = json.load(f)

df_meta = pd.DataFrame(meta)
# ensure int ids

df_meta['article_id'] = df_meta['article_id'].astype(int)
article_ids = df_meta['article_id'].tolist()

# keyword-based classifier
world_kw = [
    'world','international','global','united nations','u.n.','un ','nato','eu ','european union',
    'diplom','treaty','sanction','summit','minister','president','parliament','election',
    'war','conflict','attack','bomb','terror','militant','isis','islamic state','taliban','al-qaeda',
    'refugee','migrant','border','embassy','coup','protest','ceasefire','hostage','nuclear',
    'syria','iraq','iran','yemen','afghanistan','pakistan','india','china','russia','ukraine',
    'north korea','south korea','japan','gaza','israel','palestin','turkey','saudi','egypt','libya',
    'sudan','somalia','nigeria','kenya','ethiopia','south africa','mexico','brazil','venezuela','colombia',
    'france','germany','italy','spain','greece','britain','uk ','london','eurozone'
]
sports_kw = ['game','match','season','league','tournament','cup','olympic','nba','nfl','mlb','nhl','fifa','uefa','soccer','football','basketball','baseball','hockey','tennis','golf','cricket','coach','player','score','win','loss','draw','final']
business_kw = ['stock','market','shares','earnings','revenue','profit','bank','central bank','fed','inflation','oil','gas','price','economy','economic','gdp','unemployment','trade','deal','merger','acquisition','ipo','company','corporate','ceo','startup','investment','investor','tax','budget','currency','dollar','euro','yuan']
science_kw = ['science','scientist','research','study','technology','tech','ai','artificial intelligence','robot','space','nasa','mars','satellite','rocket','physics','chemistry','biology','genome','medical','medicine','health','disease','virus','climate','weather','earthquake','energy','battery','quantum','internet','software','hardware','cyber','security','hacker']

def score_text(text, kws):
    t = (text or '').lower()
    return sum(1 for kw in kws if kw in t)

def classify(title, desc):
    text = f"{title or ''} {desc or ''}".lower()
    scores = {
        'World': score_text(text, world_kw),
        'Sports': score_text(text, sports_kw),
        'Business': score_text(text, business_kw),
        'Science/Technology': score_text(text, science_kw),
    }
    # pick max; require >0 else None
    cat = max(scores, key=scores.get)
    if scores[cat] == 0:
        return None
    return cat

# process in chunks for mongo $in
from math import ceil
chunksize = 800
records = []
for i in range(0, len(article_ids), chunksize):
    chunk = article_ids[i:i+chunksize]
    q = {
        "collection": "articles",
        "filter": {"article_id": {"$in": chunk}},
        "projection": {"_id": 0, "article_id": 1, "title": 1, "description": 1},
        "limit": len(chunk)
    }
    res = __import__('builtins').query_db("articles_database", json.dumps(q))
    # tool not available inside python; fallback: load via storage? 
    
print('__RESULT__:')
print(json.dumps({'error':'Cannot query_db inside execute_python per tool constraints'}))"""

env_args = {'var_call_U3ia6z8a8k18x4ZeAEc7wavj': 'file_storage/call_U3ia6z8a8k18x4ZeAEc7wavj.json'}

exec(code, env_args)

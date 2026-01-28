code = """import json, pandas as pd

# load full metadata result
path = var_call_cMidJvjQSwFJtWABub9NtQh6
with open(path, 'r', encoding='utf-8') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# fetch article texts from Mongo in manageable chunks
ids = meta_df['article_id'].dropna().unique().tolist()
chunk_size = 800
chunks = [ids[i:i+chunk_size] for i in range(0, len(ids), chunk_size)]

import re

def mongo_find(ids_chunk):
    q = {
        "collection": "articles",
        "filter": {"article_id": {"$in": ids_chunk}},
        "projection": {"_id": 0, "article_id": 1, "title": 1, "description": 1},
        "limit": len(ids_chunk)
    }
    return q

# simple keyword-based classifier
world_kw = [
    'president','prime minister','parliament','election','vote','cabinet','minister','government','diplomat','diplomatic',
    'iran','iraq','syria','israel','palestinian','gaza','ukraine','russia','moscow','putin','china','beijing','north korea','pyongyang',
    'united nations','u.n.','nato','eu','european union','summit','sanctions','refugee','migrant','immigration','border',
    'terror','isis','islamic state','taliban','militant','bomb','attack','ceasefire','coup'
]
sports_kw = ['match','game','season','league','tournament','coach','player','goal','nba','nfl','mlb','nhl','fifa','olympic','tennis','cricket','soccer','football','basketball','baseball','hockey','golf']
business_kw = ['stocks','shares','market','earnings','revenue','profit','merger','acquisition','ipo','bank','fed','inflation','oil','prices','trade','tariff','economy','economic','company','ceo']
science_kw = ['research','study','scientist','space','nasa','mars','rocket','climate','carbon','genome','dna','robot','technology','tech','software','app','internet','ai','artificial intelligence']

def classify(text):
    t = (text or '').lower()
    def score(kws):
        s=0
        for kw in kws:
            if kw in t:
                s+=1
        return s
    scores = {
        'World': score(world_kw),
        'Sports': score(sports_kw),
        'Business': score(business_kw),
        'Science/Technology': score(science_kw)
    }
    # pick max; if all zero, default World? better: unknown -> World not counted
    best = max(scores, key=scores.get)
    if scores[best]==0:
        return None
    return best

from functions import query_db

article_rows = []
for ch in chunks:
    q = json.dumps(mongo_find(ch))
    res = query_db({"db_name":"articles_database","query": q})
    article_rows.extend(res)

art_df = pd.DataFrame(article_rows)
if not art_df.empty:
    art_df['article_id'] = art_df['article_id'].astype(int)
    art_df['text'] = (art_df['title'].fillna('') + ' ' + art_df['description'].fillna('')).str.strip()
    art_df['category'] = art_df['text'].apply(classify)

merged = meta_df.merge(art_df[['article_id','category']], on='article_id', how='left')
world = merged[merged['category']=='World']
counts = world.groupby('region').size().sort_values(ascending=False)

ans = None
if len(counts)>0:
    ans = {"region": counts.index[0], "world_articles": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_cMidJvjQSwFJtWABub9NtQh6': 'file_storage/call_cMidJvjQSwFJtWABub9NtQh6.json'}

exec(code, env_args)

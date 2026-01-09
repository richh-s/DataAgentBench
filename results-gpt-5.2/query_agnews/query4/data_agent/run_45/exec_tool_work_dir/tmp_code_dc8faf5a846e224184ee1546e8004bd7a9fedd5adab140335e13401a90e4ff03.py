code = """import json, pandas as pd

# load metadata 2015
meta_src = var_call_S2zV2vzRp3LnoMz27TpsHt6m
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

art_src = var_call_OFqOCiGTtFMKAZomYGVu7kDz
if isinstance(art_src, str):
    with open(art_src, 'r') as f:
        arts = json.load(f)
else:
    arts = art_src

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = pd.to_numeric(meta_df['article_id'], errors='coerce')
arts_df['article_id'] = pd.to_numeric(arts_df['article_id'], errors='coerce')

# join
df = meta_df.merge(arts_df, on='article_id', how='left')

def categorize(title, desc):
    t = (title or '').lower()
    d = (desc or '').lower()
    text = t + ' ' + d
    sci = ['science','scientist','research','nasa','space','mars','telescope','quantum','genome','dna','protein','medical','medicine','health','biotech','technology','tech','software','internet','computer','ai','robot','iphone','android','google','microsoft','apple','startup','cyber','hack','semiconductor']
    sports = ['sport','sports','nba','nfl','mlb','nhl','soccer','football','fifa','uefa','cricket','tennis','golf','olympic','olympics','formula','grand prix','nascar','race','boxing','ufc','wwe','athlete','tournament','match','league','cup','coach','vs.','won','defeated']
    biz = ['stock','stocks','wall st','wall street','market','markets','earnings','profit','revenue','ipo','shares','bond','bonds','oil','opec','crude','dollar','euro','yen','inflation','gdp','economy','economic','trade','deficit','bank','banks','central bank','interest rate','imf','merger','acquisition','company','companies','retail','fund','funds']
    world = ['iraq','iran','syria','israel','palest','gaza','ukraine','russia','china','japan','korea','afghanistan','pakistan','india','france','germany','uk','britain','england','europe','africa','asia','latin america','south america','north korea','un','united nations','nato','election','president','minister','government','parliament','rebels','military','war','conflict','attack','bomb','killed','refugee','diplomat','summit','sanction','protest']

    def score(keywords):
        s=0
        for kw in keywords:
            if kw in text:
                s += 1
        return s

    scores = {
        'Science/Technology': score(sci),
        'Sports': score(sports),
        'Business': score(biz),
        'World': score(world)
    }
    # tie-breaker preference: if world score >0 and >= others, pick world; else max
    max_score = max(scores.values())
    # if all zero, default World (most general)
    if max_score == 0:
        return 'World'
    # if tie including World and World has max_score, choose World
    tied = [k for k,v in scores.items() if v==max_score]
    if 'World' in tied:
        return 'World'
    return tied[0]

df['category'] = [categorize(t,d) for t,d in zip(df.get('title'), df.get('description'))]

world_df = df[df['category']=='World']
counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)

# pick top region
if len(counts)==0:
    top_region = None
else:
    top_region = counts.index[0]

out = {
    'top_region': None if top_region is None or (isinstance(top_region,float) and pd.isna(top_region)) else str(top_region),
    'top_count': int(counts.iloc[0]) if len(counts)>0 else 0,
    'counts_by_region': {str(k): int(v) for k,v in counts.to_dict().items()}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_S2zV2vzRp3LnoMz27TpsHt6m': 'file_storage/call_S2zV2vzRp3LnoMz27TpsHt6m.json', 'var_call_OFqOCiGTtFMKAZomYGVu7kDz': 'file_storage/call_OFqOCiGTtFMKAZomYGVu7kDz.json'}

exec(code, env_args)

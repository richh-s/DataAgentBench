code = """import json, pandas as pd

# Load metadata 2015
meta_src = var_call_wzLTSqGvAZqDXS3bzArgSO9G
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(str)

# Load articles
art_src = var_call_311RHzEvzc4vzNX83cpJsBe0
if isinstance(art_src, str):
    with open(art_src, 'r') as f:
        arts = json.load(f)
else:
    arts = art_src
art_df = pd.DataFrame(arts)
art_df['article_id'] = art_df['article_id'].astype(str)

# Join to get text for 2015 articles only
joined = meta_df.merge(art_df, on='article_id', how='inner')
joined['text'] = (joined['title'].fillna('') + ' ' + joined['description'].fillna('')).str.lower()

# Simple keyword-based categorization
world_kw = [
    'iraq','iran','syria','israel','palestin','gaza','russia','ukraine','crimea','putin',
    'china','beijing','hong kong','taiwan','japan','tokyo','korea','seoul','pyongyang',
    'india','pakistan','afghanistan','taliban','nato','european union','eu ','brussels',
    'united nations','u.n.','un ','ban ki-moon','kofi annan','pope','vatican',
    'refugee','migrant','asylum','border','election','president','prime minister',
    'terror','bomb','blast','militant','rebel','ceasefire','war','troops','strike','sanction',
    'earthquake','tsunami','flood','ebola','outbreak','aid','humanitarian','diplomat','embassy'
]

sports_kw = ['game','match','season','tournament','league','nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','world cup','coach','player','score','win','lost','draw']
business_kw = ['stocks','shares','market','ipo','profit','earnings','revenue','oil','crude','inflation','interest rate','fed','opec','bank','dollar','euro','trade deficit','economy','gdp','merger','acquisition','fund','mutual','investor']
science_kw = ['research','scientist','study','space','nasa','mars','telescope','genome','gene','clinical','vaccine','computer','software','internet','google','microsoft','apple','robot','ai','technology','chip','semiconductor']

def score(text, kws):
    s = 0
    for kw in kws:
        if kw in text:
            s += 1
    return s

scores = []
for t in joined['text'].tolist():
    sw = score(t, sports_kw)
    sb = score(t, business_kw)
    ss = score(t, science_kw)
    sww = score(t, world_kw)
    scores.append((sww, sw, sb, ss))

sc_df = pd.DataFrame(scores, columns=['world','sports','business','science'])
joined = pd.concat([joined, sc_df], axis=1)

# Assign category by max score with priority World > Sports > Business > Science in ties
prio = ['world','sports','business','science']
joined['max_score'] = joined[prio].max(axis=1)

def pick(row):
    m = row['max_score']
    if m <= 0:
        return None
    for c in prio:
        if row[c] == m:
            return c

joined['category'] = joined.apply(pick, axis=1)
world_2015 = joined[joined['category']=='world']

region_counts = world_2015.groupby('region').size().sort_values(ascending=False)
if len(region_counts)==0:
    out = {"region": None, "world_articles_2015": 0}
else:
    top_region = region_counts.index[0]
    out = {"region": str(top_region), "world_articles_2015": int(region_counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wzLTSqGvAZqDXS3bzArgSO9G': 'file_storage/call_wzLTSqGvAZqDXS3bzArgSO9G.json', 'var_call_311RHzEvzc4vzNX83cpJsBe0': 'file_storage/call_311RHzEvzc4vzNX83cpJsBe0.json'}

exec(code, env_args)

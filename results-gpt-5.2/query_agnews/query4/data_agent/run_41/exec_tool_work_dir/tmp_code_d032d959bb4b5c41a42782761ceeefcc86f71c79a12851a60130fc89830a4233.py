code = """import json, pandas as pd

def load_if_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

meta = load_if_path(var_call_QGREwgHyHCxoLYqR41CmKL0w)
arts = load_if_path(var_call_GkHDIn8TmesCHbXultTNHMdA)

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# normalize types
for c in ['article_id']:
    if c in df_meta.columns:
        df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce').astype('Int64')
    if c in df_arts.columns:
        df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce').astype('Int64')

df = df_meta.merge(df_arts, on='article_id', how='inner')
df['text'] = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# simple keyword-based categorization
world_kw = [
    'iraq','iran','israel','palestin','gaza','syria','lebanon','jordan','yemen','afghan','pakistan',
    'russia','ukraine','crimea','georgia','chechn','moscow','kremlin',
    'china','beijing','taiwan','hong kong','japan','tokyo','korea','seoul','pyongyang',
    'india','delhi','kashmir','bangladesh','nepal','sri lanka',
    'europe','eu','european union','brussels','uk ','britain','london','france','paris','germany','berlin','italy','rome','spain','madrid','greece','athens','turkey','ankara',
    'africa','nigeria','kenya','south africa','sudan','darfur','somalia','ethiopia','egypt','cairo','libya','tripoli',
    'mexico','canada',
    'un ','united nations','nato','opec','imf','world bank','summit','president','prime minister','parliament','election','protest','rebel','militant','terror','bomb','attack','killed','war','ceasefire','hostage','sanction','diplomat','embassy'
]

sports_kw = ['football','soccer','nba','nfl','mlb','nhl','olympic','tournament','championship','final','coach','match','goal','league','tennis','golf','cricket','formula','f1','racing','player','team','vs.']
science_kw = ['software','internet','web','google','microsoft','apple','iphone','android','facebook','twitter','tesla','nasa','space','mars','satellite','robot','ai','artificial intelligence','chip','semiconductor','biotech','vaccine','virus','genome','research','scientist','laboratory','quantum','cyber','hack']
business_kw = ['stock','wall st','earnings','profit','revenue','ipo','shares','market','economy','economic','inflation','interest rate','fed','central bank','dollar','euro','trade deficit','oil price','crude','opec','imf','bank','fund','merger','acquisition','takeover']

# scoring
for name, kws in [('world', world_kw), ('sports', sports_kw), ('science', science_kw), ('business', business_kw)]:
    df[name+'_score'] = 0
    for kw in kws:
        df[name+'_score'] += df['text'].str.contains(kw, regex=False).astype(int)

# choose category by max score; tie-break priority: world, sports, business, science
scores = df[['world_score','sports_score','business_score','science_score']].to_numpy()
import numpy as np
priority = np.array([0,1,2,3])
maxv = scores.max(axis=1)
# if all zero -> unknown
cat = np.where(maxv==0, 'unknown', '')
# compute argmax with tie-break using priority by subtracting tiny
adj = scores + (np.array([4,3,2,1])*1e-6)  # world highest
arg = adj.argmax(axis=1)
labels = np.array(['world','sports','business','science'])
cat = np.where(maxv==0, 'unknown', labels[arg])
df['category'] = cat

world_df = df[df['category']=='world']
region_counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)

if len(region_counts)==0:
    result = {'region': None, 'world_article_count': 0}
else:
    top_region = region_counts.index[0]
    result = {'region': None if pd.isna(top_region) else str(top_region), 'world_article_count': int(region_counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QGREwgHyHCxoLYqR41CmKL0w': 'file_storage/call_QGREwgHyHCxoLYqR41CmKL0w.json', 'var_call_GkHDIn8TmesCHbXultTNHMdA': 'file_storage/call_GkHDIn8TmesCHbXultTNHMdA.json'}

exec(code, env_args)

code = """import json, pandas as pd

# Load metadata 2015
meta = var_call_1Rb6dwzVISS9YUr6NAOwotYi
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)

arts = var_call_ZQst66ftiOUFr3vFBSqiU1pa
if isinstance(arts, str):
    with open(arts, 'r') as f:
        arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids to int
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# keyword-based classifier for 4 categories
world_kw = [
    'iraq','iran','israel','palestin','gaza','syria','syrian','russia','ukraine','crimea','putin','kremlin',
    'china','beijing','japan','tokyo','korea','seoul','north korea','kim','india','pakistan','afghanistan',
    'taliban','isis','islamic state','militant','terror','bomb','attack','u.n.','un ','united nations','nato',
    'europe','eurozone','germany','france','britain','uk ','london','spain','italy','greece','turkey',
    'africa','nigeria','egypt','libya','sudan','kenya','south africa','congo','somalia',
    'mexico','brazil','argentina','venezuela','colombia','chile',
    'refugee','migrant','immigration','election','president','prime minister','parliament','sanction','diplomat',
    'war','ceasefire','peace talks','protest','coup'
]

sports_kw = ['game','match','tournament','season','league','nba','nfl','mlb','nhl','fifa','uefa','world cup','olympic','olympics',
             'tennis','golf','soccer','football','basketball','baseball','hockey','cricket','formula one','f1','grand prix','coach','player','team']

business_kw = ['stock','stocks','market','shares','ipo','earnings','profit','revenue','economy','economic','trade','deficit','inflation','oil','crude','opec','fed','interest rate','bank','merger','acquisition','company','corporate','dollar','euro','yen','fund','investor','tax','jobs','unemployment','gdp']

sci_kw = ['study','research','scientist','science','technology','tech','computer','software','internet','web','google','microsoft','apple','iphone','android','nasa','space','mars','satellite','genome','dna','health','medical','vaccine','climate','global warming','physics','robot','ai']

def classify(text):
    t = (text or '').lower()
    def hit(kws):
        return any(kw in t for kw in kws)
    # prioritize sports/business/sci over world when clearly indicated
    if hit(sports_kw):
        return 'Sports'
    if hit(business_kw):
        return 'Business'
    if hit(sci_kw):
        return 'Science/Technology'
    if hit(world_kw):
        return 'World'
    return 'World'  # default to World if unclear

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).astype(str)
arts_df['category'] = arts_df['text'].map(classify)

world_ids = set(arts_df.loc[arts_df['category']=='World','article_id'].tolist())

meta_world = meta_df[meta_df['article_id'].isin(world_ids)]
counts = meta_world.groupby('region', dropna=False).size().sort_values(ascending=False)

if len(counts)==0:
    result = {'region': None, 'world_article_count_2015': 0}
else:
    top_region = counts.index[0]
    result = {'region': str(top_region), 'world_article_count_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_1Rb6dwzVISS9YUr6NAOwotYi': 'file_storage/call_1Rb6dwzVISS9YUr6NAOwotYi.json', 'var_call_ZQst66ftiOUFr3vFBSqiU1pa': 'file_storage/call_ZQst66ftiOUFr3vFBSqiU1pa.json'}

exec(code, env_args)

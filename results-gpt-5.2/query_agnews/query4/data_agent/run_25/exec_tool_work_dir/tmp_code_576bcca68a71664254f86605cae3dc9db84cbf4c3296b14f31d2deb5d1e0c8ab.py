code = """import json, pandas as pd

# Load full 2015 metadata rows
p_meta = var_call_tVyKNAFNZHdg9vUVdubEDIBn
if isinstance(p_meta, str):
    with open(p_meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = p_meta

# Load full articles
p_art = var_call_G7JwLepFgS4RpYCWkrZ6VGp8
if isinstance(p_art, str):
    with open(p_art, 'r', encoding='utf-8') as f:
        arts = json.load(f)
else:
    arts = p_art

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)
arts_df['title'] = arts_df['title'].fillna('')
arts_df['description'] = arts_df['description'].fillna('')

# Simple keyword-based categorization
world_kw = [
    'iraq','iran','israel','palestin','gaza','ukraine','russia','putin','kremlin','syrian','syria','assad','turkey','erdogan',
    'china','beijing','xi','japan','tokyo','korea','seoul','north korea','kim','afghanistan','pakistan','india','modi',
    'europe','eu','european','nato','un ','u.n.','united nations','refugee','migrant','election','president','prime minister',
    'parliament','embassy','military','army','missile','bomb','terror','isis','islamic state','al qaeda','taliban',
    'britain','uk ','london','france','paris','germany','merkel','spain','italy','greece',
    'egypt','libya','sudan','nigeria','kenya','somalia','south africa',
    'brazil','argentina','venezuela','mexico','canada','australia','new zealand',
    'pope','vatican'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','baseball','basketball','hockey','world cup']
biz_kw = ['stock','stocks','wall st','wall street','nasdaq','dow','ipo','earnings','profit','revenue','bank','fed','interest rate','opec','oil','crude','economy','economic','inflation','dollar','euro','yen','trade','deficit','market','shares','merger','acquisition']
sci_kw = ['research','scientist','nasa','space','mars','telescope','gene','genetic','dna','virus','vaccine','quantum','robot','ai','artificial intelligence','computer','software','internet','cyber','chip','semiconductor','smartphone','technology','tech','biotech','climate','weather','earthquake']

def categorize(text):
    t = text.lower()
    def has_any(kws):
        return any(kw in t for kw in kws)
    # priority: sports, business, sci/tech, world
    if has_any(sports_kw):
        return 'Sports'
    if has_any(biz_kw):
        return 'Business'
    if has_any(sci_kw):
        return 'Science/Technology'
    if has_any(world_kw):
        return 'World'
    # fallback: World
    return 'World'

arts_df['combined'] = (arts_df['title'].astype(str) + ' ' + arts_df['description'].astype(str))
arts_df['category'] = arts_df['combined'].map(categorize)

joined = meta_df.merge(arts_df[['article_id','category']], on='article_id', how='inner')
world_2015 = joined[joined['category']=='World']
counts = world_2015.groupby('region', dropna=False).size().sort_values(ascending=False)

if len(counts)==0:
    out = {"region": None, "world_articles_2015": 0}
else:
    top_region = counts.index[0]
    out = {"region": str(top_region), "world_articles_2015": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tVyKNAFNZHdg9vUVdubEDIBn': 'file_storage/call_tVyKNAFNZHdg9vUVdubEDIBn.json', 'var_call_G7JwLepFgS4RpYCWkrZ6VGp8': 'file_storage/call_G7JwLepFgS4RpYCWkrZ6VGp8.json'}

exec(code, env_args)

code = """import json, pandas as pd

# Load 2015 metadata
path_meta = var_call_EnlYmeQ9JyDJJ1iUGIgAjHfh
with open(path_meta,'r') as f:
    meta = json.load(f)
df_meta = pd.DataFrame(meta)
# normalize types
if not df_meta.empty:
    df_meta['article_id'] = df_meta['article_id'].astype(int)

# Load articles
path_art = var_call_iVLvqaJxSYKjCCcsDXkkMD2H
with open(path_art,'r') as f:
    arts = json.load(f)
df_art = pd.DataFrame(arts)
if not df_art.empty:
    df_art['article_id'] = df_art['article_id'].astype(int)
    df_art['text'] = (df_art['title'].fillna('') + ' ' + df_art['description'].fillna('')).str.lower()

# World category keyword heuristic
world_keywords = [
    'iraq','iran','syria','israel','palest','gaza','ukraine','russia','moscow','putin','kiev','crimea',
    'china','beijing','japan','tokyo','korea','seoul','india','pakistan','afghanistan','taliban',
    'europe','eu','european','britain','uk ','london','france','paris','germany','berlin','italy','rome',
    'spain','madrid','greece','athens','turkey','ankara','istanbul','egypt','cairo','libya','tunisia','algeria',
    'sudan','nigeria','kenya','somalia','south africa','saudi','riyadh','opec','un ','united nations','nato',
    'refugee','migrant','asylum','election','president','prime minister','parliament','government',
    'militant','rebel','bomb','attack','terror','isis','islamic state','al qaeda','ceasefire','sanction'
]
exclude_keywords = [
    'stock','stocks','wall st','wall street','nasdaq','dow','s\&p','earnings','ipo','shares','profit','oil prices',
    'fund','mutual','market','economy','economic','inflation','trade deficit','rate cut','interest rates',
    'football','soccer','nba','nfl','mlb','olympic','tournament','match','league','coach','player','goal',
    'science','research','study','nasa','space','iphone','android','google','microsoft','ibm','chip','software'
]

def is_world(text):
    hit = any(k in text for k in world_keywords)
    if not hit:
        return False
    # if strongly business/sports/tech, exclude
    ex = sum(1 for k in exclude_keywords if k in text)
    return ex < 2

# Merge 2015 articles with content
df = df_meta.merge(df_art[['article_id','text']], on='article_id', how='left')
df['is_world'] = df['text'].fillna('').apply(is_world)
df_world = df[df['is_world']]

# Count by region
counts = df_world.groupby('region', dropna=False).size().sort_values(ascending=False)
result = {
    'top_region': None,
    'top_count': 0,
    'counts_by_region': counts.to_dict()
}
if len(counts) > 0:
    result['top_region'] = counts.index[0]
    result['top_count'] = int(counts.iloc[0])

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EnlYmeQ9JyDJJ1iUGIgAjHfh': 'file_storage/call_EnlYmeQ9JyDJJ1iUGIgAjHfh.json', 'var_call_iVLvqaJxSYKjCCcsDXkkMD2H': 'file_storage/call_iVLvqaJxSYKjCCcsDXkkMD2H.json'}

exec(code, env_args)

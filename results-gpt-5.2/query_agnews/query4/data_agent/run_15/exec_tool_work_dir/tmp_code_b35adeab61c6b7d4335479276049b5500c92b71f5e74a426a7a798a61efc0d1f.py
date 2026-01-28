code = """import json, pandas as pd

meta_path = var_call_hu2YVJ3VFtwu0VevZdB9TNGz
arts_path = var_call_FyE1c2ha8WPxdcjA7vHtAmjp

with open(meta_path, 'r', encoding='utf-8') as f:
    meta = json.load(f)
with open(arts_path, 'r', encoding='utf-8') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids to int
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# join only 2015 articles
df = meta_df.merge(arts_df, on='article_id', how='inner')

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# simple keyword-based categorization
world_kw = [
    'iraq','iran','israel','palestin','gaza','syria','syrian','ukraine','russia','moscow','putin',
    'china','beijing','japan','tokyo','korea','seoul','india','pakistan','afghanistan','taliban',
    'yemen','saudi','turkey','ankara','egypt','cairo','nigeria','kenya','sudan','congo','somalia',
    'european union','eu ','britain','uk ','london','france','paris','germany','berlin','spain',
    'italy','rome','sweden','norway','finland','poland','hungary','serbia','bosnia','kosovo',
    'brazil','argentina','chile','peru','colombia','venezuela','mexico',
    'united nations','u.n.','nato','prime minister','president','election','rebels','militants',
    'terror','bomb','attack','war','ceasefire','refugee','sanctions','embassy'
]
sports_kw = ['match','tournament','league','goal','coach','nba','nfl','mlb','nhl','fifa','olympic','cricket','tennis','soccer','football','basketball','baseball','hockey','golf']
business_kw = ['stocks','wall st','earnings','ipo','market','oil','prices','trade deficit','economy','inflation','fed','interest rates','shares','profit','revenue','merger','acquisition','imf','opec','company','billion','quarter']
science_kw = ['research','scientist','study','ibm','nasa','space','planet','mars','genome','vaccine','virus','computer','software','internet','ai','robot','quantum','climate','energy','technology']

import re

def score(kws, s):
    sc = 0
    for kw in kws:
        if kw in s:
            sc += 1
    return sc

scores = pd.DataFrame({
    'world': text.apply(lambda s: score(world_kw, s)),
    'sports': text.apply(lambda s: score(sports_kw, s)),
    'business': text.apply(lambda s: score(business_kw, s)),
    'science_tech': text.apply(lambda s: score(science_kw, s)),
})

cat = scores.idxmax(axis=1)
# require at least 1 hit; else default to business (common in dataset)
cat = cat.where(scores.max(axis=1) > 0, 'business')

world_df = df[cat == 'world']

# count by region
counts = world_df.groupby('region').size().sort_values(ascending=False)
if len(counts)==0:
    result = {'region': None, 'world_article_count': 0}
else:
    top_region = counts.index[0]
    top_count = int(counts.iloc[0])
    result = {'region': str(top_region), 'world_article_count': top_count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hu2YVJ3VFtwu0VevZdB9TNGz': 'file_storage/call_hu2YVJ3VFtwu0VevZdB9TNGz.json', 'var_call_FyE1c2ha8WPxdcjA7vHtAmjp': 'file_storage/call_FyE1c2ha8WPxdcjA7vHtAmjp.json'}

exec(code, env_args)

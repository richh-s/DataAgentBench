code = """import json, pandas as pd

# load metadata (2015)
meta_src = var_call_5k8ZRe3g0A65CCler4LT5o4q
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

art_src = var_call_vMZwmQmUvTBoPBWIkxS7zE5F
if isinstance(art_src, str):
    with open(art_src, 'r', encoding='utf-8') as f:
        arts = json.load(f)
else:
    arts = art_src

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# merge
df = meta_df.merge(arts_df, on='article_id', how='inner')

# simple keyword-based classifier
world_kw = [
    'iraq','iran','israel','palestin','gaza','syria','syrian','ukraine','russia','russian','moscow',
    'afghanistan','pakistan','india','china','beijing','north korea','south korea','kim jong',
    'eu','european union','nato','united nations','u.n.','un ','france','germany','britain','uk ',
    'london','paris','berlin','madrid','italy','rome','turkey','ankara','istanbul','egypt','cairo',
    'saudi','yemen','jordan','lebanon','libya','sudan','darfur','kenya','nigeria','congo','somalia',
    'japan','tokyo','philippines','thailand','vietnam','myanmar','australia','canada','mexico',
    'brazil','argentina','chile','peru','venezuela','colombia','election','president','prime minister',
    'parliament','rebel','militant','terror','bomb','attack','war','ceasefire','refugee','diplom',
    'sanction','embassy','foreign','border','nuclear','u.s.','us ','united states'
]

sports_kw = ['game','match','season','league','tournament','olympic','nba','nfl','mlb','nhl','soccer','football','cricket','tennis','golf','baseball','hockey','coach','player','championship','finals']
biz_kw = ['stocks','wall st','wall street','ipo','shares','earnings','profit','revenue','quarter','trade deficit','economy','economic','oil','opec','market','dollar','euro','yen','interest rate','bank','imf','inflation','fund','investment','company','merger','takeover']
sci_kw = ['research','scientist','study','technology','tech','internet','software','hardware','google','ibm','microsoft','apple','nasa','space','climate','genome','virus','vaccine','quantum','robot','ai','artificial intelligence']

import re

def classify(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    def score(kws):
        s=0
        for kw in kws:
            if kw in text:
                s+=1
        return s
    scores = {
        'World': score(world_kw),
        'Sports': score(sports_kw),
        'Business': score(biz_kw),
        'Science/Technology': score(sci_kw)
    }
    # pick max; tie-breaker prefer World if it has any hit
    mx = max(scores.values())
    best = [k for k,v in scores.items() if v==mx]
    if mx==0:
        return None
    if 'World' in best:
        return 'World'
    return best[0]

df['category'] = df.apply(classify, axis=1)
world_df = df[df['category']=='World']
counts = world_df.groupby('region').size().sort_values(ascending=False)

result = {
    'top_region': None if counts.empty else counts.index[0],
    'top_region_world_articles_2015': 0 if counts.empty else int(counts.iloc[0]),
    'all_regions_counts': {k:int(v) for k,v in counts.items()}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5k8ZRe3g0A65CCler4LT5o4q': 'file_storage/call_5k8ZRe3g0A65CCler4LT5o4q.json', 'var_call_vMZwmQmUvTBoPBWIkxS7zE5F': 'file_storage/call_vMZwmQmUvTBoPBWIkxS7zE5F.json'}

exec(code, env_args)

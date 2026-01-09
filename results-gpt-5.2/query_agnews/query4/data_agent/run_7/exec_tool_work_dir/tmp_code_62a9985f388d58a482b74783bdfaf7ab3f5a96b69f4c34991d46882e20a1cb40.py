code = """import json, pandas as pd

# load metadata 2015
meta_src = var_call_smSVMN9cKDVUnyrQMYxy4rXv
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_bv2CnHsMIXHWODP6MPLURA3N

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# join to get title/description
j = meta_df.merge(arts_df, on='article_id', how='inner')

world_kw = [
    'iraq','iran','israel','palestin','gaza','syria','lebanon','jordan','yemen','saudi','uae','qatar','kuwait','bahrain','oman','afghanistan','pakistan','india','china','japan','korea','taiwan',
    'russia','ukrain','crimea','moscow','putin','europe','eu ','e.u','britain','uk ','london','france','germany','italy','spain','greece','turkey',
    'united nations','u.n.','nato','refugee','migrant','border','sanction','diplomat','embassy','election','protest','coup','terror','bomb','attack','militant','hostage',
    'pope','vatican','earthquake','tsunami','flood','typhoon','ebola','outbreak','pandemic',
    'hong kong','beijing','tokyo','seoul','baghdad','kabul','tehran','jerusalem','damascus'
]
exclude_kw = ['stock','shares','earnings','wall st','wall street','nasdaq','dow','s&p','profit','bank','oil price','crude','market','company','corp','inc','billion','deal','merger','acquisition',
              'nfl','nba','mlb','nhl','soccer','football','basketball','baseball','tennis','golf','olympic','match','tournament','league',
              'iphone','android','software','app','chip','semiconductor','google','microsoft','apple','facebook','tesla','startup']

import re

def is_world(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    # exclude clear business/sports/tech
    if any(k in text for k in exclude_kw):
        # still allow if strong world signals
        pass
    score = 0
    for k in world_kw:
        if k in text:
            score += 1
    # also if title starts with country/region patterns e.g. 'Iraq', 'China'
    if re.match(r'^(iraq|iran|israel|china|russia|ukraine|syria|france|germany|britain|uk|india|japan|korea|afghanistan|pakistan|turkey)\b', (row.get('title') or '').lower()):
        score += 2
    # decide threshold
    return score >= 2

j['is_world'] = j.apply(is_world, axis=1)
world = j[j['is_world']]

counts = world.groupby('region').size().sort_values(ascending=False)
if len(counts)==0:
    ans = {"region": None, "world_articles_2015": 0}
else:
    top_region = counts.index[0]
    ans = {"region": str(top_region), "world_articles_2015": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_smSVMN9cKDVUnyrQMYxy4rXv': 'file_storage/call_smSVMN9cKDVUnyrQMYxy4rXv.json', 'var_call_bv2CnHsMIXHWODP6MPLURA3N': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

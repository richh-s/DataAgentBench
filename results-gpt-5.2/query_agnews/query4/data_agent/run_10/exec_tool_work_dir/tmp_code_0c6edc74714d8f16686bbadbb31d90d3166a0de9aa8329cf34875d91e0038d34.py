code = """import json, pandas as pd

# Load metadata (2015 only) from file path
meta_path = var_call_35wcfxiE350vrAY4XGTNKNNm
with open(meta_path, 'r', encoding='utf-8') as f:
    meta = json.load(f)

arts = var_call_60a8W0HJUcr5Ix2Z2aKxHzEu

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize article_id types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Simple keyword-based categorization
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','syria','syrian','lebanon','jordan',
    'afghanistan','taliban','pakistan','india','china','japan','korea','north korea','south korea',
    'russia','ukrain','crimea','putin','moscow','europe','european','eu ','e.u','brexit','uk ',
    'britain','england','france','germany','italy','spain','greece','turkey','ankara','istanbul',
    'egypt','libya','tunisia','algeria','morocco','sudan','somalia','kenya','nigeria','congo','uganda','zimbabwe',
    'saudi','yemen','qatar','uae','emirates','kuwait','bahrain','oman','middle east',
    'united nations','u.n.','nato','refugee','migrant','asylum','diplomat','sanction','war','ceasefire','terror','bomb','blast','attack',
    'election','president','prime minister','parliament','coup','protest','riot','military','army','rebel'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','baseball','hockey','coach','tournament','league','cup','match','final','season','win','loss','score']
biz_kw = ['stocks','shares','earnings','revenue','profit','loss','market','wall st','wall street','nasdaq','dow','s&p','economy','economic','inflation','gdp','oil','crude','bank','fed','interest rate','merger','acquisition','ipo','company','corporate','finance','currency','dollar','euro','yen','trade','tariff']
sci_kw = ['science','technology','tech','software','hardware','internet','web','smartphone','iphone','android','google','microsoft','apple','facebook','amazon','tesla','space','nasa','satellite','robot','ai','artificial intelligence','climate','weather','virus','vaccine','medical','health','research','study','genome','quantum']

import re

def classify(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    # prioritize explicit sports/business/sci-tech signals over world
    def has_any(kws):
        return any(kw in text for kw in kws)
    if has_any(sports_kw):
        return 'Sports'
    if has_any(biz_kw):
        return 'Business'
    if has_any(sci_kw):
        return 'Science/Technology'
    if has_any(world_kw):
        return 'World'
    # fallback: if mentions country/foreign affairs lightly
    if re.search(r'\b(iraq|iran|china|russia|ukraine|syria|israel|gaza|afghanistan|pakistan|india|japan|korea|eu|united nations|nato)\b', text):
        return 'World'
    return 'Business'  # default bias toward business for Reuters-style market news

arts_df['category'] = arts_df.apply(lambda r: classify(r.get('title'), r.get('description')), axis=1)

merged = meta_df.merge(arts_df[['article_id','category']], on='article_id', how='inner')
world_2015 = merged[merged['category']=='World']

counts = world_2015.groupby('region', dropna=False).size().sort_values(ascending=False)
if len(counts)==0:
    out = {"region": None, "world_article_count": 0}
else:
    out = {"region": counts.index[0], "world_article_count": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_35wcfxiE350vrAY4XGTNKNNm': 'file_storage/call_35wcfxiE350vrAY4XGTNKNNm.json', 'var_call_60a8W0HJUcr5Ix2Z2aKxHzEu': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

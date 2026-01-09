code = """import json, pandas as pd

# load metadata (may be file path)
meta = var_call_zAvo8xPGAgjzaMqXUV0Qi5i6
if isinstance(meta, str):
    with open(meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)

arts = var_call_IqhK3KnpLVJ7qtgdQDpiYdOc

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(str)
arts_df['article_id'] = arts_df['article_id'].astype(str)

# join
df = meta_df.merge(arts_df, on='article_id', how='inner')

# simple keyword-based classifier
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','syria','syrian','lebanon','yemen','afghan','pakistan',
    'ukraine','russia','moscow','kremlin','putin','nato','european union','eu ','brussels','germany','france','britain','uk ',
    'china','beijing','japan','tokyo','korea','north korea','south korea','india','delhi','taiwan','hong kong',
    'united nations','u.n.','un ','diplomat','embassy','president','prime minister','minister','parliament','election',
    'refugee','migrant','immigration','border','sanction','ceasefire','war','militant','rebels','attack','bomb','terror',
    'earthquake','tsunami','cyclone','flood','aid','peace','summit','treaty'
]

sports_kw = ['vs.','vs ','nba','nfl','mlb','nhl','soccer','football','baseball','basketball','tennis','golf','olympic','world cup','championship','coach','player','match','tournament']
biz_kw = ['stock','wall st','dow','nasdaq','s&p','earnings','profit','revenue','acquisition','merger','ipo','shares','bond','oil','crude','economy','economic','inflation','fed','interest rate','bank','market','trade','company','companies']
sci_kw = ['study','research','scientist','space','nasa','mars','satellite','climate','global warming','gene','genetic','virus','vaccine','cancer','technology','tech','internet','software','hardware','ai','robot','iphone','android']

def score(text, kws):
    t = (text or '').lower()
    return sum(1 for k in kws if k in t)

def classify(row):
    text = f"{row.get('title','')} {row.get('description','')}"
    scores = {
        'World': score(text, world_kw),
        'Sports': score(text, sports_kw),
        'Business': score(text, biz_kw),
        'Science/Technology': score(text, sci_kw)
    }
    # tie-breaker: if all zero, default Business (Reuters finance-heavy)
    best = max(scores.items(), key=lambda x: x[1])
    if best[1] == 0:
        return 'Business'
    return best[0]

df['category'] = df.apply(classify, axis=1)
world_df = df[df['category']=='World']

counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)
if len(counts)==0:
    out = {'region': None, 'world_article_count_2015': 0}
else:
    out = {'region': counts.index[0], 'world_article_count_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zAvo8xPGAgjzaMqXUV0Qi5i6': 'file_storage/call_zAvo8xPGAgjzaMqXUV0Qi5i6.json', 'var_call_IqhK3KnpLVJ7qtgdQDpiYdOc': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

# Load metadata 2015
meta_src = var_call_jhmCMqoR53StvKyrMLp7aT8x
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

articles = var_call_MgKsYQy65liGfgL7fOqwEaHu

df_meta = pd.DataFrame(meta)
df_art = pd.DataFrame(articles)

# Normalize ids to int
for df in (df_meta, df_art):
    df['article_id'] = pd.to_numeric(df['article_id'], errors='coerce').astype('Int64')

df = df_meta.merge(df_art, on='article_id', how='left')

# Simple keyword-based classifier for 4 categories
world_kw = [
    'iraq','iran','israel','palestin','gaza','ukraine','russia','moscow','kremlin','china','beijing','japan','tokyo','korea','seoul','pyongyang',
    'afghanistan','pakistan','india','delhi','bangladesh','syria','damascus','lebanon','yemen','saudi','egypt','cairo','libya','tripoli','sudan',
    'nigeria','kenya','somalia','europe','eu','nato','united nations','u.n.','geneva','brussels','london','paris','germany','berlin','france','italy','spain','turkey',
    'prime minister','president','election','parliament','rebels','militants','bomb','attack','troops','ceasefire','sanctions','diplomat','embassy','refugee'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','tennis','golf','olympic','fifa','uefa','cricket','hockey','baseball','basketball','coach','tournament','match','cup','league']
business_kw = ['wall st','stocks','shares','earnings','profit','loss','market','dow','nasdaq','s&p','oil','crude','prices','economy','inflation','gdp','bank','fed','interest','trade','merger','acquisition','company','reuters - private investment']
science_kw = ['software','internet','computer','technology','tech','science','research','study','space','nasa','satellite','chip','biotech','medical','health','virus','ai','robot','smartphone']

kws = {
    'World': world_kw,
    'Sports': sports_kw,
    'Business': business_kw,
    'Science/Technology': science_kw
}

texts = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

scores = {}
for cat, kwlist in kws.items():
    s = pd.Series(0, index=df.index, dtype='int64')
    for kw in kwlist:
        s += texts.str.contains(kw, regex=False).astype('int64')
    scores[cat] = s

score_df = pd.DataFrame(scores)
# Assign category with max score; if all zero, default to Business (common Reuters finance)
max_cat = score_df.idxmax(axis=1)
all_zero = (score_df.max(axis=1) == 0)
max_cat = max_cat.where(~all_zero, 'Business')

df['category'] = max_cat

world_df = df[df['category'] == 'World']
counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)

if counts.empty:
    out = {'region': None, 'world_articles_2015': 0}
else:
    out = {'region': str(counts.index[0]), 'world_articles_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jhmCMqoR53StvKyrMLp7aT8x': 'file_storage/call_jhmCMqoR53StvKyrMLp7aT8x.json', 'var_call_MgKsYQy65liGfgL7fOqwEaHu': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

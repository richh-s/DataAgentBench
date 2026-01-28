code = """import json, pandas as pd

# load 2015 metadata
meta = var_call_IQ2NWziZ67s9MFUHnvt4vRJN
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# articles
arts = var_call_LYfCOz0ZVSwzGJfoo7RkCQ15
arts_df = pd.DataFrame(arts)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# classify category by keywords
world_kw = [
    'iraq','iran','israel','palestin','gaza','syria','ukraine','russia','putin','nato','eu','europe','china','japan','korea','india','pakistan',
    'afghanistan','terror','bomb','militant','rebels','u.n.','united nations','prime minister','president','election','parliament','diplomat','summit',
    'refugee','immigrant','border','war','troops','ceasefire','sanction','coup','protest','riot','earthquake','tsunami','flood','typhoon'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','tennis','golf','olympic','fifa','uefa','world cup','cricket','baseball','hockey','coach','match','tournament','league']
business_kw = ['stocks','wall st','reuters -','profit','earnings','market','oil','crude','bank','dollar','economy','inflation','merger','acquisition','ipo','shares','bond','trade','tariff','currency']
science_kw = ['tech','technology','software','internet','google','apple','microsoft','facebook','ai','robot','space','nasa','mars','satellite','science','research','study','drug','medical','health','climate']

def classify(text):
    t = (text or '').lower()
    def has_any(kws):
        return any(k in t for k in kws)
    # priority: sports, business, sci/tech, world
    if has_any(sports_kw):
        return 'Sports'
    if has_any(business_kw):
        return 'Business'
    if has_any(science_kw):
        return 'Science/Technology'
    if has_any(world_kw):
        return 'World'
    return 'World'

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna(''))
arts_df['category'] = arts_df['text'].apply(classify)

merged = meta_df.merge(arts_df[['article_id','category']], on='article_id', how='inner')
world_2015 = merged[merged['category']=='World']
counts = world_2015.groupby('region').size().sort_values(ascending=False)
if len(counts)==0:
    result = {'region': None, 'count': 0}
else:
    result = {'region': counts.index[0], 'count': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_IQ2NWziZ67s9MFUHnvt4vRJN': 'file_storage/call_IQ2NWziZ67s9MFUHnvt4vRJN.json', 'var_call_LYfCOz0ZVSwzGJfoo7RkCQ15': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

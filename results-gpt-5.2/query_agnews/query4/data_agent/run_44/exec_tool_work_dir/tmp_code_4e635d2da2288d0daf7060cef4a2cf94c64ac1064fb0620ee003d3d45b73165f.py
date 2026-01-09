code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

meta = load_records(var_call_fCy8hwKAmoRXY1ZQHf6HmmXR)
arts = load_records(var_call_TxZOOuHdxGfsnmL8kzDHECHK)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize ids to int
for df in (meta_df, arts_df):
    df['article_id'] = df['article_id'].astype(int)

# Simple keyword-based categorization
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','syria','syrian','russia','ukraine','crimea',
    'china','beijing','japan','korea','north korea','south korea','pakistan','india','afghan','taliban',
    'europe','eu ','e.u','britain','uk ','u.k','london','france','germany','spain','italy','greek','turkey',
    'united nations','u.n','nato','diplom','summit','minister','president','election','parliament','rebels',
    'terror','bomb','attack','militant','hostage','ceasefire','sanction','refugee','migrant','border',
    'pope','vatican','hong kong','taiwan','philippines','indonesia','malaysia','thailand','myanmar','sri lanka',
    'egypt','libya','sudan','nigeria','kenya','somalia','congo','zimbabwe','south africa','africa',
    'mexico','brazil','argentina','venezuela','colombia','peru','chile','cuba','haiti',
    'earthquake','tsunami','flood','typhoon'
]
# negative keywords for other categories
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','formula','nascar','hockey','baseball','basketball','coach','tournament','world cup','grand slam']
biz_kw = ['stocks','shares','market','earnings','profit','loss','wall st','wall street','dow','nasdaq','s&p','oil','opec','economy','bank','fed','inflation','gdp','company','ceo','acquisition','merger','revenue','ipo','bond','currency']
sci_kw = ['google','apple','microsoft','amazon','facebook','meta','tesla','nasa','space','rocket','mars','satellite','ai','artificial intelligence','software','hardware','chip','semiconductor','quantum','robot','cyber','virus','vaccine','health study','research','climate','science','technology','tech']

def is_world(text):
    t = (text or '').lower()
    # If clearly another category, exclude
    if any(k in t for k in sports_kw):
        return False
    if any(k in t for k in sci_kw):
        return False
    # business is broad; only exclude if strongly businessy
    if sum(k in t for k in biz_kw) >= 2:
        return False
    return any(k in t for k in world_kw)

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna(''))
arts_df['is_world'] = arts_df['text'].apply(is_world)

world_ids = set(arts_df.loc[arts_df['is_world'], 'article_id'].tolist())
meta_world = meta_df[meta_df['article_id'].isin(world_ids)].copy()

counts = meta_world.groupby('region', dropna=False).size().sort_values(ascending=False)
if len(counts)==0:
    out = {"region": None, "world_article_count": 0}
else:
    out = {"region": str(counts.index[0]), "world_article_count": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fCy8hwKAmoRXY1ZQHf6HmmXR': 'file_storage/call_fCy8hwKAmoRXY1ZQHf6HmmXR.json', 'var_call_TxZOOuHdxGfsnmL8kzDHECHK': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

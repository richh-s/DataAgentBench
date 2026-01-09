code = """import json, pandas as pd

# load 2015 metadata
meta = var_call_LZe3Mfjau1I8WdAOAgVYtaWX
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# articles (all years)
art = var_call_Ev07rRriyGT6zDRDax1kWc61
art_df = pd.DataFrame(art)
art_df['article_id'] = art_df['article_id'].astype(int)

# join only 2015 articles
df = meta_df.merge(art_df, on='article_id', how='inner')

# simple keyword-based categorization
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','syria','syrian','ukraine','russia','putin',
    'china','beijing','japan','korea','north korea','south korea','pakistan','india','afghanistan',
    'europe','eu ','e.u','nato','un ','u.n','united nations','britain','uk ','london','france','germany',
    'spain','italy','greece','turkey','egypt','libya','sudan','nigeria','kenya','somalia','congo','south africa',
    'mexico','brazil','argentina','venezuela','colombia','peru','chile','cuba','haiti',
    'refugee','migrant','immigration','border','election','prime minister','president','parliament','government',
    'bomb','attack','militant','terror','war','ceasefire','protest','uprising','coup','sanction'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','baseball','hockey','basketball','world cup','grand slam']
biz_kw = ['stock','shares','earnings','profit','revenue','bank','oil','crude','market','economy','inflation','gdp','trade','merger','acquisition','ipo','bond','currency','dollar','euro','yen']
sci_kw = ['technology','tech','software','internet','computer','ai','robot','space','nasa','satellite','physics','biology','medical','medicine','health','vaccine','research','scientist','climate','energy']

def categorize(text):
    t = (text or '').lower()
    score = {
        'World': sum(1 for k in world_kw if k in t),
        'Sports': sum(1 for k in sports_kw if k in t),
        'Business': sum(1 for k in biz_kw if k in t),
        'Science/Technology': sum(1 for k in sci_kw if k in t),
    }
    # if all zero, default to World (broadest)
    best = max(score, key=score.get)
    if score[best] == 0:
        return 'World'
    return best

texts = (df['title'].fillna('') + ' ' + df['description'].fillna('')).tolist()
df['category'] = [categorize(x) for x in texts]

world_df = df[df['category'] == 'World']
counts = world_df.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    ans = None
else:
    top_region = counts.index[0]
    ans = top_region

print('__RESULT__:')
print(json.dumps({'top_region': ans, 'counts': counts.to_dict()}))"""

env_args = {'var_call_LZe3Mfjau1I8WdAOAgVYtaWX': 'file_storage/call_LZe3Mfjau1I8WdAOAgVYtaWX.json', 'var_call_Ev07rRriyGT6zDRDax1kWc61': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

# Load 2015 metadata (large)
meta_src = var_call_fbhyUopFqnyuaOVMGrrnYK8F
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_qgtj10c1qo8C3FJDfGMQM6rm

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# join
df = meta_df.merge(arts_df, on='article_id', how='inner')

# simple keyword-based classifier for 4 categories
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezb','syria','assad','russia','ukrain','crimea',
    'afghanistan','pakistan','india','china','japan','korea','north korea','kim','europe','eu ',
    'britain','uk ','london','france','germany','italy','spain','greece','turkey','nato','un ',
    'united nations','u.n.','diplomat','election','government','president','parliament','minister',
    'rebel','militant','terror','bomb','attack','war','ceasefire','sanction','refugee','immigrant',
    'pope','vatican','australia','canada','mexico','brazil','argentina','venezuela','colombia',
    'nigeria','kenya','south africa','egypt','saudi','yemen','libya','sudan','congo','zimbabwe'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','rugby','baseball','hockey','basketball','world cup','championship','coach','player','match','tournament']
biz_kw = ['stock','stocks','wall st','wall street','market','shares','earnings','profit','loss','revenue','ipo','bond','bonds','oil','crude','gold','inflation','fed','interest rate','bank','economy','gdp','company','companies','merger','acquisition','aerospace','commercial','investment','fund','carlyle','reuters - private investment']
sci_kw = ['science','scientist','research','study','technology','tech','software','hardware','internet','online','google','apple','microsoft','facebook','amazon','startup','ai','robot','space','nasa','mars','satellite','genome','dna','climate','warming','virus','vaccine','medical','health','quantum']

def classify(text):
    t = (text or '').lower()
    def has_any(kws):
        return any(kw in t for kw in kws)
    # priority order to reduce false positives from oil/economy in world news
    if has_any(sports_kw):
        return 'Sports'
    if has_any(sci_kw):
        return 'Science/Technology'
    if has_any(biz_kw):
        return 'Business'
    if has_any(world_kw):
        return 'World'
    # fallback heuristics
    return 'World'

df['text'] = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = df['text'].map(classify)

world_df = df[df['category']=='World']
counts = world_df.groupby('region')['article_id'].nunique().sort_values(ascending=False)

if len(counts)==0:
    out = {'region': None, 'world_article_count_2015': 0}
else:
    out = {'region': counts.index[0], 'world_article_count_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fbhyUopFqnyuaOVMGrrnYK8F': 'file_storage/call_fbhyUopFqnyuaOVMGrrnYK8F.json', 'var_call_qgtj10c1qo8C3FJDfGMQM6rm': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

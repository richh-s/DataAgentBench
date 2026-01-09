code = """import json, pandas as pd

# Load metadata 2015 (large)
meta_src = var_call_Os8qSTGilO44ZgepvSHXLjhe
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_jypzZk0r94GArBeh8XGot4t4

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join 2015 metadata to article text
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple keyword-based classifier
world_kw = [
    'iraq','iran','israel','palestin','gaza','ukraine','russia','putin','moscow','china','beijing','japan','korea','north korea','syria','assad','afghanistan','pakistan','india','eu','europe','britain','uk','france','germany','spain','italy','turkey','nato','un','united nations','u.n.','election','minister','parliament','president','prime minister','rebels','militant','terror','bomb','attack','war','ceasefire','sanction','refugee','diplomat','embassy'
]
sports_kw = ['nfl','nba','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','fifa','uefa','championship','tournament','coach','player','match','win','loss','league']
business_kw = ['stocks','wall st','wall street','reuters -','earnings','profit','revenue','merger','acquisition','ipo','oil','crude','prices','economy','market','company','bank','fed','inflation','dollar','euro','trade','tariff']
science_kw = ['tech','technology','software','internet','ai','robot','space','nasa','satellite','mars','iphone','android','google','microsoft','facebook','twitter','research','study','scientist','climate','gene','virus','vaccine']


def classify(text):
    t = (text or '').lower()
    scores = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for kw in world_kw:
        if kw in t:
            scores['World'] += 1
    for kw in sports_kw:
        if kw in t:
            scores['Sports'] += 1
    for kw in business_kw:
        if kw in t:
            scores['Business'] += 1
    for kw in science_kw:
        if kw in t:
            scores['Science/Technology'] += 1
    # choose max; tie-breaker preference: World, Business, Sports, Sci/Tech
    order = ['World','Business','Sports','Science/Technology']
    maxv = max(scores.values())
    top = [k for k,v in scores.items() if v==maxv]
    if maxv==0:
        return 'World'  # default to World when uncertain
    for k in order:
        if k in top:
            return k

# Build text and classify
text = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = text.map(classify)

world_df = df[df['category']=='World']
counts = world_df.groupby('region')['article_id'].count().sort_values(ascending=False)

if len(counts)==0:
    result = {'region': None, 'world_articles_2015': 0}
else:
    top_region = counts.index[0]
    result = {'region': str(top_region), 'world_articles_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Os8qSTGilO44ZgepvSHXLjhe': 'file_storage/call_Os8qSTGilO44ZgepvSHXLjhe.json', 'var_call_jypzZk0r94GArBeh8XGot4t4': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

# load 2015 metadata (possibly from file)
meta = var_call_mWPx7VfjpHr9hlNNe7fn4s54
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)

arts = var_call_v2HnZT9gotagLoEWjIfY0WxI

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize article_id to int for join
for df in (meta_df, arts_df):
    df['article_id'] = pd.to_numeric(df['article_id'], errors='coerce').astype('Int64')

df = meta_df.merge(arts_df, on='article_id', how='inner')

# simple keyword-based classifier
world_kw = [
    'iraq','iran','israel','palestin','gaza','afghanistan','pakistan','syria','lebanon','yemen','russia','ukraine','crimea',
    'china','beijing','japan','tokyo','korea','seoul','north korea','kim','taiwan','hong kong','india','delhi','kashmir',
    'europe','eu ','european','brussels','germany','france','britain','uk ','london','italy','spain','greece',
    'united nations','u.n.','nato','terror','militant','bomb','suicide','hostage','sanction','refugee','migrant',
    'election','prime minister','president','parliament','coup','rebel','insurgent','civil war','ceasefire',
    'pope','vatican'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','world cup','olympic','tennis','golf','cricket','rugby','formula','grand prix','race','tournament','coach','striker','goal','league']
biz_kw = ['stock','wall st','dow','nasdaq','earnings','profit','revenue','oil price','crude','inflation','interest rate','fed','bank','merger','acquisition','ipo','company','ceo','shares','market','economy','gdp']
sci_kw = ['software','internet','google','microsoft','apple','iphone','android','chip','semiconductor','ai','robot','space','nasa','mars','satellite','telescope','physics','biology','virus','vaccine','clinical','gene','climate','carbon']

def classify(text):
    t = (text or '').lower()
    w = sum(1 for k in world_kw if k in t)
    s = sum(1 for k in sports_kw if k in t)
    b = sum(1 for k in biz_kw if k in t)
    c = sum(1 for k in sci_kw if k in t)
    scores = {'World': w, 'Sports': s, 'Business': b, 'Science/Technology': c}
    mx = max(scores.values())
    if mx == 0:
        # fallback: if contains country/city-like hints or conflict words, lean World; else Business if finance words; else Sci/Tech
        return 'World'
    # tie-breaker preference: World > Business > Sports > Sci/Tech
    pref = ['World','Business','Sports','Science/Technology']
    top = [k for k,v in scores.items() if v==mx]
    for p in pref:
        if p in top:
            return p

text = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = text.map(classify)

world_df = df[df['category']=='World']
counts = world_df.groupby('region').size().sort_values(ascending=False)

if len(counts)==0:
    result = {'region': None, 'world_articles': 0}
elif (counts==counts.iloc[0]).sum() > 1:
    top_regions = counts[counts==counts.iloc[0]].index.tolist()
    result = {'region': top_regions, 'world_articles': int(counts.iloc[0])}
else:
    result = {'region': counts.index[0], 'world_articles': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_mWPx7VfjpHr9hlNNe7fn4s54': 'file_storage/call_mWPx7VfjpHr9hlNNe7fn4s54.json', 'var_call_v2HnZT9gotagLoEWjIfY0WxI': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

# Load 2015 metadata (may be file path)
md = var_call_M1ISCx22zun9jcubelBYASn1
if isinstance(md, str):
    with open(md, 'r') as f:
        md = json.load(f)

arts = var_call_unxNQgQg6ngFwK6OKMf0RDbz

df_md = pd.DataFrame(md)
df_a = pd.DataFrame(arts)

# Ensure types
for c in ['article_id']:
    df_md[c] = df_md[c].astype(str)
    df_a[c] = df_a[c].astype(str)

# Merge
df = df_md.merge(df_a, on='article_id', how='inner')

# Simple keyword-based classifier
world_kw = [
    'iraq','iran','syria','israel','palest','gaza','ukraine','russia','putin','china','beijing','japan','korea',
    'afghanistan','pakistan','india','europe','eu','nato','un','united nations','refugee','migrant','election',
    'prime minister','president','parliament','government','military','army','bomb','attack','terror','isis','al qaeda',
    'earthquake','tsunami','flood','pope','vatican','saudi','yemen','egypt','libya','sudan','somalia','kenya','nigeria'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','cricket','tennis','golf','olympic','fifa','uefa','championship','coach','match','tournament','player','league']
business_kw = ['stocks','shares','earnings','profit','revenue','ipo','bank','fed','economy','economic','oil','crude','market','dollar','euro','yen','inflation','trade','deal','merger','acquisition','company','prices']
sci_kw = ['science','tech','technology','software','internet','google','apple','microsoft','facebook','nasa','space','mars','satellite','research','study','genome','virus','vaccine','climate','carbon','ai','robot']


def classify(text):
    t = (text or '').lower()
    scores = {
        'World': sum(1 for k in world_kw if k in t),
        'Sports': sum(1 for k in sports_kw if k in t),
        'Business': sum(1 for k in business_kw if k in t),
        'Science/Technology': sum(1 for k in sci_kw if k in t),
    }
    # choose max; tie-breaker priority World, Business, Sports, Sci/Tech
    order = ['World','Business','Sports','Science/Technology']
    m = max(scores.values())
    if m == 0:
        # default to World (international/general news)
        return 'World'
    for cat in order:
        if scores[cat] == m:
            return cat


df['text'] = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = df['text'].map(classify)

# Count world by region
world_counts = (df[df['category']=='World']
                .groupby('region', dropna=False)
                .size()
                .sort_values(ascending=False))

if world_counts.empty:
    result = {"region": None, "world_articles": 0}
else:
    top_region = world_counts.index[0]
    top_count = int(world_counts.iloc[0])
    result = {"region": top_region, "world_articles": top_count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_M1ISCx22zun9jcubelBYASn1': 'file_storage/call_M1ISCx22zun9jcubelBYASn1.json', 'var_call_unxNQgQg6ngFwK6OKMf0RDbz': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

# Load metadata 2015 (large) from file
path_meta = var_call_VehaT3LE2whNwNDnisFlH9Q2
with open(path_meta, 'r', encoding='utf-8') as f:
    meta = json.load(f)

arts = var_call_2JXIhXShKGrWGopKAubiudbQ

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# Normalize types
for c in ['article_id']:
    df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce')

df = df_meta.merge(df_arts, on='article_id', how='left')

# Simple keyword-based classifier
world_kw = [
    'iraq','iran','israel','palestinian','gaza','hamas','hezbollah','lebanon','syria','assad','turkey','ukraine','russia','putin','moscow','kiev','crimea',
    'afghanistan','pakistan','india','china','beijing','japan','korea','seoul','north korea','kim','eu','european union','nato','united nations','u.n.',
    'britain','uk ','england','france','germany','spain','italy','greece','sweden','norway','denmark','finland','poland','hungary','czech',
    'mexico','canada','brazil','argentina','venezuela','colombia','peru','chile','australia','new zealand',
    'president','prime minister','election','parliament','government','minister','diplomat','summit','sanctions','refugee','migrant','war','ceasefire','terror','bomb','attack','hostage'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','world cup','olympic','tennis','golf','cricket','baseball','hockey','basketball','formula','grand prix','race','match','tournament','coach','player']

business_kw = ['stocks','wall st','wall street','reuters -','earnings','profit','shares','market','economy','economic','inflation','interest rate','fed','central bank','bank','oil','crude','prices','merger','acquisition','ipo','company','corp','revenue','sales']

sci_kw = ['nasa','space','mars','satellite','physics','biotech','genome','dna','medical','medicine','drug','clinical','research','scientist','technology','tech','software','internet','google','apple','microsoft','ai','robot','cyber','chip','semiconductor']


def classify(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    scores = {
        'World': sum(1 for k in world_kw if k in text),
        'Sports': sum(1 for k in sports_kw if k in text),
        'Business': sum(1 for k in business_kw if k in text),
        'Science/Technology': sum(1 for k in sci_kw if k in text),
    }
    # tie-breaker preference: World, Business, Sports, Sci/Tech
    best = sorted(scores.items(), key=lambda x: (x[1], ['World','Business','Sports','Science/Technology'].index(x[0])), reverse=True)[0][0]
    return best

# Classify
mask_has_text = df['title'].notna() | df['description'].notna()
df = df[mask_has_text].copy()
df['category'] = df.apply(classify, axis=1)

# Filter World and count by region
world_counts = df[df['category']=='World'].groupby('region', dropna=False).size().sort_values(ascending=False)

if len(world_counts)==0:
    result = {'region': None, 'world_article_count_2015': 0}
else:
    top_region = world_counts.index[0]
    top_count = int(world_counts.iloc[0])
    result = {'region': top_region, 'world_article_count_2015': top_count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_VehaT3LE2whNwNDnisFlH9Q2': 'file_storage/call_VehaT3LE2whNwNDnisFlH9Q2.json', 'var_call_2JXIhXShKGrWGopKAubiudbQ': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

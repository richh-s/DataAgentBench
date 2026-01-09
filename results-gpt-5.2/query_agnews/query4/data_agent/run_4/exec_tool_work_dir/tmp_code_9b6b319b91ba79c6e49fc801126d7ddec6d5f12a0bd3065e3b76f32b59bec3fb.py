code = """import json, pandas as pd

# Load metadata (may be a json file path)
meta = var_call_VTdf73vn0EmFeiNT55byilRV
if isinstance(meta, str):
    with open(meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)

arts = var_call_WP32V6PQmieI9O6xEUQdduGo

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# simple keyword-based classifier
world_kw = [
    'iraq','iran','israel','palest','gaza','hamas','hezbollah','syria','syrian','afghanistan','taliban',
    'ukraine','russia','putin','moscow','crimea','nato','european union','eu ','united nations','u.n.','un ',
    'china','beijing','japan','tokyo','north korea','kim','south korea','seoul','pakistan','india','kashmir',
    'turkey','ankara','egypt','cairo','libya','yemen','saudi','lebanon','jordan','qatar','kuwait',
    'germany','france','britain','u.k.','london','spain','italy','greece','sweden','norway','finland',
    'mexico','canada','brazil','argentina','venezuela','colombia','peru','chile',
    'earthquake','tsunami','bomb','blast','militant','rebels','insurgent','ceasefire','peace talks','election',
    'prime minister','president','parliament','refugee','migrant','immigration','border'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','baseball','basketball','hockey','race','grand prix','formula']
business_kw = ['stock','shares','wall st','wall street','earnings','profit','revenue','market','dow','nasdaq','s&p','bond','oil','crude','inflation','bank','fed','interest rate','ipo','merger','acquisition','currency','dollar','euro','yen']
tech_kw = ['software','internet','google','apple','microsoft','facebook','amazon','ai','artificial intelligence','robot','chip','semiconductor','smartphone','tablet','cyber','hacker','technology','science','nasa','space','mars','research','genome']

def categorize(text):
    t = (text or '').lower()
    scores = {
        'World': sum(1 for k in world_kw if k in t),
        'Sports': sum(1 for k in sports_kw if k in t),
        'Business': sum(1 for k in business_kw if k in t),
        'Science/Technology': sum(1 for k in tech_kw if k in t),
    }
    # pick max; tie-breaker favors World then Business then Sports then Sci/Tech
    order = ['World','Business','Sports','Science/Technology']
    mx = max(scores.values())
    if mx == 0:
        return 'Business'  # default for Reuters-like feed if no signals
    for c in order:
        if scores[c] == mx:
            return c

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna(''))
arts_df['category'] = arts_df['text'].map(categorize)

merged = meta_df.merge(arts_df[['article_id','category']], on='article_id', how='inner')
world_2015 = merged[merged['category']=='World']
counts = world_2015.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = {'region': None, 'world_articles_2015': 0}
else:
    top_region = counts.index[0]
    result = {'region': top_region, 'world_articles_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_VTdf73vn0EmFeiNT55byilRV': 'file_storage/call_VTdf73vn0EmFeiNT55byilRV.json', 'var_call_WP32V6PQmieI9O6xEUQdduGo': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

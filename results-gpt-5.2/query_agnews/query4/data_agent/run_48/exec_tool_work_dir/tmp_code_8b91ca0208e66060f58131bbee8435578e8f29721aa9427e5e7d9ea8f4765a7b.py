code = """import json, pandas as pd

# Load 2015 metadata (possibly from file)
meta_src = var_call_C4zC0O3doQDaLrqpJ7e4b6cF
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_loOZkIA8Gt0pJaXurnSAVhKh

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# join only 2015 articles that exist in content db
df = meta_df.merge(arts_df, on='article_id', how='inner')

def categorize(title, desc):
    t = ((title or '') + ' ' + (desc or '')).lower()
    world_kw = [
        'iraq','iran','israel','palest','gaza','afghanistan','pakistan','india','china','russia','ukraine','syria',
        'lebanon','jordan','egypt','yemen','saudi','turkey','european union','eu ','nato','united nations','u.n.',
        'refugee','migrant','asylum','terror','bomb','militant','insurgent','ceasefire','election','president',
        'prime minister','parliament','diplomat','embassy','sanction','coup','pope','vatican'
    ]
    sports_kw = ['nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','fifa','uefa','cricket','formula','grand prix','world cup','coach','tournament','match','league']
    biz_kw = ['stocks','wall st','wall street','dow','nasdaq','s&p','earnings','profit','revenue','ipo','acquisition','merger','oil','crude','economy','economic','inflation','jobs','unemployment','bank','fed','interest rate','bond','currency','dollar','euro','yen','trade','company','companies','market','share','shares']
    sci_kw = ['software','hardware','internet','smartphone','iphone','android','microsoft','google','apple','facebook','amazon','ai','artificial intelligence','robot','chip','semiconductor','startup','cyber','hack','security','space','nasa','satellite','telescope','climate','global warming','science','scientists','research','study','drug','vaccine','medical','health','biotech','genome']

    scores = {
        'World': sum(1 for k in world_kw if k in t),
        'Sports': sum(1 for k in sports_kw if k in t),
        'Business': sum(1 for k in biz_kw if k in t),
        'Science/Technology': sum(1 for k in sci_kw if k in t)
    }
    # tie-break preference: World over others when mentioned; else max
    max_score = max(scores.values())
    if max_score == 0:
        return 'World'  # default to World for general news-like items
    # if tie includes World, pick World
    tops = [c for c,s in scores.items() if s==max_score]
    if 'World' in tops:
        return 'World'
    return tops[0]

df['category'] = [categorize(t,d) for t,d in zip(df['title'], df['description'])]
world_df = df[df['category']=='World']

counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)
if len(counts)==0:
    result = {"region": None, "world_articles": 0}
else:
    top_region = counts.index[0]
    result = {"region": str(top_region), "world_articles": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_C4zC0O3doQDaLrqpJ7e4b6cF': 'file_storage/call_C4zC0O3doQDaLrqpJ7e4b6cF.json', 'var_call_loOZkIA8Gt0pJaXurnSAVhKh': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

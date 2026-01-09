code = """import json, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

meta = load_maybe_path(var_call_ycD5Tn2PvYb9A119GxQY5n9w)
arts = load_maybe_path(var_call_YXGYT2sREtdoS9rXJDNwnswl)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# join 2015 metadata with article text
df = meta_df.merge(arts_df, on='article_id', how='inner')

world_kw = [
    'iraq','iran','syria','israel','palestin','gaza','hamas','hezbollah','lebanon','jordan',
    'afghanistan','pakistan','india','china','japan','korea','north korea','south korea','taiwan',
    'russia','ukraine','crimea','putin','moscow','eu','europe','nato','united nations','un ','u.n.',
    'britain','uk ','london','france','germany','italy','spain','greece','turkey','egypt','libya',
    'saudi','yemen','qatar','uae','kuwait','bahrain','oman','sudan','somalia','nigeria','kenya','ethiopia','south africa',
    'mexico','brazil','argentina','venezuela','colombia','peru','chile','cuba','haiti',
    'refugee','migrant','asylum','border','sanction','diplom','election','parliament','president','prime minister',
    'militant','rebels','bomb','attack','terror','isis','islamic state','al qaeda','taliban','ceasefire','peace talks',
    'quake','earthquake','tsunami','flood','typhoon','hurricane'
]
exclude_kw = [
    'stock','stocks','wall st','wall street','nasdaq','dow','s&p','earnings','profit','bank','oil price','crude','economy','economic',
    'soccer','football','nba','nfl','mlb','nhl','tennis','golf','olympic','tournament','league','coach','player','match',
    'tech','technology','software','iphone','android','google','microsoft','apple','facebook','twitter','chip','semiconductor','startup',
    'science','scientist','research','nasa','space','telescope','quantum','genome','climate'
]

def is_world(text):
    t = (text or '').lower()
    score = 0
    for k in world_kw:
        if k in t:
            score += 1
    for k in exclude_kw:
        if k in t:
            score -= 1
    return score >= 1

text = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['is_world'] = text.map(is_world)

world_df = df[df['is_world']]
counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)

if counts.empty:
    ans = None
else:
    top_region = counts.index[0]
    ans = str(top_region)

print('__RESULT__:')
print(json.dumps({'top_region': ans, 'counts_top5': counts.head(5).to_dict(), 'world_total': int(world_df.shape[0])}))"""

env_args = {'var_call_ycD5Tn2PvYb9A119GxQY5n9w': 'file_storage/call_ycD5Tn2PvYb9A119GxQY5n9w.json', 'var_call_YXGYT2sREtdoS9rXJDNwnswl': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

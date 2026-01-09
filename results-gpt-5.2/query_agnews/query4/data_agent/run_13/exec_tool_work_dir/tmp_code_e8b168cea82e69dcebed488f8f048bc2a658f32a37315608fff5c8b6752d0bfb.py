code = """import json, pandas as pd

# load 2015 metadata rows
meta_src = var_call_wV3gjoYP2B3ploMC7C2LSZP8
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_xk6YKreE2nE9FcbcMJhOfiGk

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(str)
arts_df['article_id'] = arts_df['article_id'].astype(str)

# join
df = meta_df.merge(arts_df, on='article_id', how='left')

def categorize(text):
    if text is None:
        text = ''
    t = str(text).lower()
    world_kw = [
        'iraq','israel','palestin','gaza','hamas','hezbollah','iran','syria','assad','russia','ukraine','crimea',
        'china','japan','korea','north korea','pakistan','india','afghanistan','taliban','al qaeda','isis','islamic state',
        'europe','eu ','eurozone','united nations','u.n.','nato','britain','uk ','france','germany','spain','italy',
        'turkey','saudi','yemen','egypt','libya','sudan','congo','nigeria','kenya','somalia','south africa','zimbabwe',
        'mexico','canada','brazil','argentina','venezuela','chile','peru','colombia',
        'pope','vatican','refugee','migrant','earthquake','tsunami','typhoon','ebola','cholera','coup','election',
        'terror','bomb','hostage','sanction','diplomat','minister','president'
    ]
    sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','hockey','baseball','basketball']
    biz_kw = ['stock','wall st','nasdaq','dow','earnings','profit','revenue','oil','crude','market','bank','bond','inflation','economy','merger','acquisition','ipo','carlyle','aerospace']
    sci_kw = ['science','tech','technology','software','internet','google','microsoft','apple','iphone','android','nasa','space','satellite','robot','ai','quantum','biotech','genome','climate']

    score = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for kw in world_kw:
        if kw in t:
            score['World'] += 1
    for kw in sports_kw:
        if kw in t:
            score['Sports'] += 1
    for kw in biz_kw:
        if kw in t:
            score['Business'] += 1
    for kw in sci_kw:
        if kw in t:
            score['Science/Technology'] += 1

    # if no keywords, default to World (broad news)
    if max(score.values()) == 0:
        return 'World'
    return max(score, key=score.get)

# categorize using title + description
combined = (df['title'].fillna('') + ' ' + df['description'].fillna('')).tolist()
df['category'] = [categorize(x) for x in combined]

world_df = df[df['category']=='World']
counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)

if counts.empty:
    result = {'region': None, 'world_articles_2015': 0}
else:
    top_region = counts.index[0]
    result = {'region': str(top_region), 'world_articles_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wV3gjoYP2B3ploMC7C2LSZP8': 'file_storage/call_wV3gjoYP2B3ploMC7C2LSZP8.json', 'var_call_xk6YKreE2nE9FcbcMJhOfiGk': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

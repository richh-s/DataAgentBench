code = """import json, pandas as pd

# load 2015 metadata
md = var_call_UY4nM2ksgxmtTPbAZhgwqt3J
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)
mdf = pd.DataFrame(md)
# normalize types
mdf['article_id'] = mdf['article_id'].astype(int)

# load articles
arts = var_call_7MUA1BvG2dOdqghqJfdivY6q
adf = pd.DataFrame(arts)
adf['article_id'] = adf['article_id'].astype(int)

# join
j = mdf.merge(adf, on='article_id', how='inner')
text = (j['title'].fillna('') + ' ' + j['description'].fillna('')).str.lower()

# simple keyword-based classifier for 4 categories
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','russia','ukraine','crimea','syria','assad',
    'afghanistan','pakistan','india','china','beijing','taiwan','japan','tokyo','korea','seoul','north korea',
    'eu','european union','nato','united nations','u.n.','pope','vatican','germany','france','britain','london',
    'turkey','ankara','egypt','cairo','saudi','yemen','libya','sudan','nigeria','kenya','somalia','congo',
    'australia','canada','mexico','brazil','argentina','venezuela','colombia','peru','chile',
    'prime minister','president','election','rebel','militant','bomb','attack','terror','hostage','sanction','refugee'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','baseball','hockey','championship','league','coach','player','match','tournament']
biz_kw = ['stock','wall st','wall street','market','shares','earnings','profit','revenue','fed','interest rate','inflation','economy','oil','crude','opec','dollar','euro','bank','merger','acquisition','ipo','company','ceo','carlyle']
sci_kw = ['science','scientist','research','study','space','nasa','mars','satellite','technology','tech','internet','software','hardware','iphone','google','microsoft','ai','robot','quantum','biotech','vaccine','virus','genome']

def score(txt, kws):
    s = 0
    for kw in kws:
        if kw in txt:
            s += 1
    return s

scores = pd.DataFrame({
    'world': text.apply(lambda t: score(t, world_kw)),
    'sports': text.apply(lambda t: score(t, sports_kw)),
    'business': text.apply(lambda t: score(t, biz_kw)),
    'science_tech': text.apply(lambda t: score(t, sci_kw)),
})

# assign category by max score, default business if all zero (common in dataset), but keep deterministic
cats = scores.idxmax(axis=1)
# if all zeros -> business (fallback)
all_zero = (scores.max(axis=1) == 0)
cats = cats.mask(all_zero, 'business')

j['category'] = cats.replace({'science_tech':'Science/Technology','world':'World','sports':'Sports','business':'Business'})

world = j[j['category']=='World']
res = world.groupby('region', dropna=False).size().sort_values(ascending=False)

if len(res)==0:
    out = {'region': None, 'count': 0}
else:
    out = {'region': res.index[0], 'count': int(res.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UY4nM2ksgxmtTPbAZhgwqt3J': 'file_storage/call_UY4nM2ksgxmtTPbAZhgwqt3J.json', 'var_call_7MUA1BvG2dOdqghqJfdivY6q': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

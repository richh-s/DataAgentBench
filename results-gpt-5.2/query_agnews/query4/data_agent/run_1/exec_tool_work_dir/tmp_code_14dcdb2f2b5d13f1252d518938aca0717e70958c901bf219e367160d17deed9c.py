code = """import json, pandas as pd

# Load 2015 metadata (possibly from file)
meta_src = var_call_3fH6Y7IUvrEGHKFSQlM98d3L
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_bsTf5CoSzmcKuw0pu5P2QuXa

mdf = pd.DataFrame(meta)
adf = pd.DataFrame(arts)

# Normalize types
mdf['article_id'] = mdf['article_id'].astype(int)
adf['article_id'] = adf['article_id'].astype(int)

# Merge
df = mdf.merge(adf, on='article_id', how='inner')

# Simple rule-based categorization via keywords in title+description
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

def is_world(s):
    world_kw = [
        'iraq','iran','israel','palest','gaza','hamas','hezb','leban','syria','turkey','ukraine','russia','moscow',
        'china','beijing','japan','tokyo','korea','seoul','north korea','south korea','india','pakistan','afghan',
        'european union','eu ','nato','un ','u.n.','united nations','germany','france','britain','uk ','london',
        'italy','spain','greece','sweden','norway','finland','denmark','poland','hungary','romania','serbia',
        'australia','canada','mexico','brazil','argentina','venezuela','colombia','peru','chile','bolivia',
        'africa','nigeria','kenya','somalia','sudan','egypt','libya','algeria','morocco','tunisia','south africa',
        'earthquake','tsunami','flood','cyclone','typhoon','refugee','migrant','asylum','border','sanction',
        'military','troops','rebel','insurgent','ceasefire','peace talks','election','parliament','president',
        'prime minister','embassy','terror','bomb','attack','hostage','war','killed','dead'
    ]
    for kw in world_kw:
        if kw in s:
            return True
    return False

# Exclude obvious non-world via strong keywords
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','world cup','olympic','tennis','golf','cricket','fifa','uefa','league','coach','tournament','match','final','semifinal','quarterfinal']
biz_kw = ['stocks','wall st','wall street','earnings','revenue','profit','loss','ipo','shares','bond','oil price','crude','brent','market','economy','inflation','interest rate','fed','bank','merger','acquisition','ceo','company','quarter','forecast']
tech_kw = ['software','hardware','app','iphone','android','google','microsoft','apple','facebook','amazon','ai','artificial intelligence','chip','semiconductor','robot','satellite','nasa','space','science','research','study','virus','vaccine','clinical','genome','quantum']


def has_any(s, kws):
    return any(kw in s for kw in kws)

cats = []
for s in text.tolist():
    if has_any(s, sports_kw):
        cats.append('Sports')
    elif has_any(s, tech_kw):
        cats.append('Science/Technology')
    elif has_any(s, biz_kw):
        cats.append('Business')
    elif is_world(s):
        cats.append('World')
    else:
        # fallback: if mentions a country/city/politics/disaster -> World else Business (generic Reuters)
        cats.append('World' if is_world(s) else 'Business')

df['category'] = cats

world_2015 = df[df['category']=='World']
counts = world_2015.groupby('region', dropna=False)['article_id'].nunique().sort_values(ascending=False)

if counts.empty:
    top_region = None
else:
    top_region = counts.index[0]

out = {
    'top_region': None if pd.isna(top_region) else str(top_region),
    'world_article_counts_by_region': counts.astype(int).to_dict()
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3fH6Y7IUvrEGHKFSQlM98d3L': 'file_storage/call_3fH6Y7IUvrEGHKFSQlM98d3L.json', 'var_call_bsTf5CoSzmcKuw0pu5P2QuXa': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

# Load 2015 metadata
path = var_call_I2aaARK8p9LFyEYhDD4PWQCz
with open(path, 'r') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)

art_df = pd.DataFrame(var_call_0YIYTHfk9OyHZGztqgyetyp0)

# Join
df = meta_df.merge(art_df, on='article_id', how='inner')

# Simple keyword-based classifier
world_kw = [
    'iraq','iran','syria','israel','palestine','gaza','ukraine','russia','putin','kremlin',
    'china','beijing','japan','korea','north korea','kim','india','pakistan','afghanistan',
    'european union','eu ','nato','united nations','u.n.','un ','refugee','migrant',
    'terror','bomb','militant','war','ceasefire','election','parliament','president',
    'prime minister','diplomat','embassy','sanction','coup','protest','border','minister'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','baseball','hockey','basketball','world cup','championship','coach','quarterback','goal','match']
biz_kw = ['stock','wall st','earnings','profit','revenue','ipo','shares','bond','market','dow','nasdaq','s&p','oil','crude','opec','bank','fed','interest rate','inflation','gdp','economy','merger','acquisition','aerospace','company','firm','retail','sales']
sci_kw = ['google','apple','microsoft','amazon','facebook','twitter','tesla','nasa','mars','space','rocket','satellite','software','hardware','ai','artificial intelligence','robot','cyber','hack','quantum','genome','dna','vaccine','virus','climate','temperature','scientist','technology','tech']

def classify(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    def has_any(kws):
        return any(k in text for k in kws)
    # Priority to sports if strong sports terms present
    if has_any(sports_kw):
        return 'Sports'
    if has_any(biz_kw):
        return 'Business'
    if has_any(sci_kw):
        return 'Science/Technology'
    if has_any(world_kw):
        return 'World'
    # default heuristic: if mentions country/region words, treat as World else Business
    if any(k in text for k in ['iraq','china','russia','europe','asia','africa','america','u.s.','us ','u.k.','uk ']):
        return 'World'
    return 'Business'

df['category'] = df.apply(classify, axis=1)
world_df = df[df['category']=='World']

counts = world_df.groupby('region').size().sort_values(ascending=False)
if len(counts)==0:
    ans = None
else:
    ans = {'region': counts.index[0], 'world_article_count_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_I2aaARK8p9LFyEYhDD4PWQCz': 'file_storage/call_I2aaARK8p9LFyEYhDD4PWQCz.json', 'var_call_0YIYTHfk9OyHZGztqgyetyp0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

# Load metadata 2015 from file
path = var_call_KXKlgG8XVi0m97x3kJqXcBGd
with open(path, 'r', encoding='utf-8') as f:
    meta = json.load(f)

arts = var_call_WToo0NUa0jexhRwOrzn1QyZ4

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
for c in ['article_id']:
    meta_df[c] = meta_df[c].astype(str)
    arts_df[c] = arts_df[c].astype(str)

df = meta_df.merge(arts_df, on='article_id', how='left')

# Keyword-based categorization
world_kw = [
    'iraq','iran','syria','israel','palestin','gaza','ukraine','russia','putin','china','beijing','japan','korea','north korea','south korea',
    'pakistan','india','afghanistan','taliban','nato','un','united nations','eu','european union','brexit','pope','vatican','refugee','migrant',
    'election','president','prime minister','government','parliament','minister','embassy','terror','militant','bomb','attack','war','ceasefire',
    'diplomat','sanction','coup','protest','riot','killed','hostage','missile','nuclear','aid','peace','rebel'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','baseball','hockey','basketball','coach','tournament','cup','match','league','won','beat']
business_kw = ['stock','stocks','wall street','market','oil','prices','shares','earnings','profit','bank','inflation','economy','economic','trade','company','deal','merger','acquisition','ipo','revenue','sales','fund','investment','carlyle','airline','aerospace']
sci_kw = ['science','scientist','research','study','space','nasa','mars','satellite','technology','tech','computer','software','internet','smartphone','ai','robot','chip','biotech','genome','climate','warming']

def categorize(text):
    t = (text or '').lower()
    scores = {
        'World': sum(1 for k in world_kw if k in t),
        'Sports': sum(1 for k in sports_kw if k in t),
        'Business': sum(1 for k in business_kw if k in t),
        'Science/Technology': sum(1 for k in sci_kw if k in t),
    }
    # choose max; if all zero, default to World? better: Unknown
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return 'Unknown'
    return best

combo = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = combo.map(categorize)

world_df = df[df['category']=='World']
counts = world_df.groupby('region').size().sort_values(ascending=False)

if len(counts)==0:
    result = {'region': None, 'world_article_count': 0}
else:
    top_region = counts.index[0]
    result = {'region': top_region, 'world_article_count': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KXKlgG8XVi0m97x3kJqXcBGd': 'file_storage/call_KXKlgG8XVi0m97x3kJqXcBGd.json', 'var_call_WToo0NUa0jexhRwOrzn1QyZ4': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

def load_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

meta = load_maybe_path(var_call_wJFNOsnk998jhVcF2Pnyl6je)
arts = load_maybe_path(var_call_IrLGG9aXxfoMzXTN4r9sVQAR)

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# normalize types
for c in ['article_id']:
    df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce')

df = df_meta.merge(df_arts, on='article_id', how='inner')

# Simple rule-based categorization
world_keywords = [
    'iraq','iran','syria','israel','palestin','gaza','ukraine','russia','putin','moscow','kremlin',
    'china','beijing','japan','tokyo','north korea','south korea','seoul','pyongyang',
    'india','pakistan','afghanistan','taliban','kabul',
    'europe','eu ','european','britain','uk ','london','france','paris','germany','berlin',
    'italy','spain','greece','nato','united nations','u.n.','un ','asean',
    'terror','bomb','blast','militant','rebel','insurgent','jihad',
    'election','president','prime minister','parliament','government','minister','diplomat','sanction',
    'quake','earthquake','tsunami','flood','hurricane','cyclone',
    'africa','nigeria','kenya','sudan','congo','somalia','egypt'
]

sports_keywords = ['nba','nfl','mlb','nhl','soccer','football','world cup','olympic','tennis','golf','cricket','fifa','uefa','champions league','coach','tournament']
business_keywords = ['stocks','shares','wall st','wall street','dow','nasdaq','s&p','earnings','profit','revenue','ipo','oil','crude','opec','economy','inflation','bank','fed','interest rate','merger','acquisition']
tech_keywords = ['software','internet','smartphone','iphone','android','microsoft','google','apple','facebook','twitter','ai','chip','semiconductor','nasa','space','mars','robot','biotech','genome','science','technology']

def classify(text):
    t = (text or '').lower()
    scores = {
        'World': sum(k in t for k in world_keywords),
        'Sports': sum(k in t for k in sports_keywords),
        'Business': sum(k in t for k in business_keywords),
        'Science/Technology': sum(k in t for k in tech_keywords),
    }
    # choose max; break ties by priority order
    order = ['World','Business','Sports','Science/Technology']
    best = max(order, key=lambda k: (scores[k], -order.index(k)))
    # if all zero, default to World? better mark as Unknown
    if max(scores.values())==0:
        return 'Unknown'
    return best

text = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = text.map(classify)

world_df = df[df['category']=='World']
counts = world_df.groupby('region', dropna=False)['article_id'].nunique().sort_values(ascending=False)

if len(counts)==0:
    result = {'region': None, 'world_article_count': 0}
else:
    top_region = counts.index[0]
    top_count = int(counts.iloc[0])
    result = {'region': str(top_region), 'world_article_count': top_count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wJFNOsnk998jhVcF2Pnyl6je': 'file_storage/call_wJFNOsnk998jhVcF2Pnyl6je.json', 'var_call_IrLGG9aXxfoMzXTN4r9sVQAR': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

meta_src = var_call_pjaZGeavMDThCV0rQXzaYPeD
arts_src = var_call_CacCHOiEm9fy4EUpjQyewdOW

# load meta (may be file path)
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = arts_src

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# normalize ids to int
for c in ['article_id']:
    if c in df_meta.columns:
        df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    if c in df_arts.columns:
        df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce')

# join only 2015 metadata
df = df_meta.merge(df_arts, on='article_id', how='inner')

# simple keyword-based categorization
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','syria','syrian','lebanon','jordan',
    'afghanistan','taliban','pakistan','india','kashmir','china','beijing','hong kong','taiwan','japan','tokyo','korea','seoul','pyongyang',
    'russia','moscow','ukraine','crimea','putin','europe','eurozone','greece','italy','france','germany','britain','uk','london','spain','portugal',
    'turkey','ankara','egypt','cairo','libya','yemen','saudi','qatar','uae','emirates','kuwait','oman',
    'nigeria','kenya','south africa','sudan','somalia','ethiopia',
    'un ','united nations','nato','eu ','european union','asean','sanctions','summit','diplomat','embassy','border','refugee','migrant',
    'president','prime minister','parliament','election','protest','rebels','militants','bomb','attack','ceasefire','war','troops','missile','nuclear'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','tennis','golf','cricket','formula','f1','grand prix','world cup','league','match','tournament','coach','player','championship']
biz_kw = ['stocks','wall st','wall street','market','shares','earnings','profit','revenue','ipo','bank','banks','fed','interest rate','inflation','economy','economic','trade','tariff','oil','crude','dollar','euro','yen','merger','acquisition','buyout','carlyle','fund','investment','company','ceo']
sci_kw = ['science','scientists','research','study','space','nasa','rocket','mars','planet','telescope','physics','chemistry','biotech','gene','genetic','dna','medical','medicine','virus','vaccine','technology','tech','software','internet','computer','smartphone','ai','artificial intelligence']

from collections import Counter

def classify(text):
    t = (text or '').lower()
    # score by keyword hits
    scores = {
        'World': sum(1 for k in world_kw if k in t),
        'Sports': sum(1 for k in sports_kw if k in t),
        'Business': sum(1 for k in biz_kw if k in t),
        'Science/Technology': sum(1 for k in sci_kw if k in t),
    }
    # pick max; tie-breaker priority: World>Business>Sports>Sci/Tech
    mx = max(scores.values())
    top = [k for k,v in scores.items() if v==mx]
    if mx==0:
        # fallback: if mentions country-like terms in title/desc treat as World else Business
        return 'Business'
    priority = ['World','Business','Sports','Science/Technology']
    for p in priority:
        if p in top:
            return p

# build text
text = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = text.map(classify)

world_df = df[df['category']=='World']
counts = world_df.groupby('region', dropna=False).size().sort_values(ascending=False)

if counts.empty:
    out = {"region": None, "world_article_count": 0}
else:
    region = counts.index[0]
    out = {"region": str(region), "world_article_count": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pjaZGeavMDThCV0rQXzaYPeD': 'file_storage/call_pjaZGeavMDThCV0rQXzaYPeD.json', 'var_call_CacCHOiEm9fy4EUpjQyewdOW': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd

# load 2015 metadata
path = var_call_pko2MVCjq9SeexGGs8FS2HLm
with open(path, 'r') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(str)

articles_df = pd.DataFrame(var_call_ptVZoLpmEimNOTyBTAh8g7eX)
articles_df['article_id'] = articles_df['article_id'].astype(str)

# join
df = meta_df.merge(articles_df, on='article_id', how='inner')

# keyword-based classification
world_kw = [
    'iraq','iran','syria','israel','palestin','gaza','lebanon','jordan','egypt','afghan','pakistan','india','china','japan','korea','russia','ukrain','europe','eu ','e.u','britain','uk ','france','germany','spain','italy','greece','turkey','saudi','yemen','qatar','uae','emirates','kuwait','oman','bahrain','libya','tunisia','algeria','morocco','sudan','somalia','kenya','nigeria','congo','south africa','zimbabwe','uganda','rwanda','burundi','ethiopia',
    'united nations','u.n','nato','pope','vatican','refugee','migrant','immigration','border','coup','election','parliament','prime minister','president','rebels','militant','terror','bomb','attack','war','ceasefire','peace talks','sanctions','diplomat','embassy','hostage'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','golf','tennis','olympic','cricket','rugby','formula','nascar','cup','league','tournament','championship','coach','match','win','loss','score']
business_kw = ['stocks','shares','wall st','wall street','market','earnings','profit','revenue','ipo','merger','acquisition','deal','bank','fed','interest rate','inflation','economy','economic','oil','crude','prices','company','billion','million','dollar','invest','fund','hedge','trade','tariff']
science_kw = ['science','scientist','research','study','space','nasa','mars','satellite','rocket','technology','tech','internet','software','hardware','smartphone','iphone','android','google','microsoft','apple','facebook','ai','artificial intelligence','robot','climate','carbon','gene','dna','vaccine','virus','medical','health']

def classify(text):
    t = (text or '').lower()
    scores = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for kw in world_kw:
        if kw in t:
            scores['World'] += 1
    for kw in sports_kw:
        if kw in t:
            scores['Sports'] += 1
    for kw in business_kw:
        if kw in t:
            scores['Business'] += 1
    for kw in science_kw:
        if kw in t:
            scores['Science/Technology'] += 1
    # choose max; if all zero, default to Business as many are financial; but keep 'Unknown'
    mx = max(scores.values())
    if mx == 0:
        return 'Unknown'
    return max(scores, key=scores.get)

combo = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['category'] = combo.map(classify)
world_df = df[df['category']=='World']

counts = world_df.groupby('region').size().sort_values(ascending=False)
if len(counts)==0:
    ans = {'region': None, 'world_articles_2015': 0}
else:
    ans = {'region': counts.index[0], 'world_articles_2015': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_pko2MVCjq9SeexGGs8FS2HLm': 'file_storage/call_pko2MVCjq9SeexGGs8FS2HLm.json', 'var_call_ptVZoLpmEimNOTyBTAh8g7eX': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

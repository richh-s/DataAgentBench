code = """import json, pandas as pd

# load metadata 2015 (may be file path)
meta_src = var_call_ZyJcNSBmZyBihSNO46o2itYi
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_C3PMctThITbDLNMwIwYkuhiT

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# normalize ids to int
for df in (df_meta, df_arts):
    df['article_id'] = df['article_id'].astype(int)

# join
df = df_meta.merge(df_arts, on='article_id', how='inner')

# simple keyword-based classifier
world_kw = [
    'iraq','iran','israel','palestin','gaza','hamas','hezbollah','syria','syrian','russia','ukraine','crimea',
    'china','beijing','hong kong','japan','tokyo','korea','seoul','north korea','kim jong','pakistan','india','delhi',
    'afghanistan','taliban','saudi','yemen','egypt','turkey','erdogan','europe','eu ','e.u.','britain','uk ','london',
    'france','germany','merkel','spain','italy','greek','greece','pope','vatican','un ','u.n.','united nations',
    'nato','isis','islamic state','terror','militant','rebels','election','prime minister','president','parliament',
    'refugee','migrant','border','sanction','diplomat','embassy','summit'
]
sports_kw = ['nba','nfl','mlb','nhl','soccer','football','cricket','tennis','golf','olympic','fifa','uefa','world cup','match','tournament','coach','league','goal','scored']
biz_kw = ['stocks','shares','wall st','wall street','market','earnings','profit','revenue','ipo','merger','acquisition','oil','crude','economy','gdp','inflation','fed','central bank','bond','currency','dollar','euro','yen','company','corporate','bank','billion','million']
sci_kw = ['science','scientist','research','study','space','nasa','mars','rocket','satellite','technology','tech','software','hardware','internet','ai','artificial intelligence','robot','smartphone','chip','semiconductor','quantum','medical','health','vaccine','disease','climate','carbon']

def score(text, kws):
    s=0
    for k in kws:
        if k in text:
            s += 1
    return s

def categorize(row):
    text = (str(row.get('title',''))+' '+str(row.get('description',''))).lower()
    scores = {
        'World': score(text, world_kw),
        'Sports': score(text, sports_kw),
        'Business': score(text, biz_kw),
        'Science/Technology': score(text, sci_kw)
    }
    # tie-breaker: prefer World if it has any score and is tied
    mx = max(scores.values())
    top = [k for k,v in scores.items() if v==mx]
    if mx==0:
        # fallback heuristics
        if 'reuters' in text or 'afp' in text:
            return 'World'
        return 'Business'
    if len(top)==1:
        return top[0]
    if 'World' in top:
        return 'World'
    return top[0]

df['category'] = df.apply(categorize, axis=1)
world_df = df[df['category']=='World']
counts = world_df.groupby('region').size().sort_values(ascending=False)
if counts.empty:
    res = {'region': None, 'count': 0}
else:
    res = {'region': counts.index[0], 'count': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_ZyJcNSBmZyBihSNO46o2itYi': 'file_storage/call_ZyJcNSBmZyBihSNO46o2itYi.json', 'var_call_C3PMctThITbDLNMwIwYkuhiT': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

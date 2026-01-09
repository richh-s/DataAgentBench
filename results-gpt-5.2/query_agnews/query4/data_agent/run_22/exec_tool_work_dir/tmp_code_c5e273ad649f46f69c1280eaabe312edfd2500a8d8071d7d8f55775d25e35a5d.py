code = """import json, pandas as pd

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

meta = load_json_maybe_path(var_call_Aw3dlOhJoq876XOFKZjW5l8X)
arts = load_json_maybe_path(var_call_cKxeYSZc4Si2Hfk0skN25qmb)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids to int
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# join
df = meta_df.merge(arts_df, on='article_id', how='inner')

def categorize(title, desc):
    t = ((title or '') + ' ' + (desc or '')).lower()
    world_kw = [
        'iraq','iran','israel','palestin','gaza','ukraine','russia','moscow','putin','kremlin',
        'china','beijing','xi','japan','tokyo','north korea','south korea','kim jong',
        'syria','assad','turkey','erdogan','european union','eu ','nato','united nations','u.n.',
        'refugee','migrant','immigration','border','election','parliament','prime minister','president',
        'minister','government','rebels','militia','terror','bomb','attack','hostage','war','ceasefire',
        'sanction','diplomat','embassy','coup','protest','clashes','pakistan','india','afghanistan',
        'saudi','yemen','egypt','libya','sudan','somalia','congo','nigeria','kenya','south africa',
        'france','germany','britain','uk ','london','spain','italy','greece','sweden','norway',
        'australia','canada','mexico','brazil','argentina','venezuela','colombia',
        'earthquake','tsunami','flood','hurricane','disaster'
    ]
    sports_kw = ['vs.','nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','fifa','uefa','world cup','championship','league','coach','player','match','tournament','goal','season']
    biz_kw = ['stock','stocks','wall st','wall street','reuters -','earnings','profit','loss','revenue','ipo','shares','bond','treasury','fed','interest rate','inflation','economy','economic','gdp','bank','oil','crude','barrel','price','merger','acquisition','deal','company','corp','inc','market','dow','nasdaq','s&p','fund','investment']
    sci_kw = ['nasa','space','rocket','satellite','mars','planet','telescope','physics','quantum','gene','genetic','dna','virus','vaccine','cancer','climate','warming','carbon','temperature','species','robot','ai','artificial intelligence','software','internet','chip','semiconductor','smartphone','technology','tech','cyber','hack','battery','electric vehicle']

    def score(kws):
        s = 0
        for kw in kws:
            if kw in t:
                s += 1
        return s

    scores = {
        'World': score(world_kw),
        'Sports': score(sports_kw),
        'Business': score(biz_kw),
        'Science/Technology': score(sci_kw)
    }
    # tie-breaker: if contains clear sports terms prioritize sports; else business; else sci; else world if any
    best = max(scores, key=lambda k: scores[k])
    if scores[best] == 0:
        # fallback simple rules
        if any(k in t for k in sports_kw):
            best = 'Sports'
        elif any(k in t for k in biz_kw):
            best = 'Business'
        elif any(k in t for k in sci_kw):
            best = 'Science/Technology'
        else:
            best = 'World'
    return best

df['category'] = [categorize(r.title, r.description) for r in df.itertuples(index=False)]
world_df = df[df['category'] == 'World']
counts = world_df.groupby('region').size().sort_values(ascending=False)

if len(counts)==0:
    result = {'region': None, 'world_article_count': 0}
else:
    top_region = counts.index[0]
    result = {'region': str(top_region), 'world_article_count': int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Aw3dlOhJoq876XOFKZjW5l8X': 'file_storage/call_Aw3dlOhJoq876XOFKZjW5l8X.json', 'var_call_cKxeYSZc4Si2Hfk0skN25qmb': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

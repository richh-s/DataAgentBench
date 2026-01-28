code = """import json, pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

meta = load_records(var_call_LBvKtnVJYhiHdCZncRbfFXtE)
arts = load_records(var_call_kf9d25waZoTS1ieZhIQV8vlI)

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# Normalize types
for c in ['article_id']:
    df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce')

df = df_meta.merge(df_arts, on='article_id', how='inner')

world_kw = [
    'iraq','iran','israel','palest','gaza','hamas','hezbollah','syria','lebanon','jordan','yemen',
    'afghanistan','pakistan','india','china','taiwan','japan','korea','north korea','south korea',
    'russia','ukraine','crimea','putin','moscow','nato','european union','eu','britain','uk','england','france','germany','italy','spain','greece',
    'turkey','saudi','qatar','uae','emirates','kuwait','bahrain','oman','egypt','libya','tunisia','algeria','morocco','sudan','somalia','kenya','nigeria','congo','south africa',
    'mexico','canada','brazil','argentina','venezuela','colombia','peru','chile',
    'united nations','u.n.','un ','nuclear','sanction','diplomat','embassy','election','protest','attack','bomb','militant','war','ceasefire','refugee','immigrant','migration',
    'quake','earthquake','tsunami','flood','hurricane','typhoon',
    'pope','vatican'
]

sports_kw = ['nba','nfl','mlb','nhl','soccer','football','fifa','uefa','olympic','olympics','world cup','tennis','golf','cricket','rugby','baseball','hockey','basketball','final','tournament','coach','match','season','player','team','goal']

bus_kw = ['stock','shares','wall st','dow','nasdaq','s&p','earnings','profit','revenue','merger','acquisition','ipo','bond','rates','inflation','economy','gdp','market','oil','crude','gold','dollar','euro','yen','bank','fed','central bank','company','corporate']

sci_kw = ['science','scientist','research','study','space','nasa','mars','satellite','telescope','physics','chemistry','biology','medical','medicine','health','virus','vaccine','cancer','genome','climate','global warming','technology','tech','software','hardware','internet','app','iphone','android','computer','ai','robot','chip','semiconductor']

import re

def score(text, kws):
    s = 0
    for kw in kws:
        if kw in text:
            s += 1
    return s

def classify(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    # remove punctuation-ish for better phrase matching
    text = re.sub(r'[^a-z0-9\s\.]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    scores = {
        'World': score(text, world_kw),
        'Sports': score(text, sports_kw),
        'Business': score(text, bus_kw),
        'Science/Technology': score(text, sci_kw),
    }
    # Default: pick max; if all zero, heuristics: Reuters/AFP often world/business; use a few cues
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        if any(k in text for k in ['reuters', 'afp', 'u.s.', 'us ', 'united states', 'president', 'minister', 'police', 'killed']):
            best_cat = 'World'
        else:
            best_cat = 'Business'
    return best_cat

df['category'] = [classify(t,d) for t,d in zip(df.get('title',''), df.get('description',''))]

world_df = df[df['category']=='World']
res = (world_df.groupby('region', dropna=False)['article_id']
       .count()
       .sort_values(ascending=False))

if len(res)==0:
    out = {'region': None, 'world_article_count_2015': 0}
else:
    top_region = res.index[0]
    top_count = int(res.iloc[0])
    out = {'region': None if pd.isna(top_region) else str(top_region), 'world_article_count_2015': top_count}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LBvKtnVJYhiHdCZncRbfFXtE': 'file_storage/call_LBvKtnVJYhiHdCZncRbfFXtE.json', 'var_call_kf9d25waZoTS1ieZhIQV8vlI': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

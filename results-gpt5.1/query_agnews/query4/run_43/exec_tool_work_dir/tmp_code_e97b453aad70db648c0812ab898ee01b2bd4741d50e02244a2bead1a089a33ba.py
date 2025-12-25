code = """import json, pandas as pd

# Load full metadata from file
path_meta = var_call_o0ofpIaMk5a89G4xrWN22zPd
with open(path_meta, 'r') as f:
    meta = json.load(f)

articles = var_call_cfz03RWYkodne9FFRjvS9nIf

meta_df = pd.DataFrame(meta)
art_df = pd.DataFrame(articles)

# Filter metadata for 2015
meta_df['year'] = meta_df['publication_date'].str[:4]
meta_2015 = meta_df[meta_df['year'] == '2015'][['article_id','region']]

# Simple keyword-based classifier for World category
# Tags for each category
world_kw = ['iraq','election','president','government','war','minister','united nations','un','parliament','israel','palestinian','conflict','bomb','attack','killed','u.n.','world leaders','diplomat','taliban','afghanistan','security council','summit']
sports_kw = ['game','games','team','win','victory','season','football','soccer','nba','nfl','mlb','tennis','golf','olympics','coach','player','league','tournament']
business_kw = ['stocks','stock','shares','wall st','wall street','investors','market','markets','economy','economic','profit','profits','loss','nyse','nasdaq','bond','bonds','loan','loans','trade','trading','merger','acquisition','ipo','oil prices','crude','currency']
scitech_kw = ['researchers','scientists','study','studies','nasa','space','planet','galaxy','star','technology','software','computer','computers','internet','online','virus','microsoft','apple','google','biology','genetics','physics']

def classify(text):
    if not isinstance(text, str):
        return None
    t = text.lower()
    scores = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for w in world_kw:
        if w in t: scores['World']+=1
    for w in sports_kw:
        if w in t: scores['Sports']+=1
    for w in business_kw:
        if w in t: scores['Business']+=1
    for w in scitech_kw:
        if w in t: scores['Science/Technology']+=1
    # default to World if all zero, since general news often world
    if max(scores.values())==0:
        return 'World'
    return max(scores, key=scores.get)

art_df['text'] = art_df['title'].fillna('')+' '+art_df['description'].fillna('')
art_df['category'] = art_df['text'].apply(classify)

# Merge
merged = pd.merge(meta_2015, art_df[['article_id','category']], on='article_id', how='inner')
world_2015 = merged[merged['category']=='World']
counts = world_2015.groupby('region').size().sort_values(ascending=False)

result = counts.index[0] if not counts.empty else None

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_o0ofpIaMk5a89G4xrWN22zPd': 'file_storage/call_o0ofpIaMk5a89G4xrWN22zPd.json', 'var_call_cfz03RWYkodne9FFRjvS9nIf': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

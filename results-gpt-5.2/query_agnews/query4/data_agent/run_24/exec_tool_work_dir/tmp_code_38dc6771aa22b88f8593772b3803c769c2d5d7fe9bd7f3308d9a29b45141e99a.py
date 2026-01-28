code = """import json, pandas as pd

meta_path = var_call_TV9OfqVUGOHZLFL9yISQeJpu
with open(meta_path, 'r', encoding='utf-8') as f:
    meta = json.load(f)
arts = var_call_TMjmadaVBLIaO4Cpcuv2Ies7

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# normalize types
for c in ['article_id']:
    df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce')

df = df_meta.merge(df_arts, on='article_id', how='inner')

def categorize(title, desc):
    t = (title or '')
    d = (desc or '')
    s = (t + ' ' + d).lower()

    sports_kw = ['nba','nfl','mlb','nhl','fifa','uefa','olympic','olympics','world cup','grand slam','tennis','soccer','football','basketball','baseball','golf','cricket','hockey','match','tournament','coach','player','league','championship']
    biz_kw = ['stock','stocks','wall st','wall street','nasdaq','dow','s&p','earnings','profit','revenue','ipo','bond','bonds','oil','crude','barrel','opec','economy','economic','inflation','gdp','bank','banks','interest rate','fed','merger','acquisition','share','shares','market','currency','dollar','euro','yen']
    sci_kw = ['science','scientist','research','study','technology','tech','software','hardware','internet','google','apple','microsoft','facebook','amazon','ai','artificial intelligence','robot','space','nasa','mars','satellite','climate','genome','dna','medical','medicine','health','vaccine','virus','cyber','security']
    
    def has_any(kws):
        return any(kw in s for kw in kws)

    if has_any(sports_kw):
        return 'Sports'
    if has_any(biz_kw):
        return 'Business'
    if has_any(sci_kw):
        return 'Science/Technology'
    return 'World'

df['category'] = [categorize(t, d) for t, d in zip(df['title'], df['description'])]
world = df[df['category']=='World']
counts = world.groupby('region', dropna=False).size().sort_values(ascending=False)

if len(counts)==0:
    result = {"region": None, "world_articles_2015": 0}
else:
    top_region = counts.index[0]
    result = {"region": str(top_region), "world_articles_2015": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TV9OfqVUGOHZLFL9yISQeJpu': 'file_storage/call_TV9OfqVUGOHZLFL9yISQeJpu.json', 'var_call_TMjmadaVBLIaO4Cpcuv2Ies7': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

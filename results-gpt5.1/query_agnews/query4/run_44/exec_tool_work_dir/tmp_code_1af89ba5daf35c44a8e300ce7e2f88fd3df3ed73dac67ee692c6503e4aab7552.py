code = """import json, pandas as pd

# Load full metadata result if it's a file path
def load_result(val):
    if isinstance(val, str) and val.endswith('.json'):
        with open(val, 'r') as f:
            return json.load(f)
    return val

articles = var_call_72XwPKBB4opW6TrUFVlvC6uF
metadata_2015 = load_result(var_call_yR8eGrFa4JKGr9bhAhs7QkiY)

# Create DataFrames
art_df = pd.DataFrame(articles)
meta_df = pd.DataFrame(metadata_2015)

# Ensure article_id types match
art_df['article_id'] = art_df['article_id'].astype(int)
meta_df['article_id'] = meta_df['article_id'].astype(int)

# Simple rule-based categorization into 4 categories using title+description
WORLD_KEYWORDS = ['iraq','election','war','president','prime minister','ceremony','government','rebel','militia','pipeline','export','world','united nations','u.n.','conflict','troops','bomb','terror','peace','diplomat','summit','border']
SPORTS_KEYWORDS = ['soccer','football','nba','nfl','mlb','hockey','olympic','tennis','golf','grand prix','fifa','world cup','tournament','league','coach','player','season','match','race','medal']
BUSINESS_KEYWORDS = ['stock','stocks','wall st','market','investor','investment','economy','economic','earnings','company','shares','profit','losses','merger','acquisition','ipo','bank','bond','crude','oil','price','prices','corporate']
SCI_TECH_KEYWORDS = ['science','research','study','experiment','technology','software','internet','computer','nasa','space','spaceship','rocket','biology','physics','chemistry','scientist','scientists','cell','genetic','genome']

def categorize(text):
    t = text.lower()
    scores = {'World':0,'Sports':0,'Business':0,'Science/Technology':0}
    for kw in WORLD_KEYWORDS:
        if kw in t:
            scores['World'] += 1
    for kw in SPORTS_KEYWORDS:
        if kw in t:
            scores['Sports'] += 1
    for kw in BUSINESS_KEYWORDS:
        if kw in t:
            scores['Business'] += 1
    for kw in SCI_TECH_KEYWORDS:
        if kw in t:
            scores['Science/Technology'] += 1
    # default to World if tie and no keywords
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return 'World'
    return best

art_df['text'] = (art_df['title'].fillna('') + ' ' + art_df['description'].fillna(''))
art_df['category'] = art_df['text'].apply(categorize)

# Filter to World category
world_articles = art_df[art_df['category']=='World'][['article_id']]

# Join with 2015 metadata
world_2015 = pd.merge(world_articles, meta_df, on='article_id', how='inner')

# Count by region
counts = world_2015.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = {'region': None, 'count': 0}
else:
    top_region = counts.index[0]
    result = {'region': top_region, 'count': int(counts.iloc[0])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_72XwPKBB4opW6TrUFVlvC6uF': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_yR8eGrFa4JKGr9bhAhs7QkiY': 'file_storage/call_yR8eGrFa4JKGr9bhAhs7QkiY.json'}

exec(code, env_args)

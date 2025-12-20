code = """import json, pandas as pd

# Load full metadata and articles from files
with open(var_call_I2aKvLr8aDvaDciLNQfwmksY, 'r') as f:
    metadata = json.load(f)
with open(var_call_Oaw9dSJ7IHXiG5Fj6jFS03Ht, 'r') as f:
    articles = json.load(f)

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

md_df['article_id'] = md_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Merge
df = md_df.merge(art_df, on='article_id', how='inner')

# Parse year
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Simple heuristic to classify categories based on title+description keywords
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

world_kw = ['iraq','korea','united nations','u.n.','afghanistan','election','palestinian','israel','china','european union','eu ','terror','bomb','government','president','prime minister','military','rebel','conflict','war','troops','nuclear','diplomat','summit']
sports_kw = ['nba','nfl','mlb','nhl','soccer','goal','inning','quarterback','touchdown','olympic','olympics','tennis','golf','race','racing','grand prix','football','basketball','baseball','hockey','coach','tournament','cup','league','finals','playoffs']
business_kw = ['stock','stocks','wall street','nasdaq','dow','s&p','market','shares','bond','bonds','fund','funds','bank','banks','ipo','merger','acquisition','oil','economy','economic','company','companies','profit','loss','earnings','revenue','sales','trade deficit','trade gap','currency','currencies']

cat = []
for t in text:
    c = 'Science/Technology'
    if any(k in t for k in sports_kw):
        c = 'Sports'
    elif any(k in t for k in business_kw):
        c = 'Business'
    elif any(k in t for k in world_kw):
        c = 'World'
    cat.append(c)

df['category'] = cat

world_2015 = df[(df['category']=='World') & (df['year']==2015)]

counts = world_2015.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = None
else:
    top_region = counts.index[0]
    result = top_region

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_I2aKvLr8aDvaDciLNQfwmksY': 'file_storage/call_I2aKvLr8aDvaDciLNQfwmksY.json', 'var_call_Oaw9dSJ7IHXiG5Fj6jFS03Ht': 'file_storage/call_Oaw9dSJ7IHXiG5Fj6jFS03Ht.json'}

exec(code, env_args)

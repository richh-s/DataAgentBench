code = """import json, pandas as pd

# Load full metadata
with open(var_call_Zi9vZRrGAfIGPG7bRIT61OtV, 'r') as f:
    metadata = json.load(f)

# Load full articles
with open(var_call_U5fioTI0w6m8INXtQxGC1XM7, 'r') as f:
    articles = json.load(f)

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

# Ensure types
md_df['article_id'] = md_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Filter to 2015
md_df['year'] = md_df['publication_date'].str.slice(0,4).astype(int)
md_2015 = md_df[md_df['year'] == 2015]

# Join
df = md_2015.merge(art_df, on='article_id', how='inner')

# Simple keyword-based classifier for World category
world_keywords = ['iraq','europe','asia','africa','war','election','president','government','minister','israel','palestinian','terror','united nations','u.n.','u.n','conflict','rebels','military','troops','bomb','attack','nuclear','diplomat','foreign','embassy','global','world','country','countries']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

def is_world(t):
    return any(w in t for w in world_keywords)

df['is_world'] = text.apply(is_world)

world_df = df[df['is_world']]

region_counts = world_df.groupby('region').size().sort_values(ascending=False)

if len(region_counts)==0:
    result = None
else:
    result = {"top_region": region_counts.index[0], "count": int(region_counts.iloc[0])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Zi9vZRrGAfIGPG7bRIT61OtV': 'file_storage/call_Zi9vZRrGAfIGPG7bRIT61OtV.json', 'var_call_U5fioTI0w6m8INXtQxGC1XM7': 'file_storage/call_U5fioTI0w6m8INXtQxGC1XM7.json'}

exec(code, env_args)

code = """import json, pandas as pd

# Load full results from JSON files
with open(var_call_OSPYpidg3I83pjpzkniSio5F, 'r') as f:
    meta_2015 = json.load(f)
with open(var_call_5ni973WqOo9jtPXgIXobZusd, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(meta_2015)
art_df = pd.DataFrame(articles)

# ensure article_id comparable types
meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Filter to 2015 world articles by simple keyword heuristics in title/description
world_keywords = ['iraq','afghanistan','united nations','u.n.','u.n','un ','european union','eu ','palestinian','israel','iran','sudan','russia','china','korea','election','terror','bomb','violence','clashes','war','conflict','military','president','prime minister','government','rebels','insurgents','troops']

text = (art_df['title'].fillna('') + ' ' + art_df['description'].fillna('')).str.lower()
mask_world = pd.Series(False, index=art_df.index)
for kw in world_keywords:
    mask_world |= text.str.contains(kw)

world_articles = art_df[mask_world]

# Join with metadata 2015
merged = pd.merge(meta_df, world_articles[['article_id']], on='article_id', how='inner')

# Count by region
counts = merged['region'].value_counts()

if counts.empty:
    answer = 'No World category articles from 2015 could be identified based on the available data.'
else:
    top_region = counts.idxmax()
    answer = top_region

res = json.dumps(answer)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_OSPYpidg3I83pjpzkniSio5F': 'file_storage/call_OSPYpidg3I83pjpzkniSio5F.json', 'var_call_5ni973WqOo9jtPXgIXobZusd': 'file_storage/call_5ni973WqOo9jtPXgIXobZusd.json'}

exec(code, env_args)

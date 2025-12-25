code = """import json, pandas as pd, os

# Load full results from files
with open(var_call_BNoTkJItEoV6Aykb8FZjUADx, 'r') as f:
    meta_2015 = json.load(f)
with open(var_call_CyOqxj4iGkyNDlRSeKzbT3L3, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(meta_2015)
articles_df = pd.DataFrame(articles)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge on article_id
merged = meta_df.merge(articles_df, on='article_id', how='inner')

# Simple keyword-based classifier for World category
world_keywords = ['iraq','europe','africa','asia','america','u.n.','united nations','israel','palestinian','election','war','terror','bomb','violence','minister','president','government','troops','rebels','conflict','crisis']

def is_world(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    return any(k in text for k in world_keywords)

merged['is_world'] = merged.apply(is_world, axis=1)

world_articles = merged[merged['is_world']]

# Count by region
counts = world_articles.groupby('region').size().sort_values(ascending=False)

if len(counts) == 0:
    result = {"region": None, "count": 0}
else:
    top_region = counts.index[0]
    top_count = int(counts.iloc[0])
    result = {"region": top_region, "count": top_count}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_BNoTkJItEoV6Aykb8FZjUADx': 'file_storage/call_BNoTkJItEoV6Aykb8FZjUADx.json', 'var_call_CyOqxj4iGkyNDlRSeKzbT3L3': 'file_storage/call_CyOqxj4iGkyNDlRSeKzbT3L3.json'}

exec(code, env_args)

code = """import json, pandas as pd

# Load metadata
with open(var_call_MmHxTYIovuY6Dn62sh5hMVs3, 'r') as f:
    meta = json.load(f)

# Load articles
with open(var_call_1PLiH4QLsNTQeEKuunURiA9S, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter for 2015
meta_2015 = meta_df[meta_df['publication_date'].str.startswith('2015-')]

# Merge with articles to get text
merged = meta_2015.merge(arts_df, on='article_id', how='inner')

# Very naive World-category classifier based on keywords
world_keywords = ['iraq','korea','china','japan','europe','africa','asia','war','united nations','u.n.','palestinian','israel','election','president','government','minister','terror','violence','military','nato','taliban','refugee','conflict','diplomat','embassy','parliament','protest','rally']

def is_world(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    return any(k in text for k in world_keywords)

merged['is_world'] = merged.apply(is_world, axis=1)
world_arts = merged[merged['is_world']]

counts = world_arts.groupby('region').size().sort_values(ascending=False)

result = {
    'counts_by_region': counts.to_dict(),
    'top_region': counts.idxmax() if not counts.empty else None
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MmHxTYIovuY6Dn62sh5hMVs3': 'file_storage/call_MmHxTYIovuY6Dn62sh5hMVs3.json', 'var_call_1PLiH4QLsNTQeEKuunURiA9S': 'file_storage/call_1PLiH4QLsNTQeEKuunURiA9S.json'}

exec(code, env_args)

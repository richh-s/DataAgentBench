code = """import json, pandas as pd

# Load full results from files
with open(var_call_XhZwea1DK3U3gkqMYXiE5qey, 'r') as f:
    meta = json.load(f)
with open(var_call_n0yhRjzDNNLXnJ8f87Nb5Cik, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter metadata for 2015
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)
meta_2015 = meta_df[meta_df['year'] == 2015]

# Very naive World-category heuristic: look for obvious world/geo/politics cues in title+description
world_keywords = ['iraq','afghanistan','election','war','united nations','u.n.','u.n','palestinian','israel','conflict','rebels','troops','terror','bomb','missile','diplomat','president','prime minister','government','parliament','world','global summit','summit','eu ','european union','unrest','protest','coup','nato','security council']

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()
pattern = '|'.join(world_keywords)
world_mask = arts_df['text'].str.contains(pattern, regex=True)
world_arts = arts_df[world_mask]

# Join 2015 metadata with world articles
merged = meta_2015.merge(world_arts[['article_id']], on='article_id', how='inner')

# Count by region
counts = merged.groupby('region')['article_id'].count().sort_values(ascending=False)

# Determine top region and counts as dict
if len(counts) == 0:
    result = {'top_region': None, 'counts_by_region': {}}
else:
    top_region = counts.index[0]
    result = {'top_region': top_region, 'counts_by_region': counts.to_dict()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XhZwea1DK3U3gkqMYXiE5qey': 'file_storage/call_XhZwea1DK3U3gkqMYXiE5qey.json', 'var_call_n0yhRjzDNNLXnJ8f87Nb5Cik': 'file_storage/call_n0yhRjzDNNLXnJ8f87Nb5Cik.json'}

exec(code, env_args)

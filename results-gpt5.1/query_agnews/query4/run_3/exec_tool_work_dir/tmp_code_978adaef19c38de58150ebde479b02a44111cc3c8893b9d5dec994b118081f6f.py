code = """import json, pandas as pd
import os

# Load full results from storage
with open(var_call_Epu7v4PQg5OPg691ZtEoUJ8O, 'r') as f:
    meta = json.load(f)
with open(var_call_EDTKb08ejah2pDcZWMRenzyq, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter metadata for 2015
meta_2015 = meta_df[meta_df['publication_date'].str.startswith('2015')]

# Very naive World-category classifier based on keywords typical for world news
world_keywords = ['iraq', 'war', 'election', 'president', 'minister', 'government', 'united nations', 'u.n.', 'u.n', 'conflict', 'terror', 'bomb', 'attack', 'israel', 'palestinian', 'afghanistan', 'nuclear', 'foreign', 'diplomat', 'summit', 'eu', 'european union']

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

pattern = '|'.join(world_keywords)
world_mask = arts_df['text'].str.contains(pattern, regex=True, na=False)
world_arts = arts_df[world_mask]

# Join with 2015 metadata
merged = pd.merge(meta_2015, world_arts[['article_id']], on='article_id', how='inner')

# Count by region
counts = merged.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    answer = None
else:
    top_region = counts.index[0]
    answer = top_region

result = json.dumps(answer)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Epu7v4PQg5OPg691ZtEoUJ8O': 'file_storage/call_Epu7v4PQg5OPg691ZtEoUJ8O.json', 'var_call_EDTKb08ejah2pDcZWMRenzyq': 'file_storage/call_EDTKb08ejah2pDcZWMRenzyq.json'}

exec(code, env_args)

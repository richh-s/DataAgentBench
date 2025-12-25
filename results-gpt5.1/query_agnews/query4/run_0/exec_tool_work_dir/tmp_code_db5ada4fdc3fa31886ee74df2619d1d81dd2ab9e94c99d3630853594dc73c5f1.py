code = """import json, pandas as pd
from datetime import datetime

# Load full metadata
with open(var_call_vmjFbAVwswjTfkzcW8xlHpWd, 'r') as f:
    meta = json.load(f)

# Load full articles
with open(var_call_qPW97SJgZB7KKctxNndBUSty, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter metadata to 2015
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)
meta_2015 = meta_df[meta_df['year'] == 2015]

# Heuristic: classify World category based on keywords in title/description
world_keywords = ['war','election','president','government','prime minister','conflict','UN','United Nations','terror','Iraq','Afghanistan','Israel','Palestinian','EU','NATO','Russia','China','diplomat','summit','embassy','protest','rebels','military','troops']

arts_df['text'] = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()

world_mask = arts_df['text'].apply(lambda x: any(k.lower() in x for k in world_keywords))
world_arts = arts_df[world_mask]

# Join 2015 metadata with world articles
merged = meta_2015.merge(world_arts[['article_id']], on='article_id', how='inner')

# Count by region
counts = merged.groupby('region').size().sort_values(ascending=False)

if len(counts) == 0:
    result = None
else:
    top_region = counts.index[0]
    result = top_region

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_vmjFbAVwswjTfkzcW8xlHpWd': 'file_storage/call_vmjFbAVwswjTfkzcW8xlHpWd.json', 'var_call_qPW97SJgZB7KKctxNndBUSty': 'file_storage/call_qPW97SJgZB7KKctxNndBUSty.json'}

exec(code, env_args)

code = """import json, pandas as pd

# Load full article_metadata
with open(var_call_9OxYlstvO7yf9Z5pxNQLHYJp, 'r') as f:
    meta = json.load(f)

# Load full articles
with open(var_call_HlJprYC6TVjZSNis5yCMbqeL, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Filter for year 2015
meta_df['year'] = meta_df['publication_date'].str[:4]
meta_2015 = meta_df[meta_df['year'] == '2015']

# Merge on article_id
meta_2015['article_id'] = meta_2015['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)
merged = meta_2015.merge(arts_df, on='article_id', how='inner')

# Simple heuristic to classify World vs others based on title/description keywords
world_keywords = ['iraq','israel','palestinian','palestine','afghanistan','war','u.n.','united nations','europe','asia','africa','latin america','middle east','russia','china','iran','north korea','taliban','militant','attack','bomb','peace talks','election','president','prime minister']

def is_world(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    return any(k in text for k in world_keywords)

merged['is_world'] = merged.apply(is_world, axis=1)

world_arts = merged[merged['is_world']]

# Count by region
counts = world_arts.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = None
else:
    top_region = counts.idxmax()
    result = top_region

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_9OxYlstvO7yf9Z5pxNQLHYJp': 'file_storage/call_9OxYlstvO7yf9Z5pxNQLHYJp.json', 'var_call_HlJprYC6TVjZSNis5yCMbqeL': 'file_storage/call_HlJprYC6TVjZSNis5yCMbqeL.json'}

exec(code, env_args)

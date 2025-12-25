code = """import json, pandas as pd

# Load full results from files
with open(var_call_CavSltoG0hgTAmwZNrmjq5cp, 'r') as f:
    meta_2015 = json.load(f)
with open(var_call_aR3K6qOQzHh8tdwN0GwrrQPd, 'r') as f:
    articles = json.load(f)

# Build DataFrames
meta_df = pd.DataFrame(meta_2015)
articles_df = pd.DataFrame(articles)

# Ensure article_id types match
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Join on article_id
merged = pd.merge(meta_df, articles_df, on='article_id', how='inner')

# Simple keyword-based classification for World category
# Heuristic: if title or description contains country/region/conflict/politics words, etc.
world_keywords = [
    'iraq','iran','korea','europe','africa','asia','china','japan','saudi','sudan','darfur',
    'taliban','israel','palestinian','russia','moscow','britain','london','uk ','eurozone',
    'refugee','united nations','u.n.','u.n ','election','president','minister','government',
    'war','rebels','militia','conflict','terror','nuclear','pipeline','exports','opec',
    'trade deficit','eurozone','south africa','mauritius','chad','saudi arabia','japanese',
]

text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()

is_world = text.apply(lambda t: any(k in t for k in world_keywords))
world_df = merged[is_world]

# Count world articles by region and find max
counts = world_df.groupby('region')['article_id'].nunique().reset_index(name='world_article_count')
if counts.empty:
    result = None
else:
    top_row = counts.sort_values('world_article_count', ascending=False).iloc[0]
    result = {
        'region': top_row['region'],
        'world_article_count': int(top_row['world_article_count'])
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_CavSltoG0hgTAmwZNrmjq5cp': 'file_storage/call_CavSltoG0hgTAmwZNrmjq5cp.json', 'var_call_aR3K6qOQzHh8tdwN0GwrrQPd': 'file_storage/call_aR3K6qOQzHh8tdwN0GwrrQPd.json'}

exec(code, env_args)

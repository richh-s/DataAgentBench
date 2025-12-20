code = """import json, pandas as pd
from datetime import datetime

# Load metadata
with open(var_call_BsrD0ULu90kw6tdvrYfbg20m, 'r') as f:
    metadata = json.load(f)

# Load articles
with open(var_call_4HA1KAjhpUfzMsiMdhxcwr3i, 'r') as f:
    articles = json.load(f)

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

# Ensure types
md_df['article_id'] = md_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Filter metadata for year 2015
md_df['year'] = pd.to_datetime(md_df['publication_date']).dt.year
md_2015 = md_df[md_df['year'] == 2015]

# Merge with articles
merged = md_2015.merge(art_df, on='article_id', how='inner')

# Simple keyword-based categorization for 'World' category
world_keywords = ['iraq','war','election','president','government','minister','united nations','un','world','global','conflict','troops','terror','palestinian','israel','nuclear','attack','protest','refugee','border']

def is_world(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    return any(k in text for k in world_keywords)

merged['is_world'] = merged.apply(is_world, axis=1)

world_articles = merged[merged['is_world']]

# Count by region
counts = world_articles.groupby('region').size().sort_values(ascending=False)

if len(counts) == 0:
    result = None
else:
    top_region = counts.idxmax()
    result = top_region

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_BsrD0ULu90kw6tdvrYfbg20m': 'file_storage/call_BsrD0ULu90kw6tdvrYfbg20m.json', 'var_call_4HA1KAjhpUfzMsiMdhxcwr3i': 'file_storage/call_4HA1KAjhpUfzMsiMdhxcwr3i.json'}

exec(code, env_args)

code = """import json
import pandas as pd

# Load the large query results from the provided storage file paths
meta_path = var_call_GbPvz63BJu7vNko6aJU4MTjy
articles_path = var_call_XINrgWKb2kM1jfheVNnKfaMl

with open(meta_path, 'r', encoding='utf-8') as f:
    meta = json.load(f)
with open(articles_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Create DataFrames
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Normalize article_id to integer for reliable joins
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge metadata (already filtered to 2015) with article content
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Simple keyword-based classifier for categories
sports_kw = {"game","season","match","scored","goal","tournament","league","cup","scores","wins","player","football","soccer","basketball","tennis","cricket","coach","inning","olympic","score","mlb","nhl","nfl"}
business_kw = {"stock","market","economy","business","profit","shares","bank","investment","company","oil","trade","economic","finance","financial","stocks","merger","acquisition","ipo","earnings","sales","revenue","fed","inflation"}
sci_kw = {"scientist","research","study","technology","tech","computer","software","nasa","space","scientists","experiment","drug","medical","science","researchers","nuclear","robot","ai","artificial intelligence","internet","server","device","phone","aerospace"}

import re

def classify_row(title, desc):
    text = ((title or "") + " " + (desc or "")).lower()
    # remove punctuation to better match keywords
    text_clean = re.sub(r"[^a-z0-9 ]+", " ", text)
    tokens = set(text_clean.split())
    if tokens & sports_kw:
        return 'Sports'
    if tokens & business_kw:
        return 'Business'
    if tokens & sci_kw:
        return 'Science/Technology'
    return 'World'

# Apply classifier
df['category'] = df.apply(lambda r: classify_row(r.get('title',''), r.get('description','')), axis=1)

# Filter for World category and count by region
world_df = df[df['category'] == 'World']
counts = world_df.groupby('region').size().reset_index(name='count')

if counts.empty:
    result = {"year": 2015, "top_regions": [], "max_count": 0}
else:
    max_count = int(counts['count'].max())
    top_regions = counts[counts['count'] == max_count]
    top_list = []
    for _, row in top_regions.iterrows():
        top_list.append({"region": row['region'], "count": int(row['count'])})
    result = {"year": 2015, "top_regions": top_list, "max_count": max_count}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rES5ZNy7uDq0HxFeFVdAP16S': ['articles'], 'var_call_iBe4jnZlH5tJGs5g2zgqeaoo': ['authors', 'article_metadata'], 'var_call_GbPvz63BJu7vNko6aJU4MTjy': 'file_storage/call_GbPvz63BJu7vNko6aJU4MTjy.json', 'var_call_XINrgWKb2kM1jfheVNnKfaMl': 'file_storage/call_XINrgWKb2kM1jfheVNnKfaMl.json'}

exec(code, env_args)

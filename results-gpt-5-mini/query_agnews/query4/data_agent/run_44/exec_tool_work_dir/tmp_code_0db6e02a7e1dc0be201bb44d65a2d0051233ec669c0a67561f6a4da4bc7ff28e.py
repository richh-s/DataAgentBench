code = """import json
import pandas as pd

# Load data from previous tool calls (file paths are provided in variables)
with open(var_call_AoTxbZHbO2c11Mi8wX8uGDVU, 'r', encoding='utf-8') as f:
    meta = json.load(f)
with open(var_call_12WNDkIttNSbYI7T0952OtHk, 'r', encoding='utf-8') as f:
    articles = json.load(f)

df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id as int for correct merging
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge metadata (which already filtered to 2015) with article contents
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Prepare keyword lists for category classification
sports_kw = ['game', 'match', 'score', 'season', 'football', 'soccer', 'basketball', 'tennis', 'goal', 'tournament', 'olympic', 'coach', 'inning', 'bat', 'pitch', 'league', 'cup', 'striker', 'goalkeeper', 'fifa', 'mlb', 'nba']
business_kw = ['stock', 'stocks', 'market', 'markets', 'shares', 'company', 'companies', 'firm', 'firms', 'investment', 'ipo', 'profit', 'loss', 'revenue', 'merger', 'acquisition', 'economy', 'economic', 'bank', 'banks', 'debt', 'earnings']
sci_kw = ['research', 'scientist', 'scientists', 'study', 'technology', 'technologies', 'tech', 'nasa', 'computer', 'software', 'internet', 'app', 'apps', 'clinical', 'medical', 'science', 'scientific', 'robot', 'ai', 'artificial intelligence']

# Simple priority-based classifier: Sports > Business > Science/Technology > World

def classify_text(title, desc):
    text = ''
    if not pd.isna(title):
        text += str(title).lower() + ' '
    if not pd.isna(desc):
        text += str(desc).lower()
    # check
    if any(k in text for k in sports_kw):
        return 'Sports'
    if any(k in text for k in business_kw):
        return 'Business'
    if any(k in text for k in sci_kw):
        return 'Science/Technology'
    return 'World'

# Apply classification
df['category'] = df.apply(lambda r: classify_text(r.get('title', ''), r.get('description', '')), axis=1)

# Filter World category and count by region
world_df = df[df['category'] == 'World']
counts = world_df['region'].value_counts().to_dict()

if not counts:
    result = {'regions': [], 'count': 0}
else:
    max_count = max(counts.values())
    top_regions = sorted([r for r,c in counts.items() if c == max_count])
    result = {'regions': top_regions, 'count': int(max_count)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AoTxbZHbO2c11Mi8wX8uGDVU': 'file_storage/call_AoTxbZHbO2c11Mi8wX8uGDVU.json', 'var_call_12WNDkIttNSbYI7T0952OtHk': 'file_storage/call_12WNDkIttNSbYI7T0952OtHk.json'}

exec(code, env_args)

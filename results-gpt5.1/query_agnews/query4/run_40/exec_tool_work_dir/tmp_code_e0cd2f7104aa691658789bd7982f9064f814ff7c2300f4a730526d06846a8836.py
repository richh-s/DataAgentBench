code = """import json, pandas as pd

# Load full results from files
with open(var_call_yoMnn8jwKk8kWeMm8IJ3uNTy, 'r') as f:
    meta_2015 = json.load(f)
with open(var_call_fwa4nD3PQJC2vh1Wh5sqOSKm, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(meta_2015)
articles_df = pd.DataFrame(articles)

# Ensure article_id is int for merging
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge to get titles/descriptions for 2015 articles
merged = pd.merge(meta_df, articles_df, on='article_id', how='inner')

# Simple keyword-based categorization for World vs others
# We'll use heuristics: if clearly business/sports/sci-tech keywords appear, exclude; otherwise many general news will be World.

business_kw = ['stock', 'stocks', 'market', 'markets', 'shares', 'oil', 'trade', 'economy', 'economic', 'bank', 'banks', 'fund', 'funds', 'investor', 'investment', 'ipo', 'rates', 'interest rate', 'bond', 'bonds', 'currency', 'currencies', 'dollar', 'euro', 'yen', 'profits', 'earnings', 'merger', 'acquisition', 'company', 'shares', 'quarter', 'sales']
sports_kw = ['nba', 'nfl', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'olympics', 'cup', 'tournament', 'league', 'coach', 'player', 'team', 'match', 'game', 'games']
science_kw = ['space', 'nasa', 'telescope', 'galaxy', 'cell', 'cells', 'genetic', 'genome', 'robot', 'robots', 'physics', 'chemistry', 'biology', 'scientist', 'scientists', 'researchers', 'technology', 'tech ', 'software', 'hardware', 'internet', 'online', 'computer', 'chip', 'chips']


def categorize(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    if any(k in text for k in sports_kw):
        return 'Sports'
    if any(k in text for k in science_kw):
        return 'Science/Technology'
    if any(k in text for k in business_kw):
        return 'Business'
    return 'World'

merged['category'] = merged.apply(categorize, axis=1)

world = merged[merged['category']=='World']
counts = world.groupby('region').size().sort_values(ascending=False)

top_region = counts.index[0] if len(counts)>0 else None

import json as _json
result = _json.dumps({'top_region_world_2015': top_region, 'counts_by_region_world_2015': counts.to_dict()})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_yoMnn8jwKk8kWeMm8IJ3uNTy': 'file_storage/call_yoMnn8jwKk8kWeMm8IJ3uNTy.json', 'var_call_fwa4nD3PQJC2vh1Wh5sqOSKm': 'file_storage/call_fwa4nD3PQJC2vh1Wh5sqOSKm.json'}

exec(code, env_args)

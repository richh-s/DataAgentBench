code = """import json, pandas as pd
from datetime import datetime

# Load full metadata
with open(var_call_4LQoBDcdK9dAfFW3X2kkjKQ6, 'r') as f:
    meta = json.load(f)

# Load full articles
with open(var_call_IXpBgEByzQGd77eep0iP4lYq, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure correct dtypes
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Filter to 2015
meta_df['year'] = pd.to_datetime(meta_df['publication_date']).dt.year
meta_2015 = meta_df[meta_df['year'] == 2015]

# Merge with articles to get text
df = meta_2015.merge(arts_df, on='article_id', how='inner')

# Simple heuristic classifier for World category based on keywords
world_keywords = ['iraq', 'afghanistan', 'korea', 'china', 'iran', 'united nations', 'u.n.', 'u.n', 'war', 'peace talks', 'palestinian', 'israeli', 'israel', 'gaza', 'terror', 'bomb', 'election', 'president', 'prime minister', 'parliament', 'government', 'rebel', 'militia', 'moscow', 'london', 'paris', 'tokyo', 'beijing', 'european union', 'eu', 'nato', 'baghdad']

def is_world(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    # crude exclusions for Sports, Business, Sci/Tech
    if any(k in text for k in ['football', 'soccer', 'nba', 'nfl', 'mlb', 'tennis', 'golf', 'olympic', 'olympics', 'world cup']):
        return False
    if any(k in text for k in ['stock', 'shares', 'market', 'economy', 'business', 'company', 'profit', 'bank', 'loan', 'trade deficit', 'ipo', 'fund', 'finance']):
        return False
    if any(k in text for k in ['researchers', 'scientists', 'study finds', 'study shows', 'spacecraft', 'nasa', 'astronaut', 'galaxy', 'telescope', 'laboratory', 'experiment']):
        return False
    return any(k in text for k in world_keywords)

world_df = df[df.apply(is_world, axis=1)]

# Count by region
counts = world_df.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = {"region": None, "count": 0}
else:
    top_region = counts.index[0]
    top_count = int(counts.iloc[0])
    result = {"region": top_region, "count": top_count}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4LQoBDcdK9dAfFW3X2kkjKQ6': 'file_storage/call_4LQoBDcdK9dAfFW3X2kkjKQ6.json', 'var_call_IXpBgEByzQGd77eep0iP4lYq': 'file_storage/call_IXpBgEByzQGd77eep0iP4lYq.json'}

exec(code, env_args)

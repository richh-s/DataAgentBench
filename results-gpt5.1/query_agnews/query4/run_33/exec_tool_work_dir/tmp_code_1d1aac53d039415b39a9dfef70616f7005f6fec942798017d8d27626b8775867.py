code = """import json, pandas as pd

# Load full metadata and article data from files
with open(var_call_o2v078ZZeKZPlYzKI92d0Gbn, 'r') as f:
    meta = json.load(f)
with open(var_call_tsLyjKdyi0YFbdLSTVVnNZ1Y, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Ensure article_id comparable types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Merge
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Simple keyword-based classifier for World category
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

world_kw = ['iraq','election','european','britain','french','german','russia','palestinian','israeli','afghan','korea','nuclear','united nations','u.n.','u.n ','taliban','terror','bush','kerry','al-qaeda','militant','gaza','israel','palestine','middle east','suicide bomb','rebel','militia','u.s. troops','car bomb','baghdad','kabul','moscow','london','paris','tokyo','beijing','hong kong','taiwan','china','japan','europe','africa','asia','latin america','world','global summit','olympics','iran','saddam','quake','tsunami','hurricane','earthquake']

world_mask = pd.Series(False, index=df.index)
for kw in world_kw:
    world_mask |= text.str.contains(kw)

world_df = df[world_mask]

# Count by region
counts = world_df.groupby('region').size().sort_values(ascending=False)

if len(counts) == 0:
    answer = 'No World category articles identified for 2015.'
else:
    top_region = counts.index[0]
    answer = top_region

res = json.dumps(answer)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_o2v078ZZeKZPlYzKI92d0Gbn': 'file_storage/call_o2v078ZZeKZPlYzKI92d0Gbn.json', 'var_call_tsLyjKdyi0YFbdLSTVVnNZ1Y': 'file_storage/call_tsLyjKdyi0YFbdLSTVVnNZ1Y.json'}

exec(code, env_args)

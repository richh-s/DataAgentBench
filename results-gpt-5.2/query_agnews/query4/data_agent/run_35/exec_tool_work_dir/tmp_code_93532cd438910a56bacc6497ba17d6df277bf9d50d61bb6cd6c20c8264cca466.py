code = """import json, pandas as pd

# Load metadata 2015
meta_src = var_call_Y3jUsZtSwZy9bZZb2BIN1SCU
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

art_src = var_call_TNzLExMV6Kfp915OcpO0lwaa
if isinstance(art_src, str):
    with open(art_src, 'r', encoding='utf-8') as f:
        arts = json.load(f)
else:
    arts = art_src

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
for c in ['article_id']:
    if c in meta_df.columns:
        meta_df[c] = meta_df[c].astype(str)
    if c in arts_df.columns:
        arts_df[c] = arts_df[c].astype(str)

# join
df = meta_df.merge(arts_df, on='article_id', how='left')

def is_world(title, desc):
    text = ((title or '') + ' ' + (desc or '')).lower()
    # business
    business_kw = ['stock', 'stocks', 'market', 'earnings', 'ipo', 'oil', 'opec', 'trade deficit', 'economy', 'profit', 'profits', 'shares', 'wall st', 'dollar', 'bank', 'interest rate', 'imf', 'inflation', 'fund', 'funds', 'retail sales', 'jobless', 'company', 'companies']
    # sports
    sports_kw = ['vs', 'defeats', 'beats', 'match', 'tournament', 'season', 'nba', 'nfl', 'mlb', 'nhl', 'soccer', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'cricket', 'coach', 'player', 'goal', 'run', 'score']
    # sci/tech
    sci_kw = ['google', 'microsoft', 'apple', 'iphone', 'android', 'software', 'internet', 'web', 'chip', 'nasa', 'space', 'satellite', 'robot', 'ai', 'science', 'scientist', 'research', 'study', 'technology', 'tech', 'nuclear', 'genome', 'climate', 'vaccine']
    # world/politics/conflict
    world_kw = ['iraq', 'iran', 'tehran', 'baghdad', 'afghanistan', 'pakistan', 'india', 'china', 'russia', 'ukraine', 'syria', 'israel', 'palestinian', 'gaza', 'u.n.', 'un ', 'united nations', 'minister', 'election', 'president', 'parliament', 'government', 'military', 'rebel', 'terror', 'attack', 'killed', 'refugee', 'darfur', 'sudan', 'diplomat', 'border', 'eu', 'european union', 'nato']

    def contains_any(kws):
        return any(kw in text for kw in kws)

    # classify by priority
    if contains_any(sports_kw):
        return False
    if contains_any(business_kw) and not contains_any(world_kw):
        return False
    if contains_any(sci_kw) and not contains_any(world_kw):
        return False
    # world if world keywords exist, otherwise default to world? no.
    return contains_any(world_kw)

world_mask = df.apply(lambda r: is_world(r.get('title'), r.get('description')), axis=1)
world_df = df[world_mask].copy()

counts = world_df.groupby('region', dropna=False)['article_id'].nunique().sort_values(ascending=False)
if counts.empty:
    result = {"region": None, "world_articles": 0}
else:
    top_region = counts.index[0]
    result = {"region": top_region, "world_articles": int(counts.iloc[0])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Y3jUsZtSwZy9bZZb2BIN1SCU': 'file_storage/call_Y3jUsZtSwZy9bZZb2BIN1SCU.json', 'var_call_TNzLExMV6Kfp915OcpO0lwaa': 'file_storage/call_TNzLExMV6Kfp915OcpO0lwaa.json'}

exec(code, env_args)

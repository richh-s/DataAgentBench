code = """import json, pandas as pd
from collections import Counter

# Load full results from files
with open(var_call_ZlnIqp12X11q6R5JqThZ0awS, 'r') as f:
    meta_2015 = json.load(f)
with open(var_call_U1fBzQLgSnFT2m2CZ4GrFXQj, 'r') as f:
    articles = json.load(f)

meta_df = pd.DataFrame(meta_2015)
art_df = pd.DataFrame(articles)

# Ensure article_id types align
meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

# Merge to get titles/descriptions for 2015 articles
merged = meta_df.merge(art_df, on='article_id', how='inner')

# Simple rule-based classifier for categories using keywords
world_keywords = [' iraq', 'iran', 'korea', 'africa', 'asia', 'europe', 'china', 'russia', 'israel', 'palestinian', 'pakistan', 'afghan', 'sudan', 'u.n.', 'united nations', 'terror', 'war', 'military', 'bomb', 'attack', 'election', 'prime minister', 'president', 'government', 'rebel', 'conflict', 'troops']

sports_keywords = ['nba', 'nfl', 'mlb', 'nhl', 'soccer', 'football', 'baseball', 'basketball', 'olympic', 'tennis', 'golf', 'cricket', 'hockey', 'tournament', 'finals', 'playoffs', 'world cup']

business_keywords = ['stock', 'stocks', 'shares', 'market', 'ipo', 'bank', 'banks', 'economy', 'economic', 'trade', 'oil', 'merger', 'acquisition', 'earnings', 'fund', 'funds', 'investment', 'investor', 'finance', 'financial', 'debt', 'dollar', 'euro', 'yen', 'company', 'corporate']

sci_keywords = ['scientist', 'science', 'researchers', 'research', 'nuclear', 'space', 'nasa', 'technology', 'tech ', 'software', 'hardware', 'internet', 'genetic', 'biotech', 'medical', 'medicine', 'physics', 'chemistry']


def classify(text):
    if not isinstance(text, str):
        return None
    t = ' ' + text.lower() + ' '
    scores = {'World':0, 'Sports':0, 'Business':0, 'Science/Technology':0}
    for w in world_keywords:
        if w in t:
            scores['World'] += 1
    for w in sports_keywords:
        if w in t:
            scores['Sports'] += 1
    for w in business_keywords:
        if w in t:
            scores['Business'] += 1
    for w in sci_keywords:
        if w in t:
            scores['Science/Technology'] += 1
    # pick best non-zero
    best_cat = None
    best_score = 0
    for k,v in scores.items():
        if v>best_score:
            best_score=v
            best_cat=k
    return best_cat

# Apply classifier using title+description
merged['full_text'] = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.strip()
merged['category'] = merged['full_text'].apply(classify)

world = merged[merged['category']=='World']

# Count by region
counts = world.groupby('region')['article_id'].nunique().sort_values(ascending=False)

if counts.empty:
    result = {'region': None, 'count': 0}
else:
    top_region = counts.index[0]
    top_count = int(counts.iloc[0])
    result = {'region': top_region, 'count': top_count}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ZlnIqp12X11q6R5JqThZ0awS': 'file_storage/call_ZlnIqp12X11q6R5JqThZ0awS.json', 'var_call_U1fBzQLgSnFT2m2CZ4GrFXQj': 'file_storage/call_U1fBzQLgSnFT2m2CZ4GrFXQj.json'}

exec(code, env_args)

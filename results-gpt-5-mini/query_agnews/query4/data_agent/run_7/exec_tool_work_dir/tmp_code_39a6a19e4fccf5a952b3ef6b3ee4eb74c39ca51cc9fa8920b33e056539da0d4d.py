code = """import json
import pandas as pd

meta_var = var_call_MtuWlk0X9O5O0IBOY80mNVyF
if isinstance(meta_var, str) and meta_var.endswith('.json'):
    with open(meta_var, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_var

articles = var_call_zSpNFC4iDBPxO6hTIBSdwo9l

# Convert to DataFrames
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id are strings
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge metadata for 2015 with article texts
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Simple keyword-based classifier
import re

def classify(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    # sports keywords
    sports_kw = ['match', 'goal', 'tournament', 'series', 'win', 'defeat', 'season', 'league', 'player', 'team', 'fifa', 'nba', 'mlb', 'soccer', 'football', 'basketball', 'olympic', 'scored', 'coach', 'score', 'cup', 'racing']
    # science/tech keywords
    sci_kw = ['technology', 'tech', 'science', 'nasa', 'space', 'research', 'scientists', 'computer', 'software', 'ai', 'robot', 'smartphone', 'study', 'laboratory', 'scientist']
    # business keywords
    biz_kw = ['market', 'stocks', 'shares', 'economy', 'bank', 'investment', 'firm', 'ipo', 'acquire', 'merger', 'commercial', 'oil prices', 'crude', 'stock', 'dow', "wall st", 'bonds', 'reuters -']
    # world keywords (conflict/politics/geopolitics)
    world_kw = ['president', 'minister', 'government', 'militia', 'rebel', 'attack', 'war', 'election', 'diplomat', 'united nations', 'terror', 'isis', 'iraq', 'syria', 'killed', 'dies', 'died']

    for kw in sports_kw:
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            return 'Sports'
    for kw in sci_kw:
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            return 'Science/Technology'
    for kw in biz_kw:
        if kw in text:
            return 'Business'
    for kw in world_kw:
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            return 'World'
    # fallback heuristics: if contains a country or continent name, treat as World
    countries_continents = ['africa','asia','europe','north america','south america','china','india','russia','united states','usa','britain','uk','france','germany','spain','italy','japan','korea']
    for kw in countries_continents:
        if kw in text:
            return 'World'
    # default to Business if words like 'company' or 'firm' present
    if re.search(r'\b(company|firm|business|corporation|industry)\b', text):
        return 'Business'
    # If none matched, default to World
    return 'World'

# Apply classifier
df['category'] = df.apply(classify, axis=1)

# Count World articles by region
world_df = df[df['category'] == 'World']
counts = world_df.groupby('region').size().reset_index(name='count')
counts_sorted = counts.sort_values('count', ascending=False).reset_index(drop=True)

# Prepare output
if counts_sorted.empty:
    result = {"top_region": None, "count": 0, "counts": []}
else:
    top_region = counts_sorted.loc[0, 'region']
    top_count = int(counts_sorted.loc[0, 'count'])
    counts_list = counts_sorted.to_dict(orient='records')
    for r in counts_list:
        r['count'] = int(r['count'])
    result = {"top_region": top_region, "count": top_count, "counts": counts_list}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MtuWlk0X9O5O0IBOY80mNVyF': 'file_storage/call_MtuWlk0X9O5O0IBOY80mNVyF.json', 'var_call_zSpNFC4iDBPxO6hTIBSdwo9l': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

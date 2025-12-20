code = """import json, pandas as pd
from datetime import datetime

# Load full metadata from file path
with open(var_call_wGzXRpxlkg70B8XcWDGX4N3O, 'r') as f:
    metadata = json.load(f)

articles = var_call_Ph9XH4YJhnFMGWh59w1ZyUAb

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

md_df['article_id'] = md_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

md_2015 = md_df[md_df['publication_date'].str.startswith('2015-')]
merged = md_2015.merge(art_df, on='article_id', how='inner')

text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()

world_keywords = ['world', 'iraq', 'election', 'elections', 'war', 'conflict', 'un ', ' u.n.', 'president', 'government', 'parliament']

is_world = text.apply(lambda t: any(k in t for k in world_keywords))
world_df = merged[is_world]

counts = world_df.groupby('region').size().sort_values(ascending=False)

if counts.empty:
    result = None
else:
    result = counts.idxmax()

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_wGzXRpxlkg70B8XcWDGX4N3O': 'file_storage/call_wGzXRpxlkg70B8XcWDGX4N3O.json', 'var_call_Ph9XH4YJhnFMGWh59w1ZyUAb': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json, pandas as pd
from datetime import datetime

# Load full metadata from file path
with open(var_call_oE6kMm2ERj0M2SuEma0C4y5r, 'r') as f:
    metadata = json.load(f)

articles = var_call_Zc9oSYmHgF97Eg1ISWgeTpk5

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

md_2015 = md_df[md_df['publication_date'].str.startswith('2015-')].copy()

world_ids = set()
for _, row in art_df.iterrows():
    text = f"{row['title']} {row['description']}".lower()
    if any(k in text for k in ['iraq', 'africa', 'asia', 'europe', 'latin america', 'middle east', 'palestinian', 'israel', 'united nations', 'u.n.', 'election in', 'president of', 'prime minister', 'war in', 'terrorist', 'bombing', 'conflict in']):
        world_ids.add(str(row['article_id']))

md_2015_world = md_2015[md_2015['article_id'].astype(str).isin(world_ids)]

counts = md_2015_world.groupby('region').size().sort_values(ascending=False)

if not counts.empty:
    top_region = counts.index[0]
else:
    top_region = None

result = json.dumps({'top_region_2015_world': top_region, 'counts_by_region': counts.to_dict()})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_oE6kMm2ERj0M2SuEma0C4y5r': 'file_storage/call_oE6kMm2ERj0M2SuEma0C4y5r.json', 'var_call_Zc9oSYmHgF97Eg1ISWgeTpk5': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

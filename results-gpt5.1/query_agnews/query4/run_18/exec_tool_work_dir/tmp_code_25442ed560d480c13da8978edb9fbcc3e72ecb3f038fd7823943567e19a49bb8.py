code = """import json, pandas as pd, os

articles = pd.DataFrame(var_call_lyvJXtRxDihERasn7Pf1vFER)

with open(var_call_9mzNeluin3mUUlZkCWqtAPwK, 'r') as f:
    metadata = pd.DataFrame(json.load(f))

world_keywords = ['world', 'global', 'international', 'foreign', 'abroad', 'diplomacy', 'summit', 'UN ', 'United Nations', 'NATO', 'EU ', 'European Union', 'Middle East', 'Iraq', 'Afghanistan', 'Israel', 'Palestine', 'terror', 'war', 'conflict']

articles['text'] = (articles['title'].fillna('') + ' ' + articles['description'].fillna('')).str.lower()

articles['is_world'] = articles['text'].apply(lambda t: any(k.lower() in t for k in world_keywords))

world_articles = articles[articles['is_world']][['article_id']]

world_articles['article_id'] = world_articles['article_id'].astype(int)
metadata['article_id'] = metadata['article_id'].astype(int)

merged = metadata.merge(world_articles, on='article_id', how='inner')

counts = merged.groupby('region').size().sort_values(ascending=False)

top_region = counts.index[0] if len(counts) > 0 else None

result = json.dumps({'top_region_2015_world': top_region, 'counts_by_region': counts.to_dict()})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_lyvJXtRxDihERasn7Pf1vFER': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_9mzNeluin3mUUlZkCWqtAPwK': 'file_storage/call_9mzNeluin3mUUlZkCWqtAPwK.json'}

exec(code, env_args)

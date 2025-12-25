code = """import json, pandas as pd

with open(var_call_wGzXRpxlkg70B8XcWDGX4N3O, 'r') as f:
    metadata = json.load(f)
articles = var_call_Ph9XH4YJhnFMGWh59w1ZyUAb

md_df = pd.DataFrame(metadata)
art_df = pd.DataFrame(articles)

md_df['article_id'] = md_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

md_2015 = md_df[md_df['publication_date'].str.startswith('2015-')]
merged = md_2015.merge(art_df, on='article_id', how='inner')

print('__RESULT__:')
print(json.dumps({'merged_cols': merged.columns.tolist(), 'merged_head': merged.head().to_dict(orient='records')}))"""

env_args = {'var_call_wGzXRpxlkg70B8XcWDGX4N3O': 'file_storage/call_wGzXRpxlkg70B8XcWDGX4N3O.json', 'var_call_Ph9XH4YJhnFMGWh59w1ZyUAb': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_vAKYwX276BvfTZUoOPAN4lxH': {'md_cols': ['article_id', 'region', 'publication_date'], 'art_cols': ['article_id', 'title', 'description'], 'md_head': [{'article_id': '0', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'art_head': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}}

exec(code, env_args)

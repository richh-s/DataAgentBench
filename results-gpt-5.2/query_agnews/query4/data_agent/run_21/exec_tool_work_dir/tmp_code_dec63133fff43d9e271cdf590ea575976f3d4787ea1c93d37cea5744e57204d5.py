code = """import json, pandas as pd

path = var_call_cMidJvjQSwFJtWABub9NtQh6
with open(path, 'r', encoding='utf-8') as f:
    meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
ids = meta_df['article_id'].unique().tolist()

chunk_size = 900
chunks = [ids[i:i+chunk_size] for i in range(0, len(ids), chunk_size)]
queries = []
for ch in chunks:
    queries.append({
        'collection':'articles',
        'filter': {'article_id': {'$in': [str(x) for x in ch]}},
        'projection': {'_id':0,'article_id':1,'title':1,'description':1},
        'limit': len(ch)
    })

print('__RESULT__:')
print(json.dumps({'n_chunks': len(queries), 'first_query': queries[0]}))"""

env_args = {'var_call_cMidJvjQSwFJtWABub9NtQh6': 'file_storage/call_cMidJvjQSwFJtWABub9NtQh6.json', 'var_call_QDkbNYpYGOd3zSdrNNJaNExm': {'n_2015_articles': 6696, 'note': 'Need tool calls from assistant to fetch article texts for categorization.'}, 'var_call_nfQWvAZmhcFhuO8ipDrhhpYJ': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

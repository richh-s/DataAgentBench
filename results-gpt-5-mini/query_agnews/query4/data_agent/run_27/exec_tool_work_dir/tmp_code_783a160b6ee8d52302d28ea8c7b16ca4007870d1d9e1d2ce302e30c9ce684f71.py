code = """import json
# load metadata ids list and articles list from storage
meta_ids_path = var_call_McgbruQEYnesqaAWqZD3e4b2
with open(meta_ids_path, 'r') as f:
    meta_ids = json.load(f)

articles = var_call_fQhii1PVu53kRkgR2E8jKubt
article_ids = [int(a['article_id']) for a in articles]

intersection = sorted(list(set(meta_ids).intersection(article_ids)))
result = {'meta_count': len(meta_ids), 'articles_count': len(article_ids), 'intersection_count': len(intersection), 'intersection_sample': intersection[:20]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_omp3ddExYwoslFqB4uKYS5tq': 'file_storage/call_omp3ddExYwoslFqB4uKYS5tq.json', 'var_call_McgbruQEYnesqaAWqZD3e4b2': 'file_storage/call_McgbruQEYnesqaAWqZD3e4b2.json', 'var_call_fQhii1PVu53kRkgR2E8jKubt': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_bpIQTUzik8HAFS0MyOyxgOiX': {'counts': {}, 'winners': [], 'top_count': 0}}

exec(code, env_args)

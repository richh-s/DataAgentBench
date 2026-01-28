code = """import json, os
metadata_file = locals()['var_functions.query_db:0']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)
article_ids_2015 = {int(row['article_id']) for row in metadata_2015}

articles_result = locals()['var_functions.query_db:10']
# Determine if it's a file path or direct list
if isinstance(articles_result, str) and os.path.exists(articles_result):
    with open(articles_result, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_result

filtered = []
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except Exception:
        continue
    if aid in article_ids_2015:
        filtered.append(a)

out = {'total_articles_2015': len(metadata_2015), 'articles_with_content': len(filtered)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'count': 6696, 'message': 'Found 6696 articles from 2015'}, 'var_functions.query_db:10': [{'_id': '6969d4ae855c9d59985346e5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d4ae855c9d59985346e6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d4ae855c9d59985346e7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d4ae855c9d59985346e8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d4ae855c9d59985346e9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

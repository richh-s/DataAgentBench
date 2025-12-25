code = """import json

# Load metadata path and articles path
metadata_path = locals()['var_function-call-7362815310734823686']
articles_path = locals()['var_function-call-8165940882341443129']

with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

with open(articles_path, 'r') as f:
    articles_records = json.load(f)

# Set of fetched article IDs
fetched_ids = set()
for a in articles_records:
    fetched_ids.add(str(a['article_id']))

# Check coverage
missing_count = 0
found_count = 0
for r in metadata_records:
    aid = str(r['article_id'])
    if aid in fetched_ids:
        found_count += 1
    else:
        missing_count += 1

print("__RESULT__:")
print(json.dumps({"found": found_count, "missing": missing_count}))"""

env_args = {'var_function-call-7362815310734823686': 'file_storage/function-call-7362815310734823686.json', 'var_function-call-5837169514191744689': 14860, 'var_function-call-15464103905303230680': 'file_storage/function-call-15464103905303230680.json', 'var_function-call-12360763159906928774': [{'_id': '6944db67e28dfbaacfa3ae88', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944db67e28dfbaacfa3ae89', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944db67e28dfbaacfa3ae8a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944db67e28dfbaacfa3ae8b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944db67e28dfbaacfa3ae8c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8054706129410508577': [{'_id': '6944db67e28dfbaacfa3ae88', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944db67e28dfbaacfa3ae89', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944db67e28dfbaacfa3ae8a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944db67e28dfbaacfa3ae8b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944db67e28dfbaacfa3ae8c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13308618984475909885': 5, 'var_function-call-8165940882341443129': 'file_storage/function-call-8165940882341443129.json', 'var_function-call-6551584233653994266': {'average': 43.09090909090909, 'counts_per_year': {'2016': 46, '2015': 44, '2017': 46, '2020': 44, '2013': 47, '2018': 51, '2010': 35, '2011': 48, '2014': 39, '2019': 36, '2012': 38}, 'loaded_count': 20000}}

exec(code, env_args)

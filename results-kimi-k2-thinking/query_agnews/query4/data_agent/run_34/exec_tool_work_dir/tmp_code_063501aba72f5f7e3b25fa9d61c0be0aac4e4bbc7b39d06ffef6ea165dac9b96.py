code = """import json
import pandas as pd

# Load the full metadata file
metadata_file_path = locals()['var_functions.query_db:2']
with open(metadata_file_path, 'r') as f:
    metadata_2015_raw = json.load(f)

# Load articles data
articles_data = locals()['var_functions.query_db:0']

print('Articles sample:', articles_data[:2])
print('Metadata sample:', metadata_2015_raw[:2])
print('Total articles:', len(articles_data))
print('Total metadata records:', len(metadata_2015_raw))

# Check data types
if articles_data:
    print('First article ID type:', type(articles_data[0]['article_id']))
    print('First article ID value:', repr(articles_data[0]['article_id']))
if metadata_2015_raw:
    print('First metadata article_id type:', type(metadata_2015_raw[0]['article_id']))
    print('First metadata article_id value:', repr(metadata_2015_raw[0]['article_id']))

result = {'articles': len(articles_data), 'metadata': len(metadata_2015_raw)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969eb4faa75f1e99b0a7c8f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969eb4faa75f1e99b0a7c90', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969eb4faa75f1e99b0a7c91', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969eb4faa75f1e99b0a7c92', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969eb4faa75f1e99b0a7c93', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'region': None, 'article_count': 0}}

exec(code, env_args)

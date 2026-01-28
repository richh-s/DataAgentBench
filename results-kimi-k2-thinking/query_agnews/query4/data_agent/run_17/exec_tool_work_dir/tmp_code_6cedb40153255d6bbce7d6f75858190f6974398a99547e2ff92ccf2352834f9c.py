code = """import json

# Read the metadata file path
metadata_file_path = locals()['var_functions.execute_python:5']

# Read the articles file path
articles_file_path = locals()['var_functions.query_db:28']

# Read both files
with open(metadata_file_path, 'r') as f:
    metadata_data = json.load(f)

with open(articles_file_path, 'r') as f:
    all_articles = json.load(f)

# Get the 2015 article IDs as strings
article_ids_2015 = set(metadata_data['article_ids_list'])

# Filter articles from 2015
articles_2015 = []
for article in all_articles:
    if article['article_id'] in article_ids_2015:
        articles_2015.append(article)

print('__RESULT__:')
print(json.dumps({
    "total_articles_in_db": len(all_articles),
    "articles_from_2015": len(articles_2015),
    "sample_articles": articles_2015[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:6': [{'_id': '6969de2a3e4a8741baa472bb', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969de2a3e4a8741baa472bc', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969de2a3e4a8741baa472bd', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969de2a3e4a8741baa472be', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969de2a3e4a8741baa472bf', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': [], 'var_functions.execute_python:10': {'article_ids_count': 6696, 'first_few_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'type_example': "<class 'int'>"}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_articles': 6696, 'num_batches': 7, 'first_batch_size': 1000, 'first_few_ids': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:16': [], 'var_functions.execute_python:18': {'total_unique_articles': 6696, 'sample_ids': ['31938', '62445', '18344', '87149', '63112', '124688', '113033', '743', '9249', '73090']}, 'var_functions.query_db:20': [], 'var_functions.query_db:22': [{'_id': '6969de2a3e4a8741baa472c8', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_functions.execute_python:24': {'total_article_ids': 6696, 'num_batches': 14, 'first_batch_sample': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:28': {'sample_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97', '116', '117', '141', '165', '179', '203', '240', '243', '266', '271'], 'count': 6696}}

exec(code, env_args)

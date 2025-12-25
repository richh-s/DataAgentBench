code = """import json
import pandas as pd

# Load metadata
meta_path = locals()['var_function-call-11639742510862021534']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)

# Load articles
articles_path = locals()['var_function-call-5039010200560302586']
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

# Extract IDs
meta_ids = set([int(item['article_id']) for item in meta_data])
article_ids = set([int(item['article_id']) for item in articles_data])

missing_ids = meta_ids - article_ids
max_meta_id = max(meta_ids) if meta_ids else 0
max_article_id = max(article_ids) if article_ids else 0

print(f"Meta IDs count: {len(meta_ids)}")
print(f"Fetched Articles count: {len(article_ids)}")
print(f"Missing IDs count: {len(missing_ids)}")
print(f"Max Meta ID: {max_meta_id}")
print(f"Max Article ID: {max_article_id}")

print("__RESULT__:")
print(json.dumps({
    "missing_count": len(missing_ids),
    "max_meta_id": max_meta_id,
    "max_article_id": max_article_id
}))"""

env_args = {'var_function-call-11639742510862021534': 'file_storage/function-call-11639742510862021534.json', 'var_function-call-7912262759371964937': 'file_storage/function-call-7912262759371964937.json', 'var_function-call-7698643900256978742': 14860, 'var_function-call-13170610014898490485': [{'_id': '6944d6a50a99d7e0e8672aa9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d6a50a99d7e0e8672aaa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d6a50a99d7e0e8672aab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d6a50a99d7e0e8672aac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d6a50a99d7e0e8672aad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8382702086317822417': [{'_id': '6944d6a50a99d7e0e8672aa9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d6a50a99d7e0e8672aaa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d6a50a99d7e0e8672aab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d6a50a99d7e0e8672aac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d6a50a99d7e0e8672aad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17709649415609663654': {'counts_per_year': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}, 'average': 0.09090909090909091, 'total_articles_fetched': 5, 'total_articles_merged': 1}, 'var_function-call-5039010200560302586': 'file_storage/function-call-5039010200560302586.json'}

exec(code, env_args)

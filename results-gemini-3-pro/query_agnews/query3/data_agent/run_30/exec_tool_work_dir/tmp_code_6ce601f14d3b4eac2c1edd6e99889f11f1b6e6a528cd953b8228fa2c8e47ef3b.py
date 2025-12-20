code = """import json
import pandas as pd

# Load Data (using the same variables)
with open(locals()['var_function-call-9284748779350516997'], 'r') as f:
    metadata_list = json.load(f)
with open(locals()['var_function-call-16732576443780575921'], 'r') as f:
    batch1 = json.load(f)
with open(locals()['var_function-call-11422003096982108356'], 'r') as f:
    batch2 = json.load(f)
with open(locals()['var_function-call-12106970953398615057'], 'r') as f:
    batch3 = json.load(f)

# Combine
articles_list = batch1 + batch2 + batch3
df_articles = pd.DataFrame(articles_list)
df_articles['article_id'] = df_articles['article_id'].astype(int)
df_articles = df_articles.drop_duplicates(subset=['article_id'])

# Metadata
df_meta = pd.DataFrame(metadata_list)
df_meta['article_id'] = df_meta['article_id'].astype(int)

# Check
missing_ids = set(df_meta['article_id']) - set(df_articles['article_id'])

print("__RESULT__:")
print(json.dumps({
    "articles_fetched_count": len(df_articles),
    "metadata_count": len(df_meta),
    "missing_count": len(missing_ids),
    "first_10_missing": list(missing_ids)[:10] if missing_ids else []
}))"""

env_args = {'var_function-call-9284748779350516997': 'file_storage/function-call-9284748779350516997.json', 'var_function-call-16724156452483696481': {'count': 14860, 'first_10_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_function-call-10043856992590760587': [{'_id': '6944d9cdc5455efc705a86b8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d9cdc5455efc705a86b9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d9cdc5455efc705a86ba', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d9cdc5455efc705a86bb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d9cdc5455efc705a86bc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-732580074867003729': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}, 'average': 0.09090909090909091, 'total_business': 1}, 'var_function-call-8949601244673809398': {'total_merged': 1, 'category_counts': {'Business': 1}, 'sample_non_business': [], 'sample_unknown': []}, 'var_function-call-16732576443780575921': 'file_storage/function-call-16732576443780575921.json', 'var_function-call-2263675403483438088': {'yearly_counts': {'2010': 88, '2011': 117, '2012': 116, '2013': 122, '2014': 113, '2015': 119, '2016': 113, '2017': 131, '2018': 124, '2019': 123, '2020': 122}, 'average': 117.0909090909091, 'total_business': 1288, 'total_articles_merged': 5762}, 'var_function-call-2624805255953775997': {'meta_min_id': 3, 'meta_max_id': 127583, 'articles_min_id': 0, 'articles_max_id': 49999, 'articles_count': 50000}, 'var_function-call-11422003096982108356': 'file_storage/function-call-11422003096982108356.json', 'var_function-call-12106970953398615057': 'file_storage/function-call-12106970953398615057.json', 'var_function-call-10466209198604847285': {'yearly_counts': {'2010': 282, '2011': 360, '2012': 354, '2013': 381, '2014': 345, '2015': 360, '2016': 348, '2017': 396, '2018': 381, '2019': 384, '2020': 375}, 'average': 360.54545454545456, 'total_business': 3966, 'total_articles_merged': 17286, 'total_metadata': 14860, 'match_rate': 1.163257065948856}, 'var_function-call-3087009151347447661': {'yearly_counts': {'2010': 94, '2011': 120, '2012': 118, '2013': 127, '2014': 115, '2015': 120, '2016': 116, '2017': 132, '2018': 127, '2019': 128, '2020': 125}, 'average': 120.18181818181819, 'total_business': 1322, 'total_merged': 5762}}

exec(code, env_args)

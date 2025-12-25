code = """import json
import pandas as pd
import os

# Load metadata
raw_meta = locals()['var_function-call-6219509864635122554']
if isinstance(raw_meta, str) and os.path.exists(raw_meta):
    with open(raw_meta, 'r') as f:
        meta_data = json.load(f)
else:
    meta_data = raw_meta

# Load articles
raw_articles = locals()['var_function-call-6391207851705770972']
if isinstance(raw_articles, str) and os.path.exists(raw_articles):
    with open(raw_articles, 'r') as f:
        articles_data = json.load(f)
else:
    articles_data = raw_articles

df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(articles_data)

df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

df_merged = pd.merge(df_meta, df_articles, on='article_id', how='left')

print("__RESULT__:")
print(json.dumps({
    "meta_count": int(len(df_meta)),
    "articles_count": int(len(df_articles)),
    "merged_count": int(len(df_merged)),
    "merged_with_title_count": int(df_merged['title'].notnull().sum()),
    "sample_meta_ids": df_meta['article_id'].head(5).tolist(),
    "sample_article_ids": df_articles['article_id'].head(5).tolist()
}))"""

env_args = {'var_function-call-6219509864635122554': 'file_storage/function-call-6219509864635122554.json', 'var_function-call-11799845015617883549': 14860, 'var_function-call-4236489543979189159': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c5604aa2a519adff7872', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c5604aa2a519adff7873', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c5604aa2a519adff7874', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c5604aa2a519adff7875', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13155074376232017203': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0'}], 'var_function-call-6391207851705770972': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c5604aa2a519adff7872', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c5604aa2a519adff7873', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c5604aa2a519adff7874', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c5604aa2a519adff7875', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8907977861956983750': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}, 'average': 0.09090909090909091}}

exec(code, env_args)

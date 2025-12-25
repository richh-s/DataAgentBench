code = """import pandas as pd
import json
import os

# Reload data
meta_path = locals()['var_function-call-1050039959698811753']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)
df_meta = pd.DataFrame(meta_data)
df_meta['article_id'] = pd.to_numeric(df_meta['article_id'], errors='coerce')

articles_res = locals()['var_function-call-14707976591899183813']
if isinstance(articles_res, str) and articles_res.endswith('.json') and os.path.exists(articles_res):
    with open(articles_res, 'r') as f:
        articles_data = json.load(f)
else:
    articles_data = articles_res
df_articles = pd.DataFrame(articles_data)
df_articles['article_id'] = pd.to_numeric(df_articles['article_id'], errors='coerce')

debug_info = {}
debug_info['meta_size'] = len(df_meta)
debug_info['articles_size'] = len(df_articles)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')
debug_info['merged_size'] = len(df)

if not df.empty:
    debug_info['sample'] = df[['article_id', 'title', 'description']].head(3).to_dict(orient='records')
else:
    debug_info['meta_id_sample'] = df_meta['article_id'].head().tolist()
    debug_info['articles_id_sample'] = df_articles['article_id'].head().tolist()

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-886384908282461354': ['authors', 'article_metadata'], 'var_function-call-1050039959698811753': 'file_storage/function-call-1050039959698811753.json', 'var_function-call-18250612966487496501': 'file_storage/function-call-18250612966487496501.json', 'var_function-call-4586272944250348228': 14860, 'var_function-call-14707976591899183813': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9804075469372697773': {'average': 0.0, 'counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}}}

exec(code, env_args)

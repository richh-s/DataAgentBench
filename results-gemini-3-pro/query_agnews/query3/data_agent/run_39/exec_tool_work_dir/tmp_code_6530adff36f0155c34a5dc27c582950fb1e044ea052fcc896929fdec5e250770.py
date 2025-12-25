code = """import json
import pandas as pd

# Load metadata
metadata_file = locals()['var_function-call-1557171304419617632']
with open(metadata_file, 'r') as f:
    metadata_data = json.load(f)
df_meta = pd.DataFrame(metadata_data)

# Load articles
articles_data = locals()['var_function-call-4617174131752082327']
if isinstance(articles_data, str):
    with open(articles_data, 'r') as f:
        articles_data = json.load(f)
df_articles = pd.DataFrame(articles_data)

df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

print("__RESULT__:")
debug_info = {
    "len_meta": len(df_meta),
    "len_articles": len(df_articles),
    "len_merged": len(df),
    "sample_titles": df['title'].head(5).tolist() if not df.empty else [],
    "sample_ids": df['article_id'].head(5).tolist() if not df.empty else []
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1557171304419617632': 'file_storage/function-call-1557171304419617632.json', 'var_function-call-4617174131752082327': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7069929063851328032': {'average': 0.0, 'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}}}

exec(code, env_args)

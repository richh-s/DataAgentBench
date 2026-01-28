code = """import json
import pandas as pd

# Load the 2015 metadata (stored as a file path)
meta_2015_file = var_functions.query_db:0
if isinstance(meta_2015_file, str) and meta_2015_file.endswith('.json'):
    with open(meta_2015_file, 'r') as f:
        metadata_2015 = json.load(f)
else:
    metadata_2015 = var_functions.query_db:0

# Load all articles
articles_data = var_functions.query_db:2

# Convert to DataFrames
df_meta = pd.DataFrame(metadata_2015)
df_articles = pd.DataFrame(articles_data)

# Ensure article_id is int for matching
df_meta['article_id'] = pd.to_numeric(df_meta['article_id'])
df_articles['article_id'] = pd.to_numeric(df_articles['article_id'])

# Merge to get articles from 2015
df_merged = df_articles.merge(df_meta, on='article_id', how='inner')

print(f"Total articles from 2015: {len(df_merged)}")
print("__RESULT__:")
print(json.dumps({"total_2015_articles": len(df_merged), "sample": df_merged.head(3).to_dict('records')}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'_id': '6969da34a43fb535d0881320', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969da34a43fb535d0881321', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969da34a43fb535d0881322', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969da34a43fb535d0881323', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969da34a43fb535d0881324', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

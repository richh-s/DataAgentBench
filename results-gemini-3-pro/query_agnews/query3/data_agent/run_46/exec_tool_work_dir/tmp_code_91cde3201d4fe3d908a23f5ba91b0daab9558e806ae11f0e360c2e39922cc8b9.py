code = """import json
import pandas as pd
import os

# Load SQL results
sql_key = 'var_function-call-1308901072042740489'
with open(locals()[sql_key], 'r') as f:
    sql_data = json.load(f)

df_meta = pd.DataFrame(sql_data)

# Load Mongo results
mongo_key = 'var_function-call-9429883819834955631'
mongo_val = locals()[mongo_key]

if isinstance(mongo_val, str) and os.path.exists(mongo_val):
    with open(mongo_val, 'r') as f:
        mongo_data = json.load(f)
else:
    mongo_data = mongo_val

df_articles = pd.DataFrame(mongo_data)

# Check sizes
print(f"Meta rows: {len(df_meta)}")
print(f"Articles rows: {len(df_articles)}")

# Check types
print(f"Meta ID type: {type(df_meta['article_id'].iloc[0])}")
print(f"Articles ID type: {type(df_articles['article_id'].iloc[0])}")

# Merge
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)
merged = pd.merge(df_meta, df_articles, on='article_id', how='inner')

print(f"Merged rows: {len(merged)}")

# Check a few titles
print("Sample titles:")
print(merged['title'].head(10).tolist())

# Check simple keyword hit count
kw = 'business'
hits = merged[merged['title'].str.contains(kw, case=False, na=False)].shape[0]
print(f"Hits for 'business': {hits}")

print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-1308901072042740489': 'file_storage/function-call-1308901072042740489.json', 'var_function-call-11225229030681604654': 14860, 'var_function-call-9429883819834955631': [{'_id': '6944e5dbe888aca5de8a5407', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e5dbe888aca5de8a5408', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e5dbe888aca5de8a5409', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e5dbe888aca5de8a540a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e5dbe888aca5de8a540b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17437920335912610625': {'yearly_counts': {'2020': 1}, 'average': 1.0}}

exec(code, env_args)

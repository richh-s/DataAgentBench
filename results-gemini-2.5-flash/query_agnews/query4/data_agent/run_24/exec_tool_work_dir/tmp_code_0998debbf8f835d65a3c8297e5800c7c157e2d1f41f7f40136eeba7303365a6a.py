code = """import pandas as pd
import json

with open(locals()["var_function-call-10874147460494608809"], "r") as f:
    articles_metadata_2015 = json.load(f)

all_articles = locals()["var_function-call-5752578659838702876"]

df_metadata = pd.DataFrame(articles_metadata_2015)
df_articles = pd.DataFrame(all_articles)

df_metadata['article_id'] = df_metadata['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

merged_df = pd.merge(df_metadata, df_articles, on='article_id', how='inner')

world_keywords = ['global', 'international', 'world affairs', 'foreign policy', 'diplomacy', 'United Nations', 'UN', 'NATO', 'Europe', 'Asia', 'Africa', 'America', 'Middle East', 'geopolitics', 'conflict', 'crisis', 'war', 'peace', 'human rights', 'refugee', 'migration', 'disaster', 'climate change', 'environment']

world_articles = merged_df[merged_df['title'].str.contains('|'.join(world_keywords), case=False, na=False) | merged_df['description'].str.contains('|'.join(world_keywords), case=False, na=False)]

region_counts = world_articles['region'].value_counts().reset_index()
region_counts.columns = ['region', 'count']

if not region_counts.empty:
    most_articles_region = region_counts.loc[region_counts['count'].idxmax()]
    result = most_articles_region.to_dict()
else:
    result = {"message": "No 'World' category articles found with the current keywords."}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10874147460494608809': 'file_storage/function-call-10874147460494608809.json', 'var_function-call-15436663036104572566': 'file_storage/function-call-15436663036104572566.json', 'var_function-call-5752578659838702876': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

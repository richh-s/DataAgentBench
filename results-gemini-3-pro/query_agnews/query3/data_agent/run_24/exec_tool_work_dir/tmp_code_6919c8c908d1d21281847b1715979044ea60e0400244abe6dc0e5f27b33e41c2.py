code = """import json
import pandas as pd

# Load metadata
with open(locals()['var_function-call-3160904242471063353'], 'r') as f:
    metadata_list = json.load(f)

# Load articles (fetched sample)
with open(locals()['var_function-call-2834752330008738481'], 'r') as f:
    articles_list = json.load(f)

df_meta = pd.DataFrame(metadata_list)
df_arts = pd.DataFrame(articles_list)

# Year for all metadata
df_meta['year'] = pd.to_datetime(df_meta['publication_date']).dt.year
meta_counts = df_meta['year'].value_counts().sort_index()

# Merge
df_merged = pd.merge(df_meta, df_arts, on='article_id', how='inner')
merged_counts = df_merged['year'].value_counts().sort_index()

print("Year distribution in Metadata (Total):")
print(meta_counts)
print("\nYear distribution in Sample (Intersection):")
print(merged_counts)

print("__RESULT__:")
print(json.dumps({"meta_counts": meta_counts.to_dict(), "merged_counts": merged_counts.to_dict()}))"""

env_args = {'var_function-call-3160904242471063353': 'file_storage/function-call-3160904242471063353.json', 'var_function-call-12368714050560337210': 'file_storage/function-call-12368714050560337210.json', 'var_function-call-12354598108839559361': 14860, 'var_function-call-13777281243144311029': [{'_id': '6944d5f310c69487e5042374', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d5f310c69487e5042375', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d5f310c69487e5042376', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d5f310c69487e5042377', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d5f310c69487e5042378', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14363583995400240936': {'length': 5}, 'var_function-call-2834752330008738481': 'file_storage/function-call-2834752330008738481.json', 'var_function-call-13004323883713978964': {'counts_by_year': {'2010': 47, '2011': 64, '2012': 43, '2013': 60, '2014': 49, '2015': 58, '2016': 61, '2017': 56, '2018': 62, '2019': 49, '2020': 58}, 'average': 55.18181818181818, 'total_filtered_articles': 2273, 'business_articles_count': 607}, 'var_function-call-18328532229806693103': {'max_meta_id': 127583, 'max_art_id': 19999}, 'var_function-call-8618508822174854151': 'file_storage/function-call-8618508822174854151.json'}

exec(code, env_args)

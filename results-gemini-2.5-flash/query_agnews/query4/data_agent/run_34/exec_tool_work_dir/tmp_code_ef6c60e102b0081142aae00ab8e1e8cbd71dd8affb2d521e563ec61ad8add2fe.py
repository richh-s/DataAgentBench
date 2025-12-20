code = """import pandas as pd
import json

# Load articles data from MongoDB
articles_data = locals()['var_function-call-8187928772782996665']
df_articles = pd.DataFrame(articles_data)

# Load metadata from the file
metadata_file_path = locals()['var_function-call-9313187865657086046']
with open(metadata_file_path, 'r') as f:
    metadata_data = json.load(f)
df_metadata = pd.DataFrame(metadata_data)

# Merge the two dataframes on article_id
df_merged = pd.merge(df_articles, df_metadata, on='article_id')

# Filter for articles published in 2015
df_2015 = df_merged[df_merged['publication_date'].str.startswith('2015')]

# Identify "World" articles (case-insensitive search in title or description)
df_world_articles = df_2015[
    df_2015['title'].str.contains('World', case=False, na=False) |
    df_2015['description'].str.contains('World', case=False, na=False)
]

# Group by region and count the number of World articles
world_articles_by_region = df_world_articles['region'].value_counts().reset_index()
world_articles_by_region.columns = ['region', 'article_count']

# Find the region with the largest number of World articles
if not world_articles_by_region.empty:
    largest_region = world_articles_by_region.loc[world_articles_by_region['article_count'].idxmax()]
    result = largest_region.to_dict()
else:
    result = {"message": "No World articles found in 2015."}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-8187928772782996665': [{'_id': '6943fadfc1caf79804e91bd7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943fadfc1caf79804e91bd8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943fadfc1caf79804e91bd9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943fadfc1caf79804e91bda', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943fadfc1caf79804e91bdb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9313187865657086046': 'file_storage/function-call-9313187865657086046.json'}

exec(code, env_args)

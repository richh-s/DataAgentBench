code = """import json
import pandas as pd

# Get the article data from storage
articles_list = locals()['var_functions.query_db:4']
metadata_file_path = locals()['var_functions.query_db:5']

# Load metadata from file
with open(metadata_file_path, 'r') as f:
    metadata_list = json.load(f)

# Create DataFrames
articles_df = pd.DataFrame(articles_list)
metadata_df = pd.DataFrame(metadata_list)

# Convert publication_date to datetime
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])

# Filter for 2015 articles
metadata_2015 = metadata_df[metadata_df['publication_date'].dt.year == 2015]

# Merge with articles to get content
merged_2015 = pd.merge(articles_df, metadata_2015, on='article_id', how='inner')

# For now, let's check what we have
print('__RESULT__:')
print(json.dumps({
    'total_2015_articles': len(merged_2015),
    'all_article_ids': merged_2015['article_id'].tolist()
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': [{'_id': '6969f2d0c3421cbf4230d3d6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f2d0c3421cbf4230d3d7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f2d0c3421cbf4230d3d8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f2d0c3421cbf4230d3d9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f2d0c3421cbf4230d3da', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

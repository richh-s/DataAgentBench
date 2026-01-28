code = """import json
import pandas as pd
from datetime import datetime

# Load metadata (Europe articles 2010-2020)
metadata_file = locals()['var_functions.query_db:1']
with open(metadata_file, 'r') as f:
    metadata = json.load(f)

# Load articles data
articles_file = locals()['var_functions.query_db:11']
with open(articles_file, 'r') as f:
    articles = json.load(f)

# Convert to DataFrames
df_metadata = pd.DataFrame(metadata)
df_articles = pd.DataFrame(articles)

# Convert data types
df_metadata['article_id'] = df_metadata['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge datasets
merged_df = pd.merge(df_metadata, df_articles, on='article_id', how='inner')

# Extract year from publication_date
merged_df['publication_year'] = pd.to_datetime(merged_df['publication_date']).dt.year

# Filter for 2010-2020 inclusive
merged_df = merged_df[(merged_df['publication_year'] >= 2010) & (merged_df['publication_year'] <= 2020)]

print('__RESULT__:')
print(json.dumps({
    'total_europe_articles_2010_2020': len(merged_df),
    'year_range': f"{merged_df['publication_year'].min()} to {merged_df['publication_year'].max()}",
    'sample_data': merged_df[['article_id', 'title', 'description', 'publication_date', 'publication_year']].head(5).to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969bddbd64d6d4e4f979039', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969bddbd64d6d4e4f97903a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969bddbd64d6d4e4f97903b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969bddbd64d6d4e4f97903c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969bddbd64d6d4e4f97903d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:4': {'europe_metadata_count': 14860, 'articles_data_count': 5, 'sample_europe_metadata': [{'article_id': '3', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '9', 'region': 'Europe', 'publication_date': '2016-05-24'}, {'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}], 'sample_articles': [{'_id': '6969bddbd64d6d4e4f979039', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969bddbd64d6d4e4f97903a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969bddbd64d6d4e4f97903b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:8': [{'_id': '6969bddbd64d6d4e4f979039', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969bddbd64d6d4e4f97903a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969bddbd64d6d4e4f97903b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969bddbd64d6d4e4f97903c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969bddbd64d6d4e4f97903d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:9': {'message': 'Checking available articles and metadata structure', 'articles_count': 5, 'sample_articles': [{'_id': '6969bddbd64d6d4e4f979039', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969bddbd64d6d4e4f97903a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969bddbd64d6d4e4f97903b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969bddbd64d6d4e4f97903c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969bddbd64d6d4e4f97903d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'metadata_file_path': 'file_storage/functions.query_db:1.json'}, 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)

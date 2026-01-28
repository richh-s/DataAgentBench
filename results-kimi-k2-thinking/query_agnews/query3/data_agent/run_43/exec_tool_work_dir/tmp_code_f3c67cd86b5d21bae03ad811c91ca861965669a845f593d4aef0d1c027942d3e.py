code = """import pandas as pd
import json
import re
from datetime import datetime

# Load articles data
articles_data = locals()['var_functions.query_db:12']
if isinstance(articles_data, str) and articles_data.endswith('.json'):
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_data

# Load metadata
metadata_data = locals()['var_functions.query_db:6']
if isinstance(metadata_data, str) and metadata_data.endswith('.json'):
    with open(metadata_data, 'r') as f:
        metadata = json.load(f)
else:
    metadata = metadata_data

# Convert to DataFrames
articles_df = pd.DataFrame(articles)
metadata_df = pd.DataFrame(metadata)

# Convert data types
articles_df['article_id'] = articles_df['article_id'].astype(str)
metadata_df['article_id'] = metadata_df['article_id'].astype(str)

# Merge the data
merged_df = pd.merge(articles_df, metadata_df, on='article_id', how='inner')

# Convert publication_date to datetime
merged_df['publication_date'] = pd.to_datetime(merged_df['publication_date'])
merged_df['year'] = merged_df['publication_date'].dt.year

# Filter for Europe and years 2010-2020
europe_articles = merged_df[
    (merged_df['region'] == 'Europe') & 
    (merged_df['year'] >= 2010) & 
    (merged_df['year'] <= 2020)
]

# Display initial stats
print('__RESULT__:')
print(json.dumps({
    'merged_count': len(merged_df),
    'europe_articles_count': len(europe_articles),
    'europe_years_range': f"{europe_articles['year'].min()}-{europe_articles['year'].max()}",
    'years_in_range': len(europe_articles['year'].unique()),
    'sample_europe': europe_articles.head(3).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969cb9a60113bda38e42b31', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cb9a60113bda38e42b32', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969cb9a60113bda38e42b33', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969cb9a60113bda38e42b34', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cb9a60113bda38e42b35', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:5': ['authors', 'article_metadata'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'num_articles': 5, 'num_metadata': 127600, 'sample_article': {'_id': '6969cb9a60113bda38e42b31', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, 'sample_metadata': {'article_id': '0', 'region': 'Asia', 'publication_date': '2022-09-18'}}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'articles_count': 100000, 'metadata_count': 127600, 'articles_columns': ['_id', 'article_id', 'title', 'description'], 'metadata_columns': ['article_id', 'region', 'publication_date'], 'sample_articles': [{'_id': '6969cb9a60113bda38e42b31', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cb9a60113bda38e42b32', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}], 'sample_metadata': [{'article_id': '0', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'region': 'North America', 'publication_date': '2004-03-20'}]}}

exec(code, env_args)

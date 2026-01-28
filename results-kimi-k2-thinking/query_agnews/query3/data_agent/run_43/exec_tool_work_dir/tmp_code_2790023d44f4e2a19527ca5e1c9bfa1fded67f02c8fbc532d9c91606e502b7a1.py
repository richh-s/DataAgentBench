code = """import pandas as pd
import json
import re

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

# Check data info
print('__RESULT__:')
print(json.dumps({
    'articles_count': len(articles_df),
    'metadata_count': len(metadata_df),
    'articles_columns': articles_df.columns.tolist(),
    'metadata_columns': metadata_df.columns.tolist(),
    'sample_articles': articles_df.head(2).to_dict('records'),
    'sample_metadata': metadata_df.head(2).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969cb9a60113bda38e42b31', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cb9a60113bda38e42b32', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969cb9a60113bda38e42b33', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969cb9a60113bda38e42b34', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cb9a60113bda38e42b35', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:5': ['authors', 'article_metadata'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'num_articles': 5, 'num_metadata': 127600, 'sample_article': {'_id': '6969cb9a60113bda38e42b31', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, 'sample_metadata': {'article_id': '0', 'region': 'Asia', 'publication_date': '2022-09-18'}}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

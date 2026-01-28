code = """import json
import pandas as pd

# Load articles data
articles_data = locals()['var_functions.query_db:2']

# Load metadata from file
metadata_file = locals()['var_functions.query_db:3']
with open(metadata_file, 'r') as f:
    metadata_data = json.load(f)

# Convert to DataFrames
articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)

# Convert article_id to string for consistent merging
articles_df['article_id'] = articles_df['article_id'].astype(str)
metadata_df['article_id'] = metadata_df['article_id'].astype(str)

# Filter for 2015 articles
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_2015 = metadata_df[metadata_df['publication_date'].dt.year == 2015]

# Merge with articles
merged_2015 = pd.merge(metadata_2015, articles_df, on='article_id', how='inner')

result_dict = {
    'total_2015_articles': len(merged_2015),
    'sample_articles': []
}

if len(merged_2015) > 0:
    sample_size = min(5, len(merged_2015))
    for i in range(sample_size):
        row = merged_2015.iloc[i]
        result_dict['sample_articles'].append({
            'article_id': str(row['article_id']),
            'title': str(row['title']),
            'description': str(row['description']),
            'region': str(row['region']),
            'publication_date': str(row['publication_date'])
        })

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:10': 'No World category articles found in 2015'}

exec(code, env_args)

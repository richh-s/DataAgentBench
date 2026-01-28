code = """import json
import pandas as pd

# Read metadata data
metadata_file_path = locals()['var_functions.query_db:16']
with open(metadata_file_path, 'r') as f:
    metadata_list = json.load(f)

# Read articles data  
articles_list = locals()['var_functions.query_db:6']

# Create DataFrames
metadata_df = pd.DataFrame(metadata_list)
articles_df = pd.DataFrame(articles_list)

# Convert publication_date to datetime and extract year
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_df['year'] = metadata_df['publication_date'].dt.year

# Filter for Europe region and date range 2010-2020
europe_metadata = metadata_df[
    (metadata_df['region'] == 'Europe') & 
    (metadata_df['year'] >= 2010) & 
    (metadata_df['year'] <= 2020)
].copy()

# Merge with articles to get titles and descriptions
merged_df = pd.merge(
    europe_metadata, 
    articles_df, 
    on='article_id', 
    how='inner'
)

# Count articles by year
articles_by_year = merged_df['year'].value_counts().sort_index()

# Prepare result
total_years = 2020 - 2010 + 1
avg_articles = len(merged_df) / total_years

result = {
    'total_business_articles': len(merged_df),
    'year_range': '2010-2020',
    'average_per_year': round(avg_articles, 2),
    'articles_by_year': articles_by_year.to_dict()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969cc6d7bcfcbbdd10b3748', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cc6d7bcfcbbdd10b3749', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969cc6d7bcfcbbdd10b374a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969cc6d7bcfcbbdd10b374b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cc6d7bcfcbbdd10b374c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:5': ['authors', 'article_metadata'], 'var_functions.query_db:6': [{'_id': '6969cc6d7bcfcbbdd10b3748', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cc6d7bcfcbbdd10b3749', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969cc6d7bcfcbbdd10b374a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969cc6d7bcfcbbdd10b374b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cc6d7bcfcbbdd10b374c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

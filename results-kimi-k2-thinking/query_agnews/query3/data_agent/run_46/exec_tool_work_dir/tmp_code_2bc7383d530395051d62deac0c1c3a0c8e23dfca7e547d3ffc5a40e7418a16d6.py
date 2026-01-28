code = """import json
import pandas as pd

# Load metadata results
metadata_file = locals()['var_functions.query_db:2']

with open(metadata_file, 'r') as f:
    metadata_records = json.load(f)

# Convert to DataFrame
df_metadata = pd.DataFrame(metadata_records)

# Extract year and convert article_id to int
df_metadata['year'] = pd.to_datetime(df_metadata['publication_date']).dt.year
df_metadata['article_id'] = df_metadata['article_id'].astype(int)

# Get unique article IDs
article_ids = df_metadata['article_id'].tolist()

print('__RESULT__:')
print(json.dumps({
    'total_metadata_articles': len(article_ids),
    'unique_articles': len(set(article_ids)),
    'year_range': f"{df_metadata['year'].min()} to {df_metadata['year'].max()}",
    'sample_article_ids': article_ids[:10]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_articles_by_year': [{'year': 2010, 'total_articles': 1306}, {'year': 2011, 'total_articles': 1316}, {'year': 2012, 'total_articles': 1355}, {'year': 2013, 'total_articles': 1354}, {'year': 2014, 'total_articles': 1372}, {'year': 2015, 'total_articles': 1357}, {'year': 2016, 'total_articles': 1364}, {'year': 2017, 'total_articles': 1391}, {'year': 2018, 'total_articles': 1351}, {'year': 2019, 'total_articles': 1328}, {'year': 2020, 'total_articles': 1366}], 'unique_years': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], 'total_articles': 14860}, 'var_functions.execute_python:8': {'total_article_ids': 14860, 'first_few': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'last_few': [127521, 127525, 127561, 127564, 127566, 127567, 127572, 127576, 127577, 127583]}, 'var_functions.execute_python:10': {'year_distribution': {'2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357, '2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366}, 'total_articles': 14860}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'_id': '6969cd03bb7b6acbbe34651c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cd03bb7b6acbbe34651d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969cd03bb7b6acbbe34651e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969cd03bb7b6acbbe34651f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cd03bb7b6acbbe346520', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

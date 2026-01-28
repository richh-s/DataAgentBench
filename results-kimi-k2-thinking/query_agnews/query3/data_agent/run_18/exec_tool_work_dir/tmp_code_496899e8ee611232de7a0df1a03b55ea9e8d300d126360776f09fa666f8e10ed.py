code = """import json
# Access stored results using locals()
articles_data = locals()['var_functions.query_db:2']
metadata_data = locals()['var_functions.query_db:6']
# Convert to DataFrames for analysis
import pandas as pd
articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)
# Show basic info
print('__RESULT__:')
print(json.dumps({
    'articles_count': len(articles_df),
    'metadata_count': len(metadata_df),
    'articles_columns': list(articles_df.columns),
    'metadata_columns': list(metadata_df.columns)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969b9bf2924af7adfb78d0e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b9bf2924af7adfb78d0f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b9bf2924af7adfb78d10', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b9bf2924af7adfb78d11', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b9bf2924af7adfb78d12', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': [{'article_id': '0', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'region': 'Europe', 'publication_date': '2016-05-24'}]}

exec(code, env_args)

code = """import json
import pandas as pd
import re

# Read metadata
metadata_file = locals()['var_functions.query_db:14']
with open(metadata_file, 'r') as f:
    metadata_all = json.load(f)

metadata_df = pd.DataFrame(metadata_all)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])

# Filter for Europe region and 2010-2020
europe_2010_2020 = metadata_df[
    (metadata_df['region'] == 'Europe') & 
    (metadata_df['publication_date'] >= '2010-01-01') & 
    (metadata_df['publication_date'] <= '2020-12-31')
].copy()

europe_article_ids = set(europe_2010_2020['article_id'].astype(str))

# Read articles
articles_file = locals()['var_functions.query_db:28']
with open(articles_file, 'r') as f:
    articles_all = json.load(f)

articles_df = pd.DataFrame(articles_all)

# Filter for articles in Europe 2010-2020
europe_articles = articles_df[articles_df['article_id'].astype(str).isin(europe_article_ids)]

# Classify business articles
business_keywords = [
    'wall st', 'stock', 'economy', 'economic', 'oil', 'trade', 'dollar', 'inflation', 'interest',
    'market', 'business', 'company', 'finance', 'financial', 'bank', 'invest', 'investment',
    'share', 'profit', 'loss', 'revenue', 'sales', 'deal', 'merger', 'acquisition', 'ipo',
    'fund', 'bond', 'currency', 'price', 'cost', 'budget', 'deficit', 'surplus'
]

def is_business_article(title, description):
    text = f"{title} {description}".lower()
    return any(keyword in text for keyword in business_keywords)

europe_articles['is_business'] = europe_articles.apply(
    lambda row: is_business_article(row['title'], row['description']), 
    axis=1
)

business_articles = europe_articles[europe_articles['is_business']]

# Merge with metadata to get years
business_with_dates = business_articles.merge(
    europe_2010_2020[['article_id', 'publication_date']], 
    on='article_id', 
    how='left'
)

business_with_dates['year'] = business_with_dates['publication_date'].dt.year

# Count per year
business_per_year = business_with_dates.groupby('year').size()

# Calculate average
average_business_per_year = business_per_year.mean()

result = {
    'total_business_articles': len(business_articles),
    'average_per_year': round(average_business_per_year, 2),
    'articles_by_year': business_per_year.to_dict()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969b9bf2924af7adfb78d0e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b9bf2924af7adfb78d0f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b9bf2924af7adfb78d10', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b9bf2924af7adfb78d11', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b9bf2924af7adfb78d12', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': [{'article_id': '0', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.execute_python:10': {'articles_count': 5, 'metadata_count': 10, 'articles_columns': ['_id', 'article_id', 'title', 'description'], 'metadata_columns': ['article_id', 'region', 'publication_date']}, 'var_functions.query_db:12': [{'_id': '6969b9bf2924af7adfb78d0e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b9bf2924af7adfb78d0f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b9bf2924af7adfb78d10', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b9bf2924af7adfb78d11', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b9bf2924af7adfb78d12', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': "<class 'str'>", 'var_functions.execute_python:22': {'file_path': 'file_storage/functions.query_db:14.json', 'total_metadata_records': 127600, 'sample': {'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}}, 'var_functions.execute_python:24': {'total_europe_articles_2010_2020': 14860}, 'var_functions.query_db:26': [{'_id': '6969b9bf2924af7adfb78d0e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b9bf2924af7adfb78d0f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b9bf2924af7adfb78d10', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b9bf2924af7adfb78d11', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b9bf2924af7adfb78d12', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)

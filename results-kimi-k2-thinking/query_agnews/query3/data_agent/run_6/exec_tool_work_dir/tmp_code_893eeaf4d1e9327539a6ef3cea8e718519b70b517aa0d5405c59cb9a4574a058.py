code = """import json
import pandas as pd
from datetime import datetime
import re

# Load article data
articles_file_path = locals()['var_functions.query_db:10']
if isinstance(articles_file_path, str):
    with open(articles_file_path, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_file_path

# Load metadata
metadata_file_path = locals()['var_functions.query_db:3']
if isinstance(metadata_file_path, str):
    with open(metadata_file_path, 'r') as f:
        metadata = json.load(f)
else:
    metadata = metadata_file_path

# Create DataFrames
df_articles = pd.DataFrame(articles)
df_metadata = pd.DataFrame(metadata)

# Convert data types
df_metadata['publication_date'] = pd.to_datetime(df_metadata['publication_date'])

# Merge articles with metadata
df_merged = pd.merge(df_articles, df_metadata, on='article_id')

# Filter for Europe and date range 2010-2020
df_europe = df_merged[
    (df_merged['region'] == 'Europe') & 
    (df_merged['publication_date'] >= '2010-01-01') & 
    (df_merged['publication_date'] <= '2020-12-31')
].copy()

# Categorize business articles
business_keywords = [
    'business', 'economy', 'stock', 'market', 'bank', 'finance', 'financial', 'investment', 
    'oil', 'price', 'trade', 'deficit', 'company', 'economic', 'corporate', 'economics',
    'fed', 'federal', 'gdp', 'inflation', 'rate', 'rates', 'dollar', 'wall st', 'wall street'
]

def is_business_article(title, description):
    if pd.isna(title):
        title = ''
    if pd.isna(description):
        description = ''
    
    text = (str(title) + ' ' + str(description)).lower()
    
    for keyword in business_keywords:
        if keyword in text:
            return True
    return False

# Apply categorization
df_europe['is_business'] = df_europe.apply(
    lambda row: is_business_article(row['title'], row['description']), 
    axis=1
)

# Count business articles per year
df_europe['year'] = df_europe['publication_date'].dt.year
df_business = df_europe[df_europe['is_business']].copy()

yearly_counts = df_business.groupby('year').size()
valid_years = list(range(2010, 2021))
yearly_counts = yearly_counts.reindex(valid_years, fill_value=0)

average_per_year = yearly_counts.mean()

total_business_articles = len(df_business)
total_years = len(valid_years)

result = {
    'total_business_articles_europe_2010_2020': int(total_business_articles),
    'years_in_range': valid_years,
    'articles_per_year': {int(year): int(count) for year, count in yearly_counts.items()},
    'average_per_year': round(float(average_per_year), 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969ad585f1dd578168de6d3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969ad585f1dd578168de6d4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969ad585f1dd578168de6d5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969ad585f1dd578168de6d6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969ad585f1dd578168de6d7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:8': {'metadata_records': 127600, 'article_records': 5, 'metadata_columns': ['article_id', 'author_id', 'region', 'publication_date'], 'articles_columns': ['_id', 'article_id', 'title', 'description']}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)

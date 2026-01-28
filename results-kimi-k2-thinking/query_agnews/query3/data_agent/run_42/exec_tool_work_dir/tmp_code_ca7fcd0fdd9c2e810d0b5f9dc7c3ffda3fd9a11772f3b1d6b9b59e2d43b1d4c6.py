code = """import json
import pandas as pd

# Read the metadata query result file
metadata_file_path = var_functions.query_db:6
with open(metadata_file_path, 'r') as f:
    europe_metadata = json.load(f)

# Read the articles query result file
articles_file_path = var_functions.query_db:2
with open(articles_file_path, 'r') as f:
    articles = json.load(f)

# Convert to DataFrames
df_metadata = pd.DataFrame(europe_metadata)
df_articles = pd.DataFrame(articles)

# Ensure article_id is string in both for merging
df_metadata['article_id'] = df_metadata['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge the dataframes
merged_df = pd.merge(df_metadata, df_articles, on='article_id', how='left')

# Extract year from publication_date
merged_df['publication_year'] = pd.to_datetime(merged_df['publication_date']).dt.year

# Filter for 2010-2020 range
filtered_df = merged_df[(merged_df['publication_year'] >= 2010) & (merged_df['publication_year'] <= 2020)]

# Define business keywords
business_keywords = ['business', 'economy', 'economic', 'stock', 'stocks', 'wall st', 'wall street', 'oil', 'trade', 'market', 'investment', 'invest', 'finance', 'financial', 'company', 'companies', 'ipo', 'profit', 'loss', 'rate', 'rates', 'bank', 'dollar', 'euro', 'pound', 'gbp', 'usd', 'eurozone', 'share', 'shares', 'price', 'prices', 'growth', 'gdp', 'inflation', 'deficit', 'budget']

# Classify business articles
business_articles = []
for idx, row in filtered_df.iterrows():
    title = str(row['title']).lower() if pd.notna(row['title']) else ''
    description = str(row['description']).lower() if pd.notna(row['description']) else ''
    text = title + ' ' + description
    is_business = any(keyword in text for keyword in business_keywords)
    if is_business:
        business_articles.append(row['publication_year'])

# Count business articles per year
from collections import Counter
year_counts = Counter(business_articles)

# Calculate average
years = sorted(year_counts.keys())
total_business = sum(year_counts.values())
avg_business = total_business / len(years) if years else 0

result = {
    'average_business_articles_per_year': round(avg_business, 2),
    'total_business_articles': total_business,
    'total_years': len(years),
    'yearly_counts': dict(year_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}, {'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '14', 'author_id': '223', 'region': 'Europe', 'publication_date': '2017-09-08'}, {'article_id': '16', 'author_id': '814', 'region': 'Europe', 'publication_date': '2007-01-17'}, {'article_id': '21', 'author_id': '674', 'region': 'Europe', 'publication_date': '2020-04-06'}, {'article_id': '23', 'author_id': '153', 'region': 'Europe', 'publication_date': '2008-02-25'}, {'article_id': '27', 'author_id': '244', 'region': 'Europe', 'publication_date': '2013-09-07'}, {'article_id': '43', 'author_id': '154', 'region': 'Europe', 'publication_date': '2010-03-12'}, {'article_id': '44', 'author_id': '520', 'region': 'Europe', 'publication_date': '2007-03-07'}, {'article_id': '55', 'author_id': '954', 'region': 'Europe', 'publication_date': '2021-12-17'}, {'article_id': '58', 'author_id': '473', 'region': 'Europe', 'publication_date': '2006-03-05'}, {'article_id': '60', 'author_id': '530', 'region': 'Europe', 'publication_date': '2017-04-30'}, {'article_id': '62', 'author_id': '328', 'region': 'Europe', 'publication_date': '2018-09-12'}, {'article_id': '63', 'author_id': '83', 'region': 'Europe', 'publication_date': '2010-04-19'}, {'article_id': '64', 'author_id': '34', 'region': 'Europe', 'publication_date': '2018-03-11'}, {'article_id': '66', 'author_id': '793', 'region': 'Europe', 'publication_date': '2010-03-12'}, {'article_id': '73', 'author_id': '187', 'region': 'Europe', 'publication_date': '2007-08-25'}, {'article_id': '78', 'author_id': '303', 'region': 'Europe', 'publication_date': '2019-07-08'}, {'article_id': '93', 'author_id': '82', 'region': 'Europe', 'publication_date': '2007-06-16'}, {'article_id': '110', 'author_id': '696', 'region': 'Europe', 'publication_date': '2022-01-27'}, {'article_id': '114', 'author_id': '233', 'region': 'Europe', 'publication_date': '2008-09-08'}, {'article_id': '120', 'author_id': '123', 'region': 'Europe', 'publication_date': '2007-07-29'}, {'article_id': '128', 'author_id': '101', 'region': 'Europe', 'publication_date': '2019-09-27'}, {'article_id': '135', 'author_id': '781', 'region': 'Europe', 'publication_date': '2008-01-30'}, {'article_id': '140', 'author_id': '736', 'region': 'Europe', 'publication_date': '2010-06-02'}, {'article_id': '142', 'author_id': '383', 'region': 'Europe', 'publication_date': '2017-06-01'}, {'article_id': '143', 'author_id': '55', 'region': 'Europe', 'publication_date': '2018-03-01'}, {'article_id': '144', 'author_id': '57', 'region': 'Europe', 'publication_date': '2017-07-22'}, {'article_id': '151', 'author_id': '459', 'region': 'Europe', 'publication_date': '2014-04-21'}, {'article_id': '154', 'author_id': '353', 'region': 'Europe', 'publication_date': '2013-01-08'}, {'article_id': '164', 'author_id': '40', 'region': 'Europe', 'publication_date': '2017-04-17'}, {'article_id': '171', 'author_id': '702', 'region': 'Europe', 'publication_date': '2008-07-05'}, {'article_id': '179', 'author_id': '971', 'region': 'Europe', 'publication_date': '2015-04-27'}, {'article_id': '181', 'author_id': '186', 'region': 'Europe', 'publication_date': '2019-08-11'}, {'article_id': '187', 'author_id': '187', 'region': 'Europe', 'publication_date': '2006-02-17'}, {'article_id': '190', 'author_id': '840', 'region': 'Europe', 'publication_date': '2016-11-07'}, {'article_id': '201', 'author_id': '431', 'region': 'Europe', 'publication_date': '2013-06-08'}, {'article_id': '202', 'author_id': '221', 'region': 'Europe', 'publication_date': '2014-08-23'}, {'article_id': '203', 'author_id': '322', 'region': 'Europe', 'publication_date': '2015-05-13'}, {'article_id': '210', 'author_id': '100', 'region': 'Europe', 'publication_date': '2016-08-06'}, {'article_id': '214', 'author_id': '338', 'region': 'Europe', 'publication_date': '2019-02-11'}, {'article_id': '216', 'author_id': '317', 'region': 'Europe', 'publication_date': '2011-07-13'}, {'article_id': '219', 'author_id': '771', 'region': 'Europe', 'publication_date': '2009-10-13'}, {'article_id': '223', 'author_id': '941', 'region': 'Europe', 'publication_date': '2020-10-28'}, {'article_id': '229', 'author_id': '827', 'region': 'Europe', 'publication_date': '2006-12-13'}, {'article_id': '243', 'author_id': '930', 'region': 'Europe', 'publication_date': '2015-04-12'}, {'article_id': '257', 'author_id': '398', 'region': 'Europe', 'publication_date': '2017-12-26'}, {'article_id': '260', 'author_id': '441', 'region': 'Europe', 'publication_date': '2022-09-22'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

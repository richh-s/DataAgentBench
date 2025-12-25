code = """import pandas as pd
import json

articles_data = locals()['var_function-call-9022436256339260127']['query_db_response']['results']
with open(locals()['var_function-call-6955627396248602295'], 'r') as f:
    metadata_data = json.load(f)

articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)

# Convert article_id to string to ensure consistent type for merging
articles_df['article_id'] = articles_df['article_id'].astype(str)
metadata_df['article_id'] = metadata_df['article_id'].astype(str)

# Filter for articles published in Europe between 2010 and 2020
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
filtered_metadata_df = metadata_df[
    (metadata_df['region'] == 'Europe') &
    (metadata_df['publication_date'].dt.year >= 2010) &
    (metadata_df['publication_date'].dt.year <= 2020)
]

# Merge the two dataframes
merged_df = pd.merge(articles_df, filtered_metadata_df, on='article_id', how='inner')

# Identify business articles based on keywords in title and description
business_keywords = ['business', 'economy', 'market', 'financial', 'stocks', 'trade', 'corporate', 'companies', 'industry', 'invest', 'economic', 'ceo']
def is_business_article(title, description):
    if isinstance(title, str) and any(keyword in title.lower() for keyword in business_keywords):
        return True
    if isinstance(description, str) and any(keyword in description.lower() for keyword in business_keywords):
        return True
    return False

merged_df['is_business'] = merged_df.apply(lambda row: is_business_article(row['title'], row['description']), axis=1)

business_articles_df = merged_df[merged_df['is_business']]

# Extract year from publication_date
business_articles_df['year'] = business_articles_df['publication_date'].dt.year

# Count business articles per year
articles_per_year = business_articles_df.groupby('year').size().reset_index(name='count')

# Calculate the average
average_articles = articles_per_year['count'].mean()

print('__RESULT__:')
print(json.dumps(average_articles))"""

env_args = {'var_function-call-9022436256339260127': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6955627396248602295': 'file_storage/function-call-6955627396248602295.json'}

exec(code, env_args)

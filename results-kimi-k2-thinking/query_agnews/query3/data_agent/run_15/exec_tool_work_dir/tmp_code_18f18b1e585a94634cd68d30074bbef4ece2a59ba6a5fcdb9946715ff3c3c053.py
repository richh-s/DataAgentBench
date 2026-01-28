code = """import json
import pandas as pd
from pathlib import Path

# Access the stored metadata query result
metadata_file = locals()['var_functions.query_db:8']

# Read the full metadata from the file
with open(metadata_file, 'r') as f:
    metadata = json.load(f)

# Convert to DataFrame for easier processing
metadata_df = pd.DataFrame(metadata)

# Filter for Europe region and date range 2010-2020
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_filtered = metadata_df[
    (metadata_df['region'] == 'Europe') & 
    (metadata_df['publication_date'] >= '2010-01-01') & 
    (metadata_df['publication_date'] <= '2020-12-31')
].copy()

# Extract year
metadata_filtered['year'] = metadata_filtered['publication_date'].dt.year

# Get all articles from the small sample we retrieved earlier
articles_sample = locals()['var_functions.query_db:6']

# Create DataFrame from articles
articles_df = pd.DataFrame(articles_sample)

# Define function to classify business articles based on title/description
# Based on hints, we need to extract business-related keywords
def is_business_article(title, description):
    if not title and not description:
        return False
    
    # Keywords for business articles
    business_keywords = [
        'wall st', 'business', 'economy', 'stocks', 'stock market', 'oil', 'prices',
        'commercial', 'investment', 'firm', 'company', 'companies', 'market',
        'finance', 'financial', 'trade', 'trading', 'profit', 'loss', 'revenue'
    ]
    
    text = f"{title} {description}".lower()
    return any(keyword in text for keyword in business_keywords)

# Apply classification to sample articles
if not articles_df.empty:
    articles_df['is_business'] = articles_df.apply(
        lambda row: is_business_article(row.get('title', ''), row.get('description', '')), 
        axis=1
    )
    
    # Merge with metadata
    merged_df = pd.merge(
        metadata_filtered, 
        articles_df[['article_id', 'is_business']], 
        on='article_id', 
        how='inner'
    )
    
    # Filter for business articles
    business_articles = merged_df[merged_df['is_business'] == True]
    
    # Count business articles per year
    business_by_year = business_articles.groupby('year').size().reset_index(name='count')
    
    # Calculate average
    if not business_by_year.empty:
        average_per_year = business_by_year['count'].mean()
        total_years = len(business_by_year)
        total_articles = business_by_year['count'].sum()
    else:
        average_per_year = 0
        total_years = 0
        total_articles = 0
else:
    average_per_year = 0
    total_years = 0
    total_articles = 0

result = {
    'average_business_articles_per_year': round(average_per_year, 2),
    'total_years_with_data': total_years,
    'total_business_articles': total_articles,
    'years': business_by_year.to_dict('records') if 'business_by_year' in locals() else []
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969b785cac35b9b0168bab8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b785cac35b9b0168bab9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b785cac35b9b0168baba', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b785cac35b9b0168babb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b785cac35b9b0168babc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:4': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.query_db:6': [{'_id': '6969b785cac35b9b0168bab8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b785cac35b9b0168bab9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b785cac35b9b0168baba', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b785cac35b9b0168babb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b785cac35b9b0168babc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

code = """import json
import pandas as pd
from datetime import datetime
import re

# Load all articles
articles_file_path = locals()['var_functions.query_db:16']
with open(articles_file_path, 'r') as f:
    all_articles = json.load(f)

# Load European articles metadata 
metadata_file_path = locals()['var_functions.query_db:5']
with open(metadata_file_path, 'r') as f:
    europe_metadata = json.load(f)

print(f'Total articles in database: {len(all_articles)}')
print(f'European articles (2010-2020): {len(europe_metadata)}')

# Create lookup for articles
articles_lookup = {article['article_id']: article for article in all_articles}

# Define business keywords
business_keywords = [
    'business', 'economy', 'economic', 'stock', 'stocks', 'wall st', 'wall street',
    'finance', 'financial', 'investment', 'investing', 'market', 'markets',
    'trade', 'trading', 'corporate', 'company', 'companies', 'bank', 'banking',
    'oil', 'oil prices', 'energy', 'gas', 'currency', 'dollar', 'euro',
    'IPO', 'profit', 'loss', 'revenue', 'sales', 'merger', 'acquisition',
    'industry', 'sector', 'retail', 'commercial', 'federal reserve', 'fed'
]

# Function to determine if article is business-related
def is_business_article(title, description):
    title_lower = title.lower() if title else ''
    desc_lower = description.lower() if description else ''
    
    combined = title_lower + ' ' + desc_lower
    
    business_count = sum(1 for keyword in business_keywords if keyword in combined)
    return business_count >= 2  # At least 2 business keywords to classify as business

# Process European articles to find business articles
europe_business_articles = []

for meta in europe_metadata:
    article_id = meta['article_id']
    publication_date = meta['publication_date']
    
    # Get article details
    article = articles_lookup.get(article_id)
    if not article:
        continue
    
    title = article.get('title', '')
    description = article.get('description', '')
    
    # Check if business article
    if is_business_article(title, description):
        year = int(publication_date.split('-')[0])
        europe_business_articles.append({
            'article_id': article_id,
            'year': year,
            'title': title,
            'date': publication_date
        })

print(f'Number of European business articles: {len(europe_business_articles)}')

# Create DataFrame and calculate average per year
if europe_business_articles:
    df = pd.DataFrame(europe_business_articles)
    
    # Filter years 2010-2020
    df_filtered = df[(df['year'] >= 2010) & (df['year'] <= 2020)]
    
    # Count articles per year
    year_counts = df_filtered['year'].value_counts().sort_index()
    
    # Calculate average
    if len(year_counts) > 0:
        average_per_year = year_counts.mean()
        print(f'Average business articles per year (2010-2020): {average_per_year:.2f}')
        print('Yearly breakdown:')
        print(year_counts.to_string())
    else:
        average_per_year = 0
        print('No business articles found in the specified date range')
else:
    average_per_year = 0

print('__RESULT__:')
print(json.dumps({
    'total_europe_articles': len(europe_metadata),
    'europe_business_articles': len(europe_business_articles),
    'average_per_year': round(average_per_year, 2) if 'average_per_year' in locals() else 0,
    'yearly_counts': year_counts.to_dict() if 'year_counts' in locals() else {}
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969bcab3620faa886932b41', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969bcab3620faa886932b42', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969bcab3620faa886932b43', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969bcab3620faa886932b44', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969bcab3620faa886932b45', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [{'_id': '6969bcab3620faa886932b41', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969bcab3620faa886932b42', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969bcab3620faa886932b43', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969bcab3620faa886932b44', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969bcab3620faa886932b45', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:15': 'Loaded data successfully', 'var_functions.query_db:14': [{'_id': '6969bcab3620faa886932b41', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969bcab3620faa886932b42', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969bcab3620faa886932b43', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969bcab3620faa886932b44', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969bcab3620faa886932b45', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

code = """import json
import os
import re
from datetime import datetime

# Load Europe metadata (2010-2020)
metadata_key = 'var_functions.query_db:8'
metadata_result = locals().get(metadata_key)

if isinstance(metadata_result, str) and metadata_result.endswith('.json'):
    with open(metadata_result, 'r') as f:
        europe_metadata = json.load(f)
else:
    europe_metadata = metadata_result

# Load all articles
articles_key = 'var_functions.query_db:16'
articles_result = locals().get(articles_key)

if isinstance(articles_result, str) and articles_result.endswith('.json'):
    with open(articles_result, 'r') as f:
        articles_data = json.load(f)
else:
    articles_data = articles_result

# Create a dictionary for fast lookup of articles by ID
articles_dict = {str(article['article_id']): article for article in articles_data}

# Filter business articles in Europe metadata
business_keywords = ['wall st', 'wall street', 'stock', 'stocks', 'economy', 'economic', 'oil price', 'oil prices', 'interest rate', 'interest rates', 'market', 'markets', 'trade', 'trade deficit', 'exchange', 'currency', 'investment', 'funds', 'bonds', 'commodity', 'commodities', 'real estate', 'property', 'bank', 'banks', 'banking', 'profit', 'loss', 'earnings', 'revenue', 'sales', 'capital', 'asset', 'assets', 'finance', 'financial', 'share', 'shares', 'equity', 'equities', 'gold', 'silver', 'loan', 'loans']

europe_business_articles = []

for meta_item in europe_metadata:
    article_id = str(meta_item['article_id'])
    if article_id in articles_dict:
        article = articles_dict[article_id]
        title = article.get('title', '').lower()
        description = article.get('description', '').lower()
        
        # Check if it's a business article
        has_business_keyword = any(keyword in title or keyword in description for keyword in business_keywords)
        
        if has_business_keyword:
            year = int(meta_item['publication_date'][:4])
            europe_business_articles.append({
                'article_id': article_id,
                'year': year,
                'publication_date': meta_item['publication_date']
            })

# Group by year and count
year_counts = {}
for article in europe_business_articles:
    year = article['year']
    year_counts[year] = year_counts.get(year, 0) + 1

# Calculate average
if year_counts:
    total_articles = sum(year_counts.values())
    years_covered = len(year_counts)
    avg_per_year = total_articles / years_covered
else:
    avg_per_year = 0

print('__RESULT__:')
print(json.dumps({
    'avg_per_year': round(avg_per_year, 2),
    'total_business_articles': len(europe_business_articles),
    'total_europe_articles': len(europe_metadata),
    'sample_year_counts': dict(list(year_counts.items())[:5])
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969a9e8d3fee090036ad705', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969a9e8d3fee090036ad706', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969a9e8d3fee090036ad707', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969a9e8d3fee090036ad708', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969a9e8d3fee090036ad709', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'count': '127600'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_europe_articles': 14860, 'sample_europe_ids': ['3', '9', '13', '14', '21'], 'total_articles_in_db': 5, 'sample_article_ids': ['0', '1', '2', '3', '4']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)

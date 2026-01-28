code = """import json
import os
import re

# Access the Europe articles metadata file path
metadata_file = locals()['var_functions.query_db:2']

# Open and read the full Europe articles metadata
with open(metadata_file, 'r') as f:
    europe_articles = json.load(f)

# Access the articles data
articles_data = locals()['var_functions.query_db:4']

# If it's a file path, read it; if it's already data, use it directly
if isinstance(articles_data, str) and os.path.exists(articles_data):
    with open(articles_data, 'r') as f:
        all_articles = json.load(f)
else:
    all_articles = articles_data

print(f"Number of Europe articles: {len(europe_articles)}")
print(f"Number of all articles: {len(all_articles)}")

# Extract Europe article IDs
europe_article_ids = set(str(art['article_id']) for art in europe_articles)

# Filter articles to only include those from Europe
europe_articles_content = [art for art in all_articles if str(art['article_id']) in europe_article_ids]

print(f"Number of Europe article content pieces: {len(europe_articles_content)}")

# Create a dictionary for faster lookup
articles_dict = {str(art['article_id']): art for art in europe_articles_content}

# Refined Business classification logic
def is_business_article(article):
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    text = f"{title} {description}"
    
    # Business indicators
    business_markers = [
        'wall st', 'wall street', 'stock market', 'stocks', 'stock', 'economy', 'economic',
        'finance', 'financial', 'investment', 'investing', 'investor', 'investors',
        'company', 'companies', 'corporation', 'corporate', 'business',
        'bank', 'banking', 'bankruptcy', 'earnings', 'revenue', 'profit', 'losses',
        'quarterly', 'shares', 'trading', 'trade', 'deal', 'acquisition', 'merger',
        'oil prices', 'crude prices', 'commodity', 'market outlook', 'economic menace'
    ]
    
    # Check for business markers
    for marker in business_markers:
        if marker in text:
            return True
    
    # Check for specific business contexts
    if 'reuters' in text and ('oil' in text and ('economy' in text or 'prices' in text)):
        return True
        
    return False

# Classify all Europe articles
business_articles = []
for article_id, article in articles_dict.items():
    if is_business_article(article):
        business_articles.append(article)

print(f"Number of Business articles identified: {len(business_articles)}")

# Count Business articles by year
from collections import Counter
business_year_counts = Counter()

for meta in europe_articles:
    article_id = str(meta['article_id'])
    if article_id in articles_dict and is_business_article(articles_dict[article_id]):
        date = meta.get('publication_date', '')
        if date:
            year = date.split('-')[0]
            business_year_counts[year] += 1

# Count total articles by year for reference
total_year_counts = Counter()
for meta in europe_articles:
    date = meta.get('publication_date', '')
    if date:
        year = date.split('-')[0]
        total_year_counts[year] += 1

print("Business articles by year:", dict(business_year_counts))
print("Total articles by year:", dict(total_year_counts))

# Calculate average Business articles per year from 2010-2020
years = [str(y) for y in range(2010, 2021)]
business_counts = [business_year_counts.get(year, 0) for year in years]
total_business = sum(business_counts)
average_business = total_business / len(years) if years else 0

# Calculate total Europe articles for the same period
total_europe_counts = [total_year_counts.get(year, 0) for year in years]
total_europe = sum(total_europe_counts)

print(f"Total Business articles (2010-2020): {total_business}")
print(f"Average Business articles per year: {average_business:.2f}")
print(f"Total Europe articles (2010-2020): {total_europe}")

# Show some examples of Business articles
print("Sample Business articles:")
for i, art in enumerate(business_articles[:5]):
    title = art.get('title', 'No title')
    print(str(i+1) + ". " + title)

# Prepare result
result = {
    'average_business_articles_per_year': round(average_business, 2),
    'total_business_articles_2010_2020': total_business,
    'business_articles_by_year': dict(business_year_counts),
    'total_europe_articles_2010_2020': total_europe,
    'sample_business_articles': [art.get('title', '') for art in business_articles[:3]]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860}}

exec(code, env_args)

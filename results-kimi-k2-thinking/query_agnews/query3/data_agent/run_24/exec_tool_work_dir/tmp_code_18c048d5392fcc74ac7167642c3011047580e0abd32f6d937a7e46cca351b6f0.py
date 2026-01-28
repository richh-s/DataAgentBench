code = """import json
import os
import re
from collections import defaultdict

# Load European articles metadata (already filtered by date and region)
metadata_file = locals()['var_functions.query_db:12']
if os.path.exists(metadata_file):
    with open(metadata_file, 'r') as f:
        europe_metadata = json.load(f)
else:
    europe_metadata = []

# Load all articles
all_articles = locals()['var_functions.query_db:2']

# Create a dictionary for quick lookup of articles by article_id
articles_dict = {str(art['article_id']): art for art in all_articles}

# Define business keywords to identify business articles
business_keywords = [
    'business', 'economy', 'economic', 'stock', 'stocks', 'wall st', 'wall street',
    'finance', 'financial', 'market', 'markets', 'trade', 'trading', 'investment',
    'investing', 'investor', 'company', 'companies', 'corporate', 'corporation',
    'bank', 'banking', 'oil', 'price', 'prices', 'profit', 'loss', 'revenue',
    'sales', 'earnings', 'quarter', 'economist', 'fund', 'funds', 'capital',
    'industry', 'industries', 'sector', 'sectors', 'commercial', 'enterprise',
    'entrepreneur', 'startup', 'start-up', 'venture', 'private equity', 'ipo',
    'initial public offering', 'merger', 'acquisition', 'takeover', 'deal', 'deals'
]

def is_business_article(title, description):
    """Determine if an article is a business article based on title and description."""
    text = f"{title} {description}".lower()
    for keyword in business_keywords:
        if keyword in text:
            return True
    return False

# Filter to get only business articles from Europe (2010-2020)
europe_business_articles = []
for meta in europe_metadata:
    article_id = meta['article_id']
    if article_id in articles_dict:
        article = articles_dict[article_id]
        if is_business_article(article['title'], article['description']):
            europe_business_articles.append({
                'article_id': article_id,
                'title': article['title'],
                'description': article['description'],
                'publication_date': meta['publication_date'],
                'year': int(meta['publication_date'][:4])
            })

# Count articles per year
year_counts = defaultdict(int)
for art in europe_business_articles:
    year_counts[art['year']] += 1

# Calculate average (only include years 2010-2020 that have data)
total_years = 2020 - 2010 + 1  # 11 years
total_articles = sum(year_counts.values())
average_per_year = total_articles / total_years if total_years > 0 else 0

# Sort by year for display
sorted_years = sorted(year_counts.items())

# Prepare result
result = {
    'total_europe_business_articles': len(europe_business_articles),
    'year_range': '2010-2020',
    'average_per_year': round(average_per_year, 2),
    'articles_per_year': dict(sorted_years)
}

print('----BEGIN PRINT FORMAT----')
print('__RESULT__:')
print(json.dumps(result))
print('----END PRINT FORMAT----')"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969be2e66733a3d1d7f9c82', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969be2e66733a3d1d7f9c83', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969be2e66733a3d1d7f9c84', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969be2e66733a3d1d7f9c85', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969be2e66733a3d1d7f9c86', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

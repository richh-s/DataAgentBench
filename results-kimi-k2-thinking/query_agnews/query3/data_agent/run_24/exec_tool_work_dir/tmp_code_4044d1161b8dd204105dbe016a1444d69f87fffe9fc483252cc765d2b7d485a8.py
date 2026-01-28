code = """import json
import re
from collections import defaultdict

# Load all articles (5 total)
all_articles = locals()['var_functions.query_db:26']

# Load European metadata (2010-2020)
metadata_file = locals()['var_functions.query_db:12']
with open(metadata_file, 'r') as f:
    europe_metadata = json.load(f)

# Create set of European article IDs for quick lookup
european_article_ids = set()
europe_articles_by_year = defaultdict(int)

for meta in europe_metadata:
    article_id = meta['article_id']
    european_article_ids.add(article_id)
    year = int(meta['publication_date'][:4])
    europe_articles_by_year[year] += 1

# Business keywords
business_keywords = [
    'business', 'economy', 'economic', 'stock', 'stocks', 'wall st', 'wall street',
    'finance', 'financial', 'market', 'markets', 'trade', 'trading', 'investment',
    'investing', 'investor', 'company', 'companies', 'corporate', 'corporation',
    'bank', 'banking', 'oil', 'price', 'prices', 'profit', 'loss', 'revenue',
    'sales', 'earnings', 'quarter', 'economist', 'fund', 'funds', 'capital',
    'industry', 'industries', 'sector', 'sectors', 'commercial', 'enterprise', '
    'entrepreneur', 'startup', 'start-up', 'venture', 'private equity', 'ipo',
    'initial public offering', 'merger', 'acquisition', 'takeover', 'deal', 'deals'
]

def is_business_article(title, description):
    """Check if article is business-related"""
    text = (title + ' ' + description).lower()
    # Check for keywords, but avoid false positives
    if any(keyword in text for keyword in business_keywords):
        return True
    return False

# Analyze the articles we have
business_articles_found = []
for article in all_articles:
    article_id = str(article['article_id'])
    if article_id in european_article_ids:
        if is_business_article(article['title'], article['description']):
            # Find the metadata for this article
            for meta in europe_metadata:
                if meta['article_id'] == article_id:
                    year = int(meta['publication_date'][:4])
                    business_articles_found.append({
                        'article_id': article_id,
                        'title': article['title'],
                        'year': year
                    })
                    break

# Count business articles by year
business_by_year = defaultdict(int)
for art in business_articles_found:
    business_by_year[art['year']] += 1

# Calculate statistics
total_business = len(business_articles_found)
total_years = 11  # 2010-2020 inclusive
average_per_year = total_business / total_years

# Also calculate what percentage of European articles are business (for context)
total_european = len(europe_metadata)
estimated_business_total = int(total_european * (total_business / len(european_article_ids.intersection(set(str(a['article_id']) for a in all_articles))))) if european_article_ids.intersection(set(str(a['article_id']) for a in all_articles)) else 0
estimated_average = estimated_business_total / total_years if total_years > 0 else 0

result = {
    'articles_in_sample': len(all_articles),
    'european_articles_in_sample': len(business_articles_found),
    'total_european_articles_2010_2020': total_european,
    'business_articles_by_year': dict(sorted(business_by_year.items())),
    'average_from_sample': round(average_per_year, 2),
    'estimated_total_business_articles': estimated_business_total,
    'estimated_average_per_year': round(estimated_average, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969be2e66733a3d1d7f9c82', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969be2e66733a3d1d7f9c83', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969be2e66733a3d1d7f9c84', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969be2e66733a3d1d7f9c85', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969be2e66733a3d1d7f9c86', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_europe_articles': 14860, 'sample_articles_available': 13}, 'var_functions.query_db:26': [{'_id': '6969be2e66733a3d1d7f9c82', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969be2e66733a3d1d7f9c83', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969be2e66733a3d1d7f9c84', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969be2e66733a3d1d7f9c85', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969be2e66733a3d1d7f9c86', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:28': {'article_count': 5}}

exec(code, env_args)

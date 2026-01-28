code = """import json

# Get the file paths from storage
europe_metadata_file = locals()['var_functions.query_db:16']
articles_sample_file = locals()['var_functions.query_db:12']

# Load Europe metadata
with open(europe_metadata_file, 'r') as f:
    europe_metadata = json.load(f)

# Load articles sample
with open(articles_sample_file, 'r') as f:
    articles_sample = json.load(f)

# Create lookup for articles
articles_lookup = {str(art['article_id']): art for art in articles_sample}

# Find business articles in Europe
business_keywords = ['business', 'economy', 'stock', 'market', 'finance', 'financial', 'investment', 'company', 'bank', 'trade', 'wall st', 'wall street']

business_article_ids = set()
sample_europe_ids = set()

# Check Europe metadata against sample articles
for meta in europe_metadata:
    article_id = str(meta['article_id'])
    if article_id in articles_lookup:
        sample_europe_ids.add(article_id)
        article = articles_lookup[article_id]
        title_desc = (article.get('title', '') + ' ' + article.get('description', '')).lower()
        
        if any(keyword in title_desc for keyword in business_keywords):
            business_article_ids.add(article_id)

# Count by year
from collections import Counter
year_counts = Counter()
business_year_counts = Counter()

for meta in europe_metadata:
    article_id = str(meta['article_id'])
    year = meta['publication_date'][:4]
    year_counts[year] += 1
    
    if article_id in business_article_ids:
        business_year_counts[year] += 1

# Calculate for 2010-2020
total_business = 0
total_years = 2020 - 2010 + 1

for year in range(2010, 2021):
    year_str = str(year)
    total_business += business_year_counts.get(year_str, 0)

average_business = total_business / total_years if total_years > 0 else 0

result = {
    'average_business_per_year': round(average_business, 2),
    'total_business_2010_2020': total_business,
    'sample_matches': len(sample_europe_ids),
    'business_in_sample': len(business_article_ids)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860}, 'var_functions.execute_python:10': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860, 'sample_business_articles': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

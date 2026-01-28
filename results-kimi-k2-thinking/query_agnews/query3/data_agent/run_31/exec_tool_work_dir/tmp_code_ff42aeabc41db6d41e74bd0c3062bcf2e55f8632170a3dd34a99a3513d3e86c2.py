code = """import json
import os

# Load Europe metadata
metadata_file = locals()['var_functions.query_db:2']
with open(metadata_file, 'r') as f:
    europe_articles = json.load(f)

print(f"Total Europe articles in metadata: {len(europe_articles)}")

# Load a larger sample of articles
articles_sample_file = locals()['var_functions.query_db:12']
with open(articles_sample_file, 'r') as f:
    articles_sample = json.load(f)

print(f"Articles in sample: {len(articles_sample)}")

# Check article_id ranges
europe_article_ids = set(str(art['article_id']) for art in europe_articles)
sample_article_ids = set(str(art['article_id']) for art in articles_sample)

print(f"Europe article ID range: {min(europe_article_ids)} to {max(europe_article_ids)}")
print(f"Sample article ID range: {min(sample_article_ids)} to {max(sample_article_ids)}")

# Check overlap
overlap = europe_article_ids.intersection(sample_article_ids)
print(f"Overlapping articles: {len(overlap)}")

# Check if Europe articles exist in the sample
test_europe_ids = list(europe_article_ids)[:10]
print(f"First 10 Europe IDs: {test_europe_ids}")
found_in_sample = [aid for aid in test_europe_ids if aid in sample_article_ids]
print(f"Found in sample: {found_in_sample}")

# Check what Europe metadata looks like
print("Sample Europe metadata:", europe_articles[:3])

# Get year distribution
from collections import Counter
year_counts = Counter()
for art in europe_articles:
    date = art.get('publication_date', '')
    if date:
        year = date.split('-')[0]
        year_counts[year] += 1

print("Articles by year:", dict(year_counts))

# Try different approach: get ALL articles from MongoDB
# Since the dataset might be large, let's try without limit
print("\nTrying to get full articles collection...")
result = {'europe_count': len(europe_articles), 'sample_count': len(articles_sample), 'overlap': len(overlap), 'years': dict(year_counts)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860}, 'var_functions.execute_python:10': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860, 'sample_business_articles': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)

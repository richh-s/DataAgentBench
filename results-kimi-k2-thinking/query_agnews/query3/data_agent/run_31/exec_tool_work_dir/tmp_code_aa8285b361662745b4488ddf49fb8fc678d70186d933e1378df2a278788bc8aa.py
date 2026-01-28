code = """import json

# Load Europe metadata (stored in file)
metadata_file = locals()['var_functions.query_db:16']
print(f"Loading metadata from: {metadata_file}")
with open(metadata_file, 'r') as f:
    europe_metadata = json.load(f)

print(f"Total Europe articles (metadata): {len(europe_metadata)}")
print("Sample metadata entries:", europe_metadata[:3])

# Load articles sample (stored in file)
articles_file = locals()['var_functions.query_db:12']
print(f"\nLoading articles from: {articles_file}")
with open(articles_file, 'r') as f:
    articles_sample = json.load(f)

print(f"Total articles in sample: {len(articles_sample)}")
print("Sample articles:", articles_sample[:3])

# Check article_id ranges
europe_ids = set(str(art['article_id']) for art in europe_metadata)
sample_ids = set(str(art['article_id']) for art in articles_sample)

print(f"\nEurope article IDs range: min={min(europe_ids)}, max={max(europe_ids)}")
print(f"Sample article IDs range: min={min(sample_ids)}, max={max(sample_ids)}")

# Check overlap between Europe metadata and articles sample
overlap = europe_ids.intersection(sample_ids)
print(f"Articles found in both datasets: {len(overlap)}")

# Check year distribution
from collections import Counter
year_counts = Counter()
for art in europe_metadata:
    year = art['publication_date'].split('-')[0]
    year_counts[year] += 1

years_2010_2020 = {year: count for year, count in year_counts.items() if 2010 <= int(year) <= 2020}
print(f"\nArticles by year (2010-2020): {years_2010_2020}")

result = {
    'total_europe_articles': len(europe_metadata),
    'articles_per_year': years_2010_2020,
    'overlap_with_sample': len(overlap)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860}, 'var_functions.execute_python:10': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860, 'sample_business_articles': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

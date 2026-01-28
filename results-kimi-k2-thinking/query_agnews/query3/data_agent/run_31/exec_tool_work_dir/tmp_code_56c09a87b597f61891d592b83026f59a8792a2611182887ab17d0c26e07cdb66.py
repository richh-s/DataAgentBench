code = """import json

# Load Europe metadata (stored in file)
metadata_file = locals()['var_functions.query_db:16']
print("Loading metadata from file")
with open(metadata_file, 'r') as f:
    europe_metadata = json.load(f)

print("Total Europe articles (metadata): " + str(len(europe_metadata)))
print("Sample metadata entries: " + str(europe_metadata[:3]))

# Load articles sample (stored in file)
articles_file = locals()['var_functions.query_db:12']
print("\nLoading articles from file")
with open(articles_file, 'r') as f:
    articles_sample = json.load(f)

print("Total articles in sample: " + str(len(articles_sample)))
print("Sample articles: " + str(articles_sample[:3]))

# Check overlap
if len(europe_metadata) > 0 and len(articles_sample) > 0:
    europe_id = str(europe_metadata[0]['article_id'])
    sample_id = str(articles_sample[0]['article_id'])
    print("\nFirst Europe article_id: " + europe_id)
    print("First Sample article_id: " + sample_id)
    
    # Check if first Europe article is in sample
    found = False
    for art in articles_sample:
        if str(art['article_id']) == europe_id:
            found = True
            print("Found first Europe article in sample: " + str(art))
            break
    
    if not found:
        print("First Europe article not found in sample")

# Get year range distribution
from collections import Counter
year_counts = Counter()
for art in europe_metadata:
    date_str = art['publication_date']
    if date_str and len(date_str) >= 4:
        year = date_str[:4]
        year_counts[year] += 1

# Count only 2010-2020
relevant_years = {year: count for year, count in year_counts.items() if year >= '2010' and year <= '2020'}
total_relevant = sum(relevant_years.values())

print("\nArticles by year (2010-2020):")
for year in sorted(relevant_years.keys()):
    print(year + ": " + str(relevant_years[year]))

print("Total articles 2010-2020: " + str(total_relevant))

result = {
    'total_europe_articles': len(europe_metadata),
    'articles_2010_2020': total_relevant,
    'articles_per_year': relevant_years,
    'total_business_articles': 0  # Need to analyze content
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860}, 'var_functions.execute_python:10': {'average_business_articles_per_year': 0.0, 'total_business_articles_2010_2020': 0, 'business_articles_by_year': {}, 'total_europe_articles_2010_2020': 14860, 'sample_business_articles': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'_id': '6969c158a2d45f9a2caeb2af', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c158a2d45f9a2caeb2b0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c158a2d45f9a2caeb2b1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c158a2d45f9a2caeb2b2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c158a2d45f9a2caeb2b3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

code = """import json

# Load all data - articles is a list, metadata is a file path
articles = locals()['var_functions.query_db:16']  # List of articles
metadata_file = locals()['var_functions.query_db:5']  # File path

with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

print('Total articles in collection:', len(articles))
print('Total metadata records for 2015:', len(metadata_2015))

# Create a dictionary of articles for quick lookup
articles_dict = {a['article_id']: a for a in articles}

# Check sample metadata records and see if we can find matching articles
print('Sample metadata records:')
for i, meta in enumerate(metadata_2015[:10]):
    article_id = meta['article_id']
    article = articles_dict.get(article_id)
    print(f"{i+1}. Article ID: {article_id}, Region: {meta['region']}, Found: {article is not None}")
    if article:
        print(f"   Title: {article['title'][:80]}")

# Try to find all matches
matches = 0
for meta in metadata_2015:
    if meta['article_id'] in articles_dict:
        matches += 1

print(f'Found {matches} matches out of {len(metadata_2015)} metadata records')

# If matches exist, analyze by region
if matches > 0:
    from collections import Counter
    region_counts = Counter()
    for meta in metadata_2015:
        if meta['article_id'] in articles_dict:
            region_counts[meta['region']] += 1
    print('Region distribution of matched articles:')
    print(dict(region_counts))

result = {
    'total_articles': len(articles),
    'total_metadata_2015': len(metadata_2015),
    'total_matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'articles_in_database': 100, 'metadata_entries_2015': 6696, 'matching_articles_2015': 10}, 'var_functions.query_db:16': [{'_id': '6969d8cb28fdce3a67a0b6d0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d8cb28fdce3a67a0b6d1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d8cb28fdce3a67a0b6d2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d8cb28fdce3a67a0b6d3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d8cb28fdce3a67a0b6d4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

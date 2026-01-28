code = """import json

# Read the file path that contains query_db:2 results
file_path = var_functions.query_db:2

# Open and read the data
with open(file_path, 'r') as f:
    metadata_raw = json.load(f)

# Clean up metadata
metadata = []
for record in metadata_raw:
    if isinstance(record, dict):
        metadata.append(record)
    elif isinstance(record, str):
        # Handle string entries if any
        metadata.append(json.loads(record))

# Get Europe article IDs and their publication years
europe_articles = []
for record in metadata:
    try:
        article_id = int(record.get('article_id'))
        publication_date = record.get('publication_date', '')
        year = int(publication_date.split('-')[0])
        europe_articles.append({'article_id': article_id, 'year': year})
    except:
        continue

num_europe_articles = len(europe_articles)
years = sorted(list(set([item['year'] for item in europe_articles])))

print('__RESULT__:')
print(json.dumps({
    'num_europe_articles': num_europe_articles,
    'years_covered': years,
    'min_year': min(years),
    'max_year': max(years)
}))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'_id': '6969abd2d85d3c92a2e13bcc', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969abd2d85d3c92a2e13bcd', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969abd2d85d3c92a2e13bce', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969abd2d85d3c92a2e13bcf', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969abd2d85d3c92a2e13bd0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

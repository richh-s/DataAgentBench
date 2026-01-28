code = """import json, os

# Load Europe metadata
path = locals()['var_functions.query_db:2']
full_path = path.strip('"')
with open(full_path, 'r') as f:
    europe_meta = json.load(f)

# Group by year
from collections import defaultdict
year_counts = defaultdict(int)
year_articles = defaultdict(list)

for item in europe_meta:
    year = int(item["publication_date"].split('-')[0])
    year_counts[year] += 1
    year_articles[year].append(int(item["article_id"]))

# Sort years
sorted_years = sorted(year_counts.keys())

results = {
    "total_europe_articles": len(europe_meta),
    "year_range": [sorted_years[0], sorted_years[-1]],
    "articles_per_year": {year: year_counts[year] for year in sorted_years}
}
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 14860}, 'var_functions.execute_python:8': {'article_ids_count': 14860, 'sample_ids': [3, 9, 13, 14, 21]}, 'var_functions.query_db:10': [{'_id': '6969b4271b6a4815fa810439', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b4271b6a4815fa81043a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b4271b6a4815fa81043b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b4271b6a4815fa81043c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b4271b6a4815fa81043d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)

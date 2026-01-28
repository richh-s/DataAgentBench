code = """import json
import random

# Read Europe metadata
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    europe_metadata = json.load(f)

# Create a sample of articles to classify - 500 articles distributed across years
# Group by year first
from collections import defaultdict
articles_by_year = defaultdict(list)
for item in europe_metadata:
    year = item['publication_date'][:4]
    articles_by_year[year].append(item['article_id'])

# Determine how many samples per year to get ~500 total
years = sorted(articles_by_year.keys())
samples_per_year = 500 // len(years) + 1

sample_article_ids = []
for year in years:
    year_articles = articles_by_year[year]
    if len(year_articles) > samples_per_year:
        sample_article_ids.extend(random.sample(year_articles, samples_per_year))
    else:
        sample_article_ids.extend(year_articles)

# Add random samples if we don't have enough
while len(sample_article_ids) < 500:
    remaining = [item['article_id'] for item in europe_metadata if item['article_id'] not in sample_article_ids]
    if remaining:
        sample_article_ids.append(random.choice(remaining))
    else:
        break

# Shuffle the sample
random.shuffle(sample_article_ids)

print('__RESULT__:')
print(json.dumps({
    'total_samples': len(sample_article_ids),
    'sample_article_ids': sample_article_ids[:100]  # Return first 100 IDs
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': [{'_id': '6969c42c8494de621543382e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c42c8494de621543382f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c42c8494de6215433830', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c42c8494de6215433831', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c42c8494de6215433832', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:16': {'count': 14860, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_europe_articles': 14860, 'sample_europe_ids_int': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'sample_europe_ids_str': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63'], 'sample_article_ids_from_db': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'match_check': True}, 'var_functions.execute_python:24': {'total_articles': 14860, 'batch_size': 1000, 'num_batches': 15}, 'var_functions.execute_python:26': {'year_range': '2010 to 2020', 'total_years': 11, 'year_distribution': {'2020': 1366, '2016': 1364, '2015': 1357, '2017': 1391, '2013': 1354, '2010': 1306, '2018': 1351, '2019': 1328, '2014': 1372, '2011': 1316, '2012': 1355}, 'articles_2010': 1306, 'articles_2020': 1366}}

exec(code, env_args)

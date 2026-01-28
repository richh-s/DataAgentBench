code = """import json
import random

# Load all Europe articles from 2010-2020
var_name = 'var_functions.query_db:24'
metadata_path = locals()[var_name]

with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

# Group by year
articles_by_year = {}
for rec in metadata_records:
    year = int(rec['publication_date'][:4])
    if 2010 <= year <= 2020:
        if year not in articles_by_year:
            articles_by_year[year] = []
        articles_by_year[year].append(int(rec['article_id']))

# Show counts per year
year_counts = {year: len(ids) for year, ids in articles_by_year.items()}
print('Articles per year:')
for year in sorted(year_counts.keys()):
    print(f"{year}: {year_counts[year]}")

total_articles = sum(year_counts.values())
print(f'Total Europe articles (2010-2020): {total_articles}')

# Take a random sample of 500 articles from all years
all_article_ids = []
for year_ids in articles_by_year.values():
    all_article_ids.extend(year_ids)

sample_size = 500
random_sample = random.sample(all_article_ids, min(sample_size, len(all_article_ids)))

print(f'Taking random sample of {len(random_sample)} articles')

# Save the sample
result = {
    'total_by_year': year_counts,
    'total_all_years': total_articles,
    'sample_article_ids': random_sample,
    'sample_size': len(random_sample)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': '14860', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:18': {'collection': 'articles', 'filter': {'article_id': {'$in': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}}, 'projection': {'article_id': 1, 'title': 1, 'description': 1}}, 'var_functions.query_db:20': [{'_id': '6969cf6befa86fa502823d70', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cf6befa86fa502823d76', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969cf6befa86fa502823d7a', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969cf6befa86fa502823d7b', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969cf6befa86fa502823d82', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)

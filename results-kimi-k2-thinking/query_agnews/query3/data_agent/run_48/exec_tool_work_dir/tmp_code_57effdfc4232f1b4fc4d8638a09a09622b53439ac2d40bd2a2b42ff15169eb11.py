code = """import json
import re
from collections import defaultdict

# Read the Europe articles metadata file
file_path = locals()['var_functions.query_db:14']
with open(file_path, 'r') as f:
    europe_articles = json.load(f)

# Group article_ids by year
articles_by_year = defaultdict(list)
for item in europe_articles:
    article_id = int(item['article_id'])
    publication_date = item['publication_date']
    year = int(publication_date.split('-')[0])
    if 2010 <= year <= 2020:
        articles_by_year[year].append(article_id)

# Show summary
year_counts = {year: len(ids) for year, ids in sorted(articles_by_year.items())}
total_articles = sum(year_counts.values())

print('__RESULT__:')
print(json.dumps({
    'total_europe_articles_2010_2020': total_articles,
    'articles_per_year': year_counts,
    'sample_2015': articles_by_year[2015][:5] if 2015 in articles_by_year else []
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}, {'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '14', 'author_id': '223', 'region': 'Europe', 'publication_date': '2017-09-08'}, {'article_id': '21', 'author_id': '674', 'region': 'Europe', 'publication_date': '2020-04-06'}, {'article_id': '27', 'author_id': '244', 'region': 'Europe', 'publication_date': '2013-09-07'}, {'article_id': '43', 'author_id': '154', 'region': 'Europe', 'publication_date': '2010-03-12'}, {'article_id': '60', 'author_id': '530', 'region': 'Europe', 'publication_date': '2017-04-30'}, {'article_id': '62', 'author_id': '328', 'region': 'Europe', 'publication_date': '2018-09-12'}, {'article_id': '63', 'author_id': '83', 'region': 'Europe', 'publication_date': '2010-04-19'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'count': 14860, 'sample': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.execute_python:12': {'total_articles': 14860, 'num_batches': 30, 'first_batch': [3, 9, 13, 14, 21]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)

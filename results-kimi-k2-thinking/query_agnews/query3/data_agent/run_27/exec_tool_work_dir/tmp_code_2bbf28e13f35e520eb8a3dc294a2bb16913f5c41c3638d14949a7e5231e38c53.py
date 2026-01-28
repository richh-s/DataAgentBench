code = """import json

# Load Europe metadata to get article IDs
europe_file = locals()['var_functions.query_db:5']
with open(europe_file, 'r') as f:
    europe_metadata = json.load(f)

# Group by year
articles_by_year = {}
for article in europe_metadata:
    year = article['publication_date'][:4]
    if year not in articles_by_year:
        articles_by_year[year] = []
    articles_by_year[year].append(article['article_id'])

# Show years and counts
year_info = {}
for year in sorted(articles_by_year.keys()):
    year_info[year] = len(articles_by_year[year])

print('__RESULT__:')
print(json.dumps({
    'years': sorted(articles_by_year.keys()),
    'year_counts': year_info,
    'total_articles': len(europe_metadata)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_europe_articles': 14860, 'sample_articles': [{'article_id': '3', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '9', 'region': 'Europe', 'publication_date': '2016-05-24'}, {'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '14', 'region': 'Europe', 'publication_date': '2017-09-08'}, {'article_id': '21', 'region': 'Europe', 'publication_date': '2020-04-06'}]}, 'var_functions.query_db:10': [{'_id': '6969bfe00f136a1ca898fcfa', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969bfe00f136a1ca898fcfb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969bfe00f136a1ca898fcfc', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}], 'var_functions.execute_python:12': {'sample_articles_5': [{'article_id': '3', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '9', 'region': 'Europe', 'publication_date': '2016-05-24'}, {'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '14', 'region': 'Europe', 'publication_date': '2017-09-08'}, {'article_id': '21', 'region': 'Europe', 'publication_date': '2020-04-06'}], 'article_ids_sample': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63']}, 'var_functions.execute_python:16': {'total_articles': 14860, 'sample_article_ids': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63']}, 'var_functions.execute_python:20': {'total_articles': 14860, 'year_range': '2010-2020', 'articles_per_year': {'2020': 1366, '2016': 1364, '2015': 1357, '2017': 1391, '2013': 1354, '2010': 1306, '2018': 1351, '2019': 1328, '2014': 1372, '2011': 1316, '2012': 1355}, 'sample_articles_by_year': {'2010': ['43', '63', '66'], '2011': ['216', '371', '482'], '2012': ['383', '539', '576']}}}

exec(code, env_args)

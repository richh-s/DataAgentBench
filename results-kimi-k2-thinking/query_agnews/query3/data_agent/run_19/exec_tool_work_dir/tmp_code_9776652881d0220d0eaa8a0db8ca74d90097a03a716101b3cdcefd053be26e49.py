code = """import json
metadata_path = locals()['var_functions.query_db:2']
with open(metadata_path, 'r') as f:
    metadata = json.load(f)
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
counts = {year: 0 for year in years}
total_articles = 0
for item in metadata:
    year = int(item['publication_date'][:4])
    if year in counts:
        counts[year] += 1
        total_articles += 1
print('__RESULT__:')
print(json.dumps({'total_articles': total_articles, 'articles_per_year': counts}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.execute_python:8': 14860, 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json'}

exec(code, env_args)

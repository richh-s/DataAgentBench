code = """import json
import pandas as pd

# Read the metadata results
result_file = locals()['var_functions.query_db:2']

with open(result_file, 'r') as f:
    metadata = json.load(f)

# Convert article_id to integer
article_ids = [int(item['article_id']) for item in metadata]

# Get unique article_ids (though they should already be unique)
unique_article_ids = sorted(set(article_ids))

print('__RESULT__:')
print(json.dumps({
    'total_article_ids': len(unique_article_ids),
    'first_few': unique_article_ids[:10],
    'last_few': unique_article_ids[-10:]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_articles_by_year': [{'year': 2010, 'total_articles': 1306}, {'year': 2011, 'total_articles': 1316}, {'year': 2012, 'total_articles': 1355}, {'year': 2013, 'total_articles': 1354}, {'year': 2014, 'total_articles': 1372}, {'year': 2015, 'total_articles': 1357}, {'year': 2016, 'total_articles': 1364}, {'year': 2017, 'total_articles': 1391}, {'year': 2018, 'total_articles': 1351}, {'year': 2019, 'total_articles': 1328}, {'year': 2020, 'total_articles': 1366}], 'unique_years': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], 'total_articles': 14860}}

exec(code, env_args)

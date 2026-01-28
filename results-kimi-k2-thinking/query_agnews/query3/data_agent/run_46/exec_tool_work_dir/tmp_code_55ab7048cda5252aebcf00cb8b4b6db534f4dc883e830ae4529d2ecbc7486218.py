code = """import json
import pandas as pd
from collections import Counter

# Read the metadata results to get article IDs
result_file = locals()['var_functions.query_db:2']

with open(result_file, 'r') as f:
    metadata = json.load(f)

# Convert to DataFrame and extract article_ids and years
df_metadata = pd.DataFrame(metadata)
df_metadata['article_id'] = df_metadata['article_id'].astype(int)
df_metadata['year'] = pd.to_datetime(df_metadata['publication_date']).dt.year

# Group by year to see distribution
year_distribution = df_metadata['year'].value_counts().sort_index()
print('__RESULT__:')
print(json.dumps({
    'year_distribution': year_distribution.to_dict(),
    'total_articles': len(df_metadata)
}, default=str))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_articles_by_year': [{'year': 2010, 'total_articles': 1306}, {'year': 2011, 'total_articles': 1316}, {'year': 2012, 'total_articles': 1355}, {'year': 2013, 'total_articles': 1354}, {'year': 2014, 'total_articles': 1372}, {'year': 2015, 'total_articles': 1357}, {'year': 2016, 'total_articles': 1364}, {'year': 2017, 'total_articles': 1391}, {'year': 2018, 'total_articles': 1351}, {'year': 2019, 'total_articles': 1328}, {'year': 2020, 'total_articles': 1366}], 'unique_years': ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], 'total_articles': 14860}, 'var_functions.execute_python:8': {'total_article_ids': 14860, 'first_few': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'last_few': [127521, 127525, 127561, 127564, 127566, 127567, 127572, 127576, 127577, 127583]}}

exec(code, env_args)

code = """import json
articles_data = locals()['var_functions.query_db:2']
metadata_data = locals()['var_functions.query_db:5']
print('__RESULT__:')
print(json.dumps({'articles': len(articles_data) if isinstance(articles_data, list) else 'file', 
                  'metadata_sample': metadata_data[:2] if isinstance(metadata_data, list) else metadata_data}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_functions.query_db:6': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'region': 'Africa', 'publication_date': '2015-06-02'}, {'article_id': '67', 'region': 'Asia', 'publication_date': '2015-07-16'}, {'article_id': '70', 'region': 'Asia', 'publication_date': '2015-03-21'}, {'article_id': '74', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '86', 'region': 'Asia', 'publication_date': '2015-05-11'}, {'article_id': '97', 'region': 'North America', 'publication_date': '2015-09-16'}]}

exec(code, env_args)

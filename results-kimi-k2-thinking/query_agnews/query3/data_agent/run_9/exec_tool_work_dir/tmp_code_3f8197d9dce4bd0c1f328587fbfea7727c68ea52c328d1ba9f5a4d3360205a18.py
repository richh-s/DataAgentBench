code = """import json

# Read the article IDs file
article_ids_file = locals()['var_functions.execute_python:14']

with open(article_ids_file, 'r') as f:
    data = json.load(f)

article_ids = data['article_ids']

# Create MongoDB query
mongo_query = {
    "collection": "articles",
    "filter": {"article_id": {"$in": article_ids}},
    "projection": {"article_id": 1, "title": 1, "description": 1}
}

print('__RESULT__:')
print(json.dumps(mongo_query))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.list_db:5': ['articles'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': {'article_ids_count': 14860, 'sample_ids': [3, 9, 13, 14, 21]}}

exec(code, env_args)

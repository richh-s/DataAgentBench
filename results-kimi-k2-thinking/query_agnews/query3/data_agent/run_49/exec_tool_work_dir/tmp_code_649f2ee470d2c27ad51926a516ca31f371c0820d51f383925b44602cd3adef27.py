code = """import json

# Load the generated MongoDB query
var_name = 'var_functions.execute_python:12'
mongo_query_path = locals()[var_name]

with open(mongo_query_path, 'r') as f:
    mongo_query = json.loads(f.read())

article_ids = mongo_query['filter']['article_id']['$in']
print('Total article IDs:', len(article_ids))

# Create a smaller test query with just first 10 articles
test_article_ids = article_ids[:10]
test_query = {
    'collection': 'articles',
    'filter': {'article_id': {'$in': test_article_ids}},
    'projection': {'article_id': 1, 'title': 1, 'description': 1}
}

print('Test query for first 10 articles')
print('__RESULT__:')
print(json.dumps(test_query))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': '14860', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)

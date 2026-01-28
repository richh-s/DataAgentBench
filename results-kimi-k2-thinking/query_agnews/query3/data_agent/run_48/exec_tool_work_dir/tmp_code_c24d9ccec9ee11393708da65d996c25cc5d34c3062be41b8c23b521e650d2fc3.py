code = """import json

# Read the Europe articles file
file_path = locals()['var_functions.query_db:4']
with open(file_path, 'r') as f:
    europe_articles = json.load(f)

# Get all article IDs as integers
all_article_ids = [int(item['article_id']) for item in europe_articles]
total_articles = len(all_article_ids)

# Process in batches to avoid query size limits
batch_size = 500
batches = []
for i in range(0, total_articles, batch_size):
    batch = all_article_ids[i:i + batch_size]
    batches.append(batch)

print('__RESULT__:')
print(json.dumps({
    'total_articles': total_articles,
    'num_batches': len(batches),
    'first_batch': batches[0][:5]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}, {'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '14', 'author_id': '223', 'region': 'Europe', 'publication_date': '2017-09-08'}, {'article_id': '21', 'author_id': '674', 'region': 'Europe', 'publication_date': '2020-04-06'}, {'article_id': '27', 'author_id': '244', 'region': 'Europe', 'publication_date': '2013-09-07'}, {'article_id': '43', 'author_id': '154', 'region': 'Europe', 'publication_date': '2010-03-12'}, {'article_id': '60', 'author_id': '530', 'region': 'Europe', 'publication_date': '2017-04-30'}, {'article_id': '62', 'author_id': '328', 'region': 'Europe', 'publication_date': '2018-09-12'}, {'article_id': '63', 'author_id': '83', 'region': 'Europe', 'publication_date': '2010-04-19'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'count': 14860, 'sample': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}}

exec(code, env_args)

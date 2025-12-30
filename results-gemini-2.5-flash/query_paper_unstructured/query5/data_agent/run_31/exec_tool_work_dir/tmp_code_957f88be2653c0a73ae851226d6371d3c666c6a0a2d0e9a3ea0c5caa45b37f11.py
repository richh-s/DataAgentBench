code = """import json
with open(locals()['var_function-call-12033899987082541639'], 'r') as f:
    titles = json.load(f)

query_filter = {'filename': {'$in': [title + '.txt' for title in titles]}}
query_projection = {'filename': 1, 'text': 1, '_id': 0}

mongo_query = {
    'collection': 'paper_docs',
    'filter': query_filter,
    'projection': query_projection
}

print('__RESULT__:')
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-11236365375082320521': 'file_storage/function-call-11236365375082320521.json', 'var_function-call-12033899987082541639': 'file_storage/function-call-12033899987082541639.json'}

exec(code, env_args)

code = """import json

filepath = locals().get('var_functions.query_db:5')
with open(filepath) as f:
    data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'count': len(data),
    'first_keys': list(data[0].keys()) if data else [],
    'first_patent_info': data[0].get('Patents_info', '')[:200] if data else '',
    'first_citation_len': len(str(data[0].get('citation', ''))) if data else 0
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

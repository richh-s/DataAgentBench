code = """import json

# Access the query result directly from locals()
query_result = locals().get('var_functions.query_db:2')

# Check what we have
result = {
    'type': str(type(query_result)),
    'length': len(query_result) if hasattr(query_result, '__len__') else None,
    'is_list': isinstance(query_result, list),
}

if isinstance(query_result, list) and query_result:
    result['first_record_keys'] = list(query_result[0].keys())
    result['first_record_patents_info'] = query_result[0].get('Patents_info', '')
    result['has_uc'] = 'UNIV CALIFORNIA' in query_result[0].get('Patents_info', '')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition']}

exec(code, env_args)

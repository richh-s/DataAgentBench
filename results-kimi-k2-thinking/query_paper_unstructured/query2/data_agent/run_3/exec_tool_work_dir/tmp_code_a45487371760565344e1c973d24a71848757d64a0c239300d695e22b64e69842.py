code = """import json

# Check what's in the storage variable
citations_result = var_functions.query_db:2

print('Type of citations_result:', type(citations_result))
print('Value:', citations_result)

# If it's a list already
if isinstance(citations_result, list):
    print('Number of records:', len(citations_result))
    if citations_result:
        print('First record:', citations_result[0])
    result = {'count': len(citations_result), 'is_list': True}
else:
    result = {'type': str(type(citations_result)), 'is_list': False}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

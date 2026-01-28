code = """import json

# Access the stored results using the correct syntax
mongo_docs = locals()['var_functions.query_db:4']
funding_records = locals()['var_functions.query_db:6']

print('__RESULT__:')
print(json.dumps({
    "mongo_type": str(type(mongo_docs)),
    "funding_type": str(type(funding_records)),
    "mongo_is_list": isinstance(mongo_docs, list),
    "funding_is_list": isinstance(funding_records, list)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

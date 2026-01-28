code = """import json

civic_docs = json.load(open(locals()['var_functions.query_db:0']))
funding_data = json.load(open(locals()['var_functions.query_db:1']))

print('__RESULT__:')
print(json.dumps({'civic_docs': len(civic_docs), 'funding': len(funding_data)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)

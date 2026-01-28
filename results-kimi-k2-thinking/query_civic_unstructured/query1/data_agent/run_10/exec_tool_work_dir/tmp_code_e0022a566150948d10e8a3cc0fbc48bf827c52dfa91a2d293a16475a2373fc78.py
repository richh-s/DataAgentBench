code = """import json, re

civic_result = var_functions.query_db:2
funding_result = var_functions.query_db:5

# Load files
civic_docs = open(civic_result).read() if isinstance(civic_result, str) and civic_result.endswith('.json') else civic_result
funding_recs = open(funding_result).read() if isinstance(funding_result, str) and funding_result.endswith('.json') else funding_result

print('__RESULT__:')
print(json.dumps({'civic_count': len(civic_docs), 'funding_count': len(funding_recs)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

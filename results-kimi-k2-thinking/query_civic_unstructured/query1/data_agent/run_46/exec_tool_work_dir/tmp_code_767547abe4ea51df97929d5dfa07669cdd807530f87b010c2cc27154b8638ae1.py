code = """import json, re

# Check variable types and content
funding_var = var_functions.query_db:6
civic_var = var_functions.query_db:8

result = {
    'funding_type': str(type(funding_var)),
    'civic_type': str(type(civic_var)),
    'funding_preview': str(funding_var)[:200] if isinstance(funding_var, str) else 'not_string',
    'civic_preview': str(civic_var)[:200] if isinstance(civic_var, str) else 'not_string'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)

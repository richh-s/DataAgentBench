code = """import json

# Retrieve the stored results
funding_result = locals().get('var_functions.query_db:0')
civic_docs_result = locals().get('var_functions.query_db:2')

print("__RESULT__:")
print(json.dumps({
    'funding_result_type': str(type(funding_result)),
    'civic_docs_result_type': str(type(civic_docs_result)),
    'funding_result_preview': str(funding_result)[:500] if funding_result else None,
    'civic_docs_result_preview': str(civic_docs_result)[:500] if civic_docs_result else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

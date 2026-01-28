code = """import json

# Access the stored results - they might be file paths
lang_result = locals()['var_functions.query_db:0']
readme_result = locals()['var_functions.query_db:2']

# Check if these are file paths (strings) or data
type_lang = type(lang_result).__name__
type_readme = type(readme_result).__name__

print('__RESULT__:')
print(json.dumps({
    'lang_result_type': type_lang,
    'readme_result_type': type_readme,
    'lang_result_preview': str(lang_result)[:100] if isinstance(lang_result, str) else 'Not a string',
    'readme_result_preview': str(readme_result)[:100] if isinstance(readme_result, str) else 'Not a string'
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

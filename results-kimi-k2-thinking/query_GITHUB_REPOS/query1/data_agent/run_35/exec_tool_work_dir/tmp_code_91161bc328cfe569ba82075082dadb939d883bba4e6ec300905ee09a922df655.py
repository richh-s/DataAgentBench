code = """import json
import os

# The variables should be accessible via locals()
lang_result = locals()['var_functions.query_db:0']
readme_result = locals()['var_functions.query_db:2']

print('Language result type:', type(lang_result))
print('README result type:', type(readme_result))

print('Language result (first 200 chars):', str(lang_result)[:200])
print('README result (first 200 chars):', str(readme_result)[:200])

# Try to parse as JSON if it's a string
if isinstance(lang_result, str):
    try:
        lang_data = json.loads(lang_result)
        print('Parsed lang_data as JSON string, length:', len(lang_data))
    except:
        # Might be a file path
        if os.path.exists(lang_result):
            with open(lang_result, 'r') as f:
                lang_data = json.load(f)
            print('Read lang_data from file, length:', len(lang_data))
        else:
            print('lang_result is string but not JSON or file path')
            lang_data = []
else:
    lang_data = lang_result

if isinstance(readme_result, str):
    try:
        readme_data = json.loads(readme_result)
        print('Parsed readme_data as JSON string, length:', len(readme_data))
    except:
        # Might be a file path
        if os.path.exists(readme_result):
            with open(readme_result, 'r') as f:
                readme_data = json.load(f)
            print('Read readme_data from file, length:', len(readme_data))
        else:
            print('readme_result is string but not JSON or file path')
            readme_data = []
else:
    readme_data = readme_result

print('\nFinal counts:')
print('Languages:', len(lang_data) if lang_data else 0)
print('Readmes:', len(readme_data) if readme_data else 0)

__RESULT__ = json.dumps({'lang_count': len(lang_data) if lang_data else 0, 'readme_count': len(readme_data) if readme_data else 0})"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

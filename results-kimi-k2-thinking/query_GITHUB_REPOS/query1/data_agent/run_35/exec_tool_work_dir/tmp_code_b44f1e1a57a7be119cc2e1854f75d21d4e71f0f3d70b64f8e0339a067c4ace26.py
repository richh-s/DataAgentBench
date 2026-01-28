code = """import json
import os

# Get the previous query results
lang_result = locals()['var_functions.query_db:0']
readme_result = locals()['var_functions.query_db:2']

print('Language result type:', type(lang_result))
print('README result type:', type(readme_result))

# Check if results are strings (file paths) or already parsed data
lang_data = None
readme_data = None

if isinstance(lang_result, str):
    if os.path.exists(lang_result):
        with open(lang_result, 'r') as f:
            lang_data = json.load(f)
        print('Loaded languages from file:', lang_result)
    else:
        try:
            lang_data = json.loads(lang_result)
            print('Parsed languages from JSON string')
        except:
            print('Could not parse languages')
            lang_data = []
else:
    lang_data = lang_result

if isinstance(readme_result, str):
    if os.path.exists(readme_result):
        with open(readme_result, 'r') as f:
            readme_data = json.load(f)
        print('Loaded readmes from file:', readme_result)
    else:
        try:
            readme_data = json.loads(readme_result)
            print('Parsed readmes from JSON string')
        except:
            print('Could not parse readmes')
            readme_data = []
else:
    readme_data = readme_result

# Verify data loaded
print('Languages count:', len(lang_data) if lang_data else 0)
print('Readmes count:', len(readme_data) if readme_data else 0)

__RESULT__ = json.dumps({'success': True, 'lang_count': len(lang_data) if lang_data else 0, 'readme_count': len(readme_data) if readme_data else 0})"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

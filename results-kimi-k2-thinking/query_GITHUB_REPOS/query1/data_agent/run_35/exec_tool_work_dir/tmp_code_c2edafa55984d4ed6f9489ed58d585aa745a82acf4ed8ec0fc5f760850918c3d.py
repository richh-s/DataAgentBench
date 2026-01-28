code = """import json
import re

# Read files - since result is large, it might be a file path
# Let's try reading the results directly first
lang_data = locals()['var_functions.query_db:0']
readme_data = locals()['var_functions.query_db:2']

# Debug type and content
print('Type of lang_data:', type(lang_data))
print('Type of readme_data:', type(readme_data))

# If they're file paths, read the files
if isinstance(lang_data, str) and '.json' in lang_data:
    with open(lang_data, 'r') as f:
        languages = json.load(f)
else:
    languages = lang_data

if isinstance(readme_data, str) and '.json' in readme_data:
    with open(readme_data, 'r') as f:
        readmes = json.load(f)
else:
    readmes = readme_data

print('Languages loaded:', len(languages) if languages else 0)
print('Readmes loaded:', len(readmes) if readmes else 0)

# Show sample data
if languages:
    print('Sample language entry:', json.dumps(languages[0]))
if readmes:
    print('Sample readme entry:', json.dumps(readmes[0]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

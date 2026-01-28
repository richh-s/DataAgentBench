code = """import json
import re

# Read the language data file
lang_file_path = locals()['var_functions.query_db:0']
with open(lang_file_path, 'r') as f:
    languages_data = json.load(f)

# Read the README content data file
readme_file_path = locals()['var_functions.query_db:2']
with open(readme_file_path, 'r') as f:
    readme_data = json.load(f)

print(f"Total language records: {len(languages_data)}")
print(f"Total README records: {len(readme_data)}")

# Look at a sample of the data
print("\nSample language record:")
print(json.dumps(languages_data[0], indent=2))

print("\nSample README record:")
print(json.dumps(readme_data[0], indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)

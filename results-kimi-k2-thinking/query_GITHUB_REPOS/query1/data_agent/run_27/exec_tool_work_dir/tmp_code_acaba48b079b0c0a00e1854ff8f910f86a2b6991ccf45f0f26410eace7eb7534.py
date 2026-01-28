code = """import json
import os
import sys

# Check available variables
vars_list = sorted([k for k in locals().keys() if k.startswith('var_') or k.startswith('functions')])
print("Available variables:", len(vars_list))
for v in vars_list:
    print("  ", v)

# Also check files in /tmp
import glob
tmp_files = glob.glob('/tmp/*')
print("\nFiles in /tmp:", len(tmp_files))
for f in tmp_files[:5]:  # Show first 5
    print("  ", f)

result = {"vars_count": len(vars_list), "files_count": len(tmp_files)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)

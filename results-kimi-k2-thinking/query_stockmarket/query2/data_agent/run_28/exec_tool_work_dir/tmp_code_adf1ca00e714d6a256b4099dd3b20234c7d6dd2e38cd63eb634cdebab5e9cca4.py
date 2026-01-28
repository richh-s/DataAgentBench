code = """import json
import os
import glob

# Find the actual JSON files
tmp_dir = '/tmp'
files = glob.glob(f'{tmp_dir}/**/*.json', recursive=True) + glob.glob(f'{tmp_dir}/var_*')

print('Files found:', files[:15])
print('Count:', len(files))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}}

exec(code, env_args)

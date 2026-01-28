code = """import json
import os

# Determine actual file paths
# Results are stored in /tmp/ directory with the variable names as keys
stockinfo_path = '/tmp/var_functions.query_db:2.json'
stocktables_path = '/tmp/var_functions.list_db:5.json'

# Check if files exist
print('Checking paths:', stockinfo_path, os.path.exists(stockinfo_path))
print('Checking paths:', stocktables_path, os.path.exists(stocktables_path))

# List files in /tmp/
import glob
tmp_files = glob.glob('/tmp/var_functions.*')
print('Available files:', tmp_files[:10])"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:5'], 'var_functions.execute_python:16': {'stockinfo_type': "<class 'str'>", 'stockinfo_length': 0, 'stocktables_type': "<class 'str'>", 'stocktables_length': 0, 'stockinfo_sample': None, 'stocktables_sample': None}}

exec(code, env_args)

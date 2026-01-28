code = """import json
import os
import re

# Let's check what files are in the /tmp directory
tmp_files = [f for f in os.listdir('/tmp') if f.startswith('tmp')]
print("Temporary files:", tmp_files)

# Let's also check the variables that should be available
print("Available variables:", list(locals().keys()))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)

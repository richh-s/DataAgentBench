code = """import os
import glob
import json

# Find all json temp files
json_files = glob.glob('/tmp/**/*.json', recursive=True)
print('Found JSON files:')
for f in json_files:
    print(f'  {f}')

# Find the civic docs file - look for the one with 'tmp7' or 'civic' in the name
civic_candidates = [f for f in json_files if 'tmp7' in f or 'civic' in f.lower()]
funding_candidates = [f for f in json_files if 'tmp8' in f or 'tmp9' in f or 'tmp10' in f or 'funding' in f.lower()]

print(f'\nCivic doc candidates: {civic_candidates}')
print(f'Funding data candidates: {funding_candidates}')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)

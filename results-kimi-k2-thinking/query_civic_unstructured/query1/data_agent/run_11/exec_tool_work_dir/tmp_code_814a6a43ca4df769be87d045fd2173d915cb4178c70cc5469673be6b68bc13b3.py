code = """import json
import re
import os

# Load the data
civic_docs_path = 'file_storage/functions.query_db:8.json'
funding_data_path = 'file_storage/functions.query_db:2.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

# Look at the structure
sample_doc = civic_docs[0] if civic_docs else None
sample_funding = funding_data[0] if funding_data else None

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'sample_doc_keys': list(sample_doc.keys()) if sample_doc else None,
    'sample_doc_text_preview': sample_doc.get('text', '')[:500] if sample_doc else None,
    'funding_data_count': len(funding_data),
    'sample_funding': sample_funding
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'civic_docs_count': 0, 'civic_docs_sample': None, 'funding_data_count': 0, 'funding_data_sample': None}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 38, 'sample_doc': 'f'}, 'var_functions.execute_python:12': {'json_files': [], 'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6', 'var_functions.query_db:8', 'var_functions.execute_python:10'], 'current_dir_files': ['tmp_code_b262fd095b36b5236393345bb8d1ca0a3d195790acfd855432118fb96265da25.py', 'tmp_code_ec12d0aa8e6ef28366e7553f1de624160a0ec8fe0b8dcd1d857bdc21d2ac6101.py', 'tmp_code_571c1044f3b97a69aa8a7d818bee03068db011ff8bc05dfe8973c1b9d8bffe19.py', 'tmp_code_e5ff25f71b3e4ce5f3ce1c812f4ebf25f913fb64b2bed77fbaa660f1d36156fc.py', 'file_storage']}, 'var_functions.execute_python:14': {'civic_docs_loaded': 38, 'funding_data_loaded': 38, 'civic_docs_type': 'str'}, 'var_functions.execute_python:16': {'civic_docs_path': 'file_storage/functions.query_db:8.json', 'funding_data_path': 'file_storage/functions.query_db:2.json', 'civic_docs_loaded': 5, 'funding_data_loaded': 276}}

exec(code, env_args)
